# attack-simulation/app/services/simulation_handler.py

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

async def handle_simulation_and_log(
    sim_type: str,
    params: Any, 
    simulation_function: Callable,
    background_tasks: BackgroundTasks
):
    start_time = datetime.now(timezone.utc)
    simulation_run_id = str(ObjectId())
    params_for_mongo = serialize_pydantic_for_mongo(params)
    
    target_url_str = str(getattr(params, 'target_url', 'N/A'))
    target_method_value = "N/A"
    if hasattr(params, 'method') and isinstance(params.method, Enum): 
        target_method_value = params.method.value

    initial_log_data = {
        "simulation_id": simulation_run_id,
        "simulation_type": sim_type,
        "target_details": {"url": target_url_str, "method": target_method_value},
        "parameters_used": params_for_mongo,
        "status": "running",
        "start_time": start_time,
        "summary": {"message": "Simulation has been initiated..."},
        "created_at": datetime.now(timezone.utc)
    }
    
    db_conn = db_manager.get_db()
    sim_collection: Collection | None = None
    if db_conn is not None:
        sim_collection = db_conn.simulations_log
        try:
            await asyncio.to_thread(sim_collection.insert_one, initial_log_data)
        except Exception as e:
            print(f"❌ Error writing initial log: {e}")
            sim_collection = None
    else:
        print("⚠️ No database connection, initial log skipped.")

    async def progress_callback(data: dict):
        """Callback function to send progress updates over WebSocket."""
        await ws_manager.send_json_update(simulation_run_id, data)

    async def simulation_task():
        try:
            # ...
            # Artık tüm simülasyonlar aynı imzaya sahip olduğu için if/else'e gerek yok
            sim_result_details = await simulation_function(params, progress_callback, simulation_run_id)

            # Simülasyon tipine göre çağrı şeklini belirle
            if sim_type == "ddos":
                # DDoS simülasyonuna 'simulation_run_id'yi de gönderiyoruz
                sim_result_details = await simulation_function(params, progress_callback, simulation_run_id)
            elif sim_type in ["brute_force", "sql_injection"]:
                # Diğerleri hala callback alıyor ama ID'ye ihtiyaçları yok (şimdilik)
                sim_result_details = await simulation_function(params, progress_callback)
            else:
                # Callback almayan eski bir simülasyon varsa diye (güvenlik için)
                sim_result_details = await simulation_function(params)
            
            end_time = datetime.now(timezone.utc)
            duration = (end_time - start_time).total_seconds()
            
            summary_data = {}
            if sim_type == "ddos":
                summary_data = { "total_requests_attempted": sim_result_details.get("total_requests_attempted"), "successful_requests": sim_result_details.get("successful_requests"), "failed_requests": sim_result_details.get("failed_requests"), "requests_per_second": sim_result_details.get("requests_per_second"), "average_request_time_ms": sim_result_details.get("average_request_time_ms"), "status_codes_distribution": sim_result_details.get("status_codes_distribution") }
            elif sim_type == "brute_force":
                summary_data = { "total_attempts_made": sim_result_details.get("total_attempts_made"), "credentials_found_count": len(sim_result_details.get("credentials_found", [])), "simulation_halted_early": sim_result_details.get("simulation_halted_early") }
            elif sim_type == "sql_injection":
                summary_data = { "total_payloads_tested": sim_result_details.get("total_payloads_tested"), "potentially_vulnerable_findings_count": len(sim_result_details.get("potentially_vulnerable_findings", [])) }
            
            if sim_collection is not None:
                update_data = { "$set": { "status": "completed", "end_time": end_time, "duration_seconds": round(duration, 3), "summary": summary_data, "raw_result": sim_result_details } }
                await asyncio.to_thread(sim_collection.update_one, {"simulation_id": simulation_run_id}, update_data)
            
            await progress_callback({ "type": "completed", "message": "Simulation finished and logged.", "final_results": sim_result_details })
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
        "simulation_run_id": simulation_run_id,
        "params_received": params_for_mongo
    }