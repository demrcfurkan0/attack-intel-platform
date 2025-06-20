from app.simulations.simulation_params import DDoSParams
from typing import List, Dict, Any, Callable, Coroutine
import httpx
import asyncio
import random
import time
import os
from app.core import state
from app.services.simulation_handler import handle_simulation_and_log

INTERNAL_API_BASE_URL = os.getenv("INTERNAL_API_BASE_URL", "http://localhost:8000")

def generate_fake_ddos_features():
    if not state.feature_columns: return {}
    features = {key: 0.0 for key in state.feature_columns}
    
    features.update({
        'Flow_Duration':            max(0, random.uniform(4.09e+07 - 2e+07, 4.09e+07 + 2e+07)),
        'Total_Fwd_Packets':        max(0, random.uniform(5.83 - 2, 5.83 + 10)),
        'Total_Bwd_Packets':        max(0, random.uniform(4.50 - 2, 4.50 + 10)),
        'Total_Fwd_Bytes':          max(0, random.uniform(959.8 - 400, 959.8 + 1500)),
        'Total_Bwd_Bytes':          max(0, random.uniform(7967.8 - 3000, 7967.8 + 15000)),
        'Fwd_Packet_Length_Mean':   max(0, random.uniform(38.59 - 20, 38.59 + 50)),
        'Bwd_Packet_Length_Mean':   max(0, random.uniform(1258.6 - 500, 1258.6 + 1000)),
        'Packet_Length_Mean':       max(0, random.uniform(603.7 - 300, 603.7 + 500)),
        'SYN_Flag_Count':           0,
        'FIN_Flag_Count':           random.choice([0, 1]),
    })
    return features

async def trigger_prediction(simulation_id: str):
    try:
        features = generate_fake_ddos_features()
        async with httpx.AsyncClient() as internal_client:
            predict_url = f"{INTERNAL_API_BASE_URL}/api/predict"
            await internal_client.post(
                predict_url, 
                json={
                    "features": features, 
                    "source_info": f"ddos_simulation_run_{simulation_id}",
                    "simulation_id": simulation_id 
                },
                timeout=10.0
            )
    except Exception as e:
        print(f"Error during internal prediction call: {e}")


async def run_ddos_simulation(
    params: DDoSParams, 
    progress_callback: Callable[[Dict[str, Any]], Coroutine[Any, Any, None]],
    simulation_run_id: str 
) -> Dict[str, Any]:
    print(f"Starting DDoS Simulation: Target={params.target_url}, Requests={params.num_requests}")
    successful_requests = 0
    failed_requests = 0
    status_codes_distribution: Dict[str, int] = {}
    request_times: List[float] = []
    start_time_total = time.time()
    total_requests_made = 0

    async def send_single_request(session: httpx.AsyncClient, req_id: int):
        nonlocal successful_requests, failed_requests, status_codes_distribution, request_times, total_requests_made
        if params.random_delay_ms_max > 0:
            await asyncio.sleep(random.randint(0, params.random_delay_ms_max) / 1000.0)

        start_req_time = time.time()
        try:
              # Send GET or POST request
            if params.method.value == "POST":
                response = await session.post(str(params.target_url), json=params.payload, headers=params.headers, timeout=params.timeout_seconds)
            else:
                response = await session.get(str(params.target_url), headers=params.headers, timeout=params.timeout_seconds)
            # Record statistics
            request_times.append(time.time() - start_req_time)
            status_code_str = str(response.status_code)
            status_codes_distribution[status_code_str] = status_codes_distribution.get(status_code_str, 0) + 1
            
            if 200 <= response.status_code < 400: successful_requests += 1
            else: failed_requests += 1

        except (httpx.TimeoutException, httpx.RequestError):
            failed_requests += 1
        finally:
            total_requests_made += 1
            # After each request trigger a prediction to simulate detection
            asyncio.create_task(trigger_prediction(simulation_run_id))
            print(f"[TRIGGER] Sending fake features to prediction endpoint for sim_id: {simulation_run_id}")
            
            if total_requests_made % 50 == 0 or total_requests_made == params.num_requests:
                progress_data = {
                    "type": "progress",
                    "completed": total_requests_made,
                    "total": params.num_requests,
                    "successful": successful_requests,
                    "failed": failed_requests,
                    "message": f"Sent {total_requests_made}/{params.num_requests} requests..."
                }
                await progress_callback(progress_data)

    semaphore = asyncio.Semaphore(params.concurrency)
    async def worker(session: httpx.AsyncClient, req_id: int):
        async with semaphore:
            await send_single_request(session, req_id)
    # Create and run all request tasks
    async with httpx.AsyncClient(verify=False) as client:
        tasks = [worker(client, i) for i in range(params.num_requests)]
        await asyncio.gather(*tasks)

    end_time_total = time.time()
    # Calculate final performance
    total_duration_seconds = end_time_total - start_time_total
    requests_per_second = params.num_requests / total_duration_seconds if total_duration_seconds > 0 else 0
    avg_request_time_ms = (sum(request_times) / len(request_times) * 1000) if request_times else 0
    # Compile the final result
    result = {
        "target_url": str(params.target_url),
        "method": params.method.value,
        "target_ip": getattr(params, "target_ip", "N/A"),
        "packet_rate": getattr(params, "packet_rate", "N/A"),
        "duration_seconds": getattr(params, "duration_seconds", "N/A"),
        "total_requests_attempted": params.num_requests,
        "successful_requests": successful_requests,
        "failed_requests": failed_requests,
        "status_codes_distribution": status_codes_distribution,
        "total_duration_seconds": round(total_duration_seconds, 3),
        "requests_per_second": round(requests_per_second, 2),
        "average_request_time_ms": round(avg_request_time_ms, 2)
    }
    
    await progress_callback({"type": "final_summary", "message": "DDoS simulation completed."})
    return result