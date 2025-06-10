from app.database import db_manager, log_to_db
from datetime import datetime, time, timezone, date
from enum import Enum
from typing import Any 
from fastapi import FastAPI, HTTPException, BackgroundTasks
import traceback
from app.core.utils import serialize_pydantic_for_mongo
from bson import ObjectId


async def handle_simulation_and_log(
    sim_type: str,
    params: Any, 
    simulation_function: callable,
    background_tasks: BackgroundTasks
):
    start_time = datetime.now(timezone.utc)
    simulation_run_id = str(ObjectId())
    params_for_mongo = serialize_pydantic_for_mongo(params)
    
    target_url_str = str(getattr(params, 'target_url', 'N/A'))
    target_method_value = "N/A"
    if hasattr(params, 'method') and isinstance(params.method, Enum): 
        target_method_value = params.method.value

    async def simulation_task():
        try:
            print(f"{sim_type.upper()} simülasyonu ({simulation_run_id}) arka planda başlatılıyor...")
            sim_result_details = await simulation_function(params)
            end_time = datetime.now(timezone.utc)
            duration = (end_time - start_time).total_seconds()

            summary_data = {}
            if sim_type == "ddos":
                summary_data = {
                    "total_requests_attempted": sim_result_details.get("total_requests_attempted"),
                    "successful_requests": sim_result_details.get("successful_requests"),
                    "failed_requests": sim_result_details.get("failed_requests"),
                    "requests_per_second": sim_result_details.get("requests_per_second"),
                    "average_request_time_ms": sim_result_details.get("average_request_time_ms"),
                    "status_codes_distribution": sim_result_details.get("status_codes_distribution")
                }
            elif sim_type == "brute_force":
                summary_data = {
                    "total_attempts_made": sim_result_details.get("total_attempts_made"),
                    "credentials_found_count": len(sim_result_details.get("credentials_found", [])),
                    "simulation_halted_early": sim_result_details.get("simulation_halted_early")
                }
            elif sim_type == "sql_injection":
                summary_data = {
                    "total_payloads_tested": sim_result_details.get("total_payloads_tested"),
                    "potentially_vulnerable_findings_count": len(sim_result_details.get("potentially_vulnerable_findings", []))
                }
            
            log_data = {
                "simulation_id": simulation_run_id,
                "simulation_type": sim_type,
                "target_details": {"url": target_url_str, "method": target_method_value},
                "parameters_used": params_for_mongo,
                "status": "completed",
                "start_time": start_time,
                "end_time": end_time,
                "duration_seconds": round(duration, 3),
                "summary": summary_data,
                "raw_result": sim_result_details
            }
            await log_to_db("simulations_log", log_data, db_manager)
            print(f"{sim_type.upper()} simülasyonu ({simulation_run_id}) tamamlandı ve loglandı.")

        except Exception as e:
            end_time = datetime.now(timezone.utc)
            duration = (end_time - start_time).total_seconds()
            print(f" {sim_type.upper()} simülasyonu ({simulation_run_id}) sırasında hata: {e}")
            print(traceback.format_exc())
            log_data_error = {
                "simulation_id": simulation_run_id,
                "simulation_type": sim_type,
                "target_details": {"url": target_url_str, "method": target_method_value},
                "parameters_used": params_for_mongo,
                "status": "failed",
                "start_time": start_time,
                "end_time": end_time,
                "duration_seconds": round(duration, 3),
                "error_message": str(e),
                "error_traceback": traceback.format_exc()
            }
            await log_to_db("simulations_log", log_data_error, db_manager)

    background_tasks.add_task(simulation_task)
    return {
        "status": f"{sim_type.upper()} simulation started in background",
        "simulation_run_id": simulation_run_id,
        "params_received": params_for_mongo
    }
