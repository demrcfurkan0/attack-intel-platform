from typing import Dict, Any, List, Callable, Coroutine
import httpx
import asyncio
from app.simulations.simulation_params import SQLInjectionParams
from app.services.simulation_handler import handle_simulation_and_log
import time
from app.simulations.utils import SQLI_PAYLOADS, HTTPMethod
from app.core import state
import random
import os

# AI prediction endpointi
INTERNAL_API_BASE_URL = os.getenv("INTERNAL_API_BASE_URL", "http://localhost:8000")

def generate_fake_sqli_features():
    if not state.feature_columns:
        print("⚠️ Feature columns not loaded in state.")
        return {}
    features = {key: 0.0 for key in state.feature_columns}
    features.update({
        'Flow Duration': random.uniform(10_000, 70_000),
        'Fwd Packet Length Max': random.uniform(40, 100),
        'Packet Length Mean': random.uniform(10, 60),
        'Flow IAT Mean': random.uniform(5_000, 50_000),
        'Init_Win_bytes_forward': -1.0,
        'Init_Win_bytes_backward': -1.0
    })
    return features

async def trigger_prediction(simulation_id: str):
    try:
        features = generate_fake_sqli_features()
        async with httpx.AsyncClient() as client:
            await client.post(
                f"{INTERNAL_API_BASE_URL}/api/predict",
                json={
                    "features": features,
                    "source_info": f"sqli_simulation_run_{simulation_id}"
                },
                timeout=10.0
            )
    except Exception as e:
        print(f"❌ Error during SQLi prediction trigger: {e}")

async def run_sqlinjection_simulation(
    params: SQLInjectionParams,
    progress_callback: Callable[[Dict[str, Any]], Coroutine[Any, Any, None]],
    simulation_run_id: str
) -> Dict[str, Any]:
    print(f"Starting SQL Injection Simulation: Target={params.target_url}")
    potentially_vulnerable_findings: List[Dict[str, Any]] = []
    
    selected_payloads: List[str] = []
    for category in params.payload_categories:
        selected_payloads.extend(SQLI_PAYLOADS.get(category, []))
    
    total_payloads_to_test = len(selected_payloads)
    if not selected_payloads:
        await progress_callback({"type": "error", "message": "No SQLi payloads for selected categories."})
        return {}

    await progress_callback({
        "type": "progress", "message": f"Testing {total_payloads_to_test} payloads...",
        "completed": 0, "total": total_payloads_to_test
    })

    async with httpx.AsyncClient(verify=False, timeout=20.0) as client:
        for i, payload_fragment in enumerate(selected_payloads):
            if (i + 1) % 5 == 0 or (i + 1) == total_payloads_to_test:
                await progress_callback({
                    "type": "progress", 
                    "message": f"Payload {i+1}/{total_payloads_to_test}",
                    "completed": i + 1, 
                    "total": total_payloads_to_test
                })
            
            full_payload_value = (params.base_value_for_param or "") + payload_fragment
            try:
                if params.method == HTTPMethod.GET:
                    response = await client.get(str(params.target_url), params={params.param_to_inject: full_payload_value})
                else:
                    post_data = params.other_post_data.copy() if params.other_post_data else {}
                    post_data[params.param_to_inject] = full_payload_value
                    response = await client.post(str(params.target_url), data=post_data)
                
                # Modeli her payload'dan sonra tetikle (opsiyonel olarak her 3 payload'da bir de yapabilirsin)
                asyncio.create_task(trigger_prediction(simulation_run_id))

                if any(indicator.lower() in response.text.lower() for indicator in params.error_indicator_texts):
                    await progress_callback({"type": "progress", "message": f"VULNERABLE with: {payload_fragment}"})
                    potentially_vulnerable_findings.append({"payload_used": payload_fragment})
            except Exception:
                pass

    result = {
        "target_url": str(params.target_url),
        "method": params.method.value,
        "param_to_inject": params.param_to_inject,
        "base_value_for_param": params.base_value_for_param,
        "total_payloads_tested": total_payloads_to_test,
        "payload_categories": params.payload_categories,
        "vulnerable_payloads": potentially_vulnerable_findings
    }

    await progress_callback({"type": "final_summary", "message": "SQLi simulation completed."})
    return result