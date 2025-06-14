from app.database import db_manager
from datetime import datetime, timezone
from enum import Enum
from typing import Any, Callable, Coroutine, Dict
from fastapi import BackgroundTasks
import traceback
from app.core.utils import serialize_pydantic_for_mongo
from app.core.ws_manager import manager as ws_manager
from bson import ObjectId
import asyncio
from pymongo.collection import Collection
from app.database.database import get_mongo_client

async def handle_simulation_and_log(
    sim_type: str,
    params: Any, 
    simulation_function: Callable,
    background_tasks: BackgroundTasks
):
    start_time = datetime.now(timezone.utc)
    simulation_run_id = str(ObjectId())
    params_for_mongo = serialize_pydantic_for_mongo(params)
    target_ip = getattr(params, 'target_ip', 'N/A')
    packet_rate = getattr(params, 'packet_rate', 'N/A')
    duration_seconds = getattr(params, 'duration_seconds', 'N/A')
    target_url_str = str(getattr(params, 'target_url', 'N/A'))
    target_method_value = "N/A"
    if hasattr(params, 'method') and isinstance(params.method, Enum): 
        target_method_value = params.method.value

    initial_log_data = {
        "simulation_id": simulation_run_id,
        "simulation_type": sim_type,
        "target_details": {
            "url": target_url_str,
            "method": target_method_value,
            "ip": target_ip
        },
        "parameters_used": params_for_mongo,
        "packet_rate": packet_rate,
        "duration_seconds": duration_seconds,
        "status": "running",
        "start_time": start_time,
        "summary": {"message": "Simulation initiated..."},
        "created_at": datetime.now(timezone.utc)
    }

    db_conn = db_manager.get_db()
    sim_collection: Collection | None = None
    if db_conn is not None:
        sim_collection = db_conn.simulations_log
        try:
            await asyncio.to_thread(sim_collection.insert_one, initial_log_data)
            print("📥 Inserting initial simulation log...")
        except Exception as e:
            print(f"❌ Error writing initial log: {e}")
            sim_collection = None

    async def progress_callback(data: dict):
        await ws_manager.send_json_update(simulation_run_id, data)

    async def simulation_task():
        try:
            print(f"{sim_type.upper()} simulation ({simulation_run_id}) starting in background...")

            sim_result_details = await simulation_function(params, progress_callback, simulation_run_id)

            # --- PREDICTION LOG EKLEME ---
            db_conn = db_manager.get_db()
            if db_conn is not None:
                db_conn.prediction_logs.insert_one({
                    "source_of_data": f"{sim_type}_simulation",
                    "created_at": datetime.utcnow(),
                    "prediction_result": {
                        "prediction_label": sim_result_details.get("label", "UNKNOWN"),
                        "confidence_score": sim_result_details.get("confidence", 0.0)
                    },
                    "is_attack": sim_result_details.get("label", "BENIGN") != "BENIGN"
                })

            end_time = datetime.now(timezone.utc)
            duration = (end_time - start_time).total_seconds()

            if sim_collection is not None:
                update_data = { "$set": { 
                    "status": "completed", 
                    "end_time": end_time, 
                    "duration_seconds": round(duration, 3), 
                    "summary": sim_result_details, 
                    "raw_result": sim_result_details 
                }}
                await asyncio.to_thread(sim_collection.update_one, {"simulation_id": simulation_run_id}, update_data)

            await progress_callback({ "type": "completed", "message": "Simulation finished and logged." })
            print(f"{sim_type.upper()} simulation ({simulation_run_id}) completed and logged.")

        except Exception as e:
            end_time = datetime.now(timezone.utc)
            print(f"Error during {sim_type.upper()} simulation ({simulation_run_id}): {e}")
            print(traceback.format_exc())

            if sim_collection is not None:
                update_data_error = { "$set": { "status": "failed", "end_time": end_time, "error_message": str(e), "error_traceback": traceback.format_exc() } }
                await asyncio.to_thread(sim_collection.update_one, {"simulation_id": simulation_run_id}, update_data_error)

            await progress_callback({ "type": "error", "message": str(e) })

    background_tasks.add_task(simulation_task)
    return {
        "status": f"{sim_type.upper()} simulation started in background",
        "simulation_run_id": simulation_run_id
    }
    
    