import asyncio
import os
import random
import traceback
from typing import Any, Callable, Coroutine, Dict, List

import httpx

from app.core import state
from app.simulations.simulation_params import SQLInjectionParams
from app.simulations.utils import HTTPMethod, SQLI_PAYLOADS

INTERNAL_API_BASE_URL = os.getenv("INTERNAL_API_BASE_URL", "http://localhost:8000")


def generate_fake_sqli_features():
    if not state.feature_columns: return {}
    features = {key: 0.0 for key in state.feature_columns}
# larger forward bytes for payload
    features.update({
        'Flow_Duration':            max(0, random.uniform(2.87e+06 - 1e+06, 2.87e+06 + 2e+06)),
        'Total_Fwd_Packets':        max(0, random.uniform(3.04 - 1, 3.04 + 3)),
        'Total_Bwd_Packets':        max(0, random.uniform(2.66 - 1, 2.66 + 3)),
        'Total_Fwd_Bytes':          max(0, random.uniform(316.0 - 150, 316.0 + 500)), # Payload 
        'Total_Bwd_Bytes':          max(0, random.uniform(1286.2 - 500, 1286.2 + 1500)), # Error
        'Fwd_Packet_Length_Mean':   max(0, random.uniform(71.05 - 30, 71.05 + 100)),
        'Bwd_Packet_Length_Mean':   max(0, random.uniform(327.1 - 150, 327.1 + 300)),
        'Packet_Length_Mean':       max(0, random.uniform(166.3 - 80, 166.3 + 200)),
        'SYN_Flag_Count':           0,
        'FIN_Flag_Count':           0,
    })
    return features

async def trigger_prediction(simulation_id: str):
    try:
        features = generate_fake_sqli_features()
        fake_source_ip = f"10.42.{random.randint(1, 254)}.{random.randint(1, 254)}"
        
        async with httpx.AsyncClient() as client:
            await client.post(
                f"{INTERNAL_API_BASE_URL}/api/predict",
                json={
                    "features": features,
                    "source_info": f"sqli_sim_{fake_source_ip}",
                    "simulation_id": simulation_id
                },
                timeout=10.0
            )
    except Exception as e:
        print(f"Error during SQLi prediction trigger: {e}")

async def run_sqlinjection_simulation(
    params: SQLInjectionParams,
    progress_callback: Callable[[Dict[str, Any]], Coroutine[Any, Any, None]],
    simulation_run_id: str
) -> Dict[str, Any]:
    print(f"Starting SQL Injection Simulation: Target={params.target_url}")
    vulnerable_findings: List[Dict[str, Any]] = []
     # Collect all payloads
    payloads_to_test = [p for cat in params.payload_categories for p in SQLI_PAYLOADS.get(cat, [])]
    total_payloads = len(payloads_to_test)
    
    if not total_payloads:
        await progress_callback({"type": "error", "message": "No SQLi payloads for selected categories."})
        return {}

    await progress_callback({"type": "progress", "message": f"Testing {total_payloads} payloads...", "completed": 0, "total": total_payloads})

    async def send_request(session, payload):
         # Construct the full payload
        full_payload = (params.base_value_for_param or "") + payload
        try:
            if params.method == HTTPMethod.GET:
                response = await session.get(str(params.target_url), params={params.param_to_inject: full_payload})
            else:
                post_data = params.other_post_data.copy() if params.other_post_data else {}
                post_data[params.param_to_inject] = full_payload
                response = await session.post(str(params.target_url), data=post_data)
            # Simulate AI detection
            asyncio.create_task(trigger_prediction(simulation_run_id))
            # Check if any of the error indicator texts are present in the response
            if any(indicator.lower() in response.text.lower() for indicator in params.error_indicator_texts):
                vulnerable_findings.append({"payload_used": payload})
                await progress_callback({"type": "progress", "message": f"VULNERABLE with: {payload}"})
        except Exception as e:
            print(f"Error during SQLi request with payload {payload}: {e}")
    # Run all payload tests
    async with httpx.AsyncClient(verify=False, timeout=20.0) as client:
        tasks = [send_request(client, payload) for payload in payloads_to_test]
        # Track progress
        for i, task in enumerate(asyncio.as_completed(tasks)):
            await task
            await progress_callback({"type": "progress", "message": f"Payload {i+1}/{total_payloads}", "completed": i + 1, "total": total_payloads})
    # Prepare the final result
    result = {"target_url": str(params.target_url), "total_payloads_tested": total_payloads, "vulnerable_payloads": vulnerable_findings}
    await progress_callback({"type": "final_summary", "message": "💉 SQLi simulation completed."})
    return result