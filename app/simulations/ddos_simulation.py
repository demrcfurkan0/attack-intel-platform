from app.simulations.simulation_params import DDoSParams
from typing import Optional, List, Dict, Any
import httpx
import asyncio
import random
import time
from app.simulations.utils import HTTPMethod

async def run_ddos_simulation(params: DDoSParams) -> Dict[str, Any]:
    print(f"Starting DDoS Simulation: Target={params.target_url}, Requests={params.num_requests}, Concurrency={params.concurrency}")
    successful_requests = 0
    failed_requests = 0
    status_codes_distribution: Dict[str, int] = {} 
    request_times: List[float] = []
    start_time_total = time.time()

    async def send_single_request(session: httpx.AsyncClient, req_id: int):
        nonlocal successful_requests, failed_requests, status_codes_distribution, request_times
        if params.random_delay_ms_max > 0:
            delay_seconds = random.randint(0, params.random_delay_ms_max) / 1000.0
            await asyncio.sleep(delay_seconds)

        start_req_time = time.time()
        try:
            if params.method == HTTPMethod.POST:
                response = await session.post(
                    str(params.target_url), 
                    json=params.payload,
                    headers=params.headers,
                    timeout=params.timeout_seconds
                )
            else:
                response = await session.get(
                    str(params.target_url), 
                    headers=params.headers,
                    timeout=params.timeout_seconds
                )
            
            end_req_time = time.time()
            request_times.append(end_req_time - start_req_time)
            status_code_str = str(response.status_code)
            status_codes_distribution[status_code_str] = status_codes_distribution.get(status_code_str, 0) + 1
            
            if 200 <= response.status_code < 400:
                successful_requests += 1
            else:
                failed_requests += 1
        except httpx.TimeoutException:
            failed_requests +=1
            status_codes_distribution["timeout"] = status_codes_distribution.get("timeout", 0) + 1
        except httpx.RequestError:
            failed_requests += 1
            status_codes_distribution["error"] = status_codes_distribution.get("error", 0) + 1
        except Exception:
            failed_requests += 1
            status_codes_distribution["unknown_error"] = status_codes_distribution.get("unknown_error", 0) + 1

    semaphore = asyncio.Semaphore(params.concurrency)
    async def worker(session: httpx.AsyncClient, req_id: int):
        async with semaphore:
            await send_single_request(session, req_id)

    async with httpx.AsyncClient(verify=False) as client:
        tasks = [worker(client, i) for i in range(params.num_requests)]
        await asyncio.gather(*tasks, return_exceptions=True)

    end_time_total = time.time()
    total_duration_seconds = end_time_total - start_time_total
    requests_per_second = params.num_requests / total_duration_seconds if total_duration_seconds > 0 else 0
    avg_request_time_ms = (sum(request_times) / len(request_times) * 1000) if request_times else 0

    result = {
        "target_url": str(params.target_url),
        "method": params.method.value,
        "total_requests_attempted": params.num_requests,
        "successful_requests": successful_requests,
        "failed_requests": failed_requests,
        "status_codes_distribution": status_codes_distribution,
        "total_duration_seconds": round(total_duration_seconds, 3),
        "requests_per_second": round(requests_per_second, 2),
        "average_request_time_ms": round(avg_request_time_ms, 2)
    }
    print(f"DDoS Simulation Completed: {result}")
    return result