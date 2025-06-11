from typing import Dict, Any, List, Callable, Coroutine
import httpx
import asyncio
from app.simulations.simulation_params import SQLInjectionParams
import time
from app.simulations.utils import SQLI_PAYLOADS, HTTPMethod

async def run_sqlinjection_simulation(
    params: SQLInjectionParams,
    progress_callback: Callable[[Dict[str, Any]], Coroutine[Any, Any, None]],
    simulation_run_id: str # Eksik olan argüman
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
        "type": "progress", "message": f"Starting to test {total_payloads_to_test} payloads...",
        "completed": 0, "total": total_payloads_to_test
    })

    async with httpx.AsyncClient(verify=False, timeout=20.0) as client:
        for i, payload_fragment in enumerate(selected_payloads):
            if (i + 1) % 5 == 0 or (i + 1) == total_payloads_to_test:
                await progress_callback({
                    "type": "progress", "message": f"Testing payload {i+1}/{total_payloads_to_test}...",
                    "completed": i + 1, "total": total_payloads_to_test
                })
            
            full_payload_value = (params.base_value_for_param or "") + payload_fragment
            try:
                if params.method == HTTPMethod.GET:
                    response = await client.get(str(params.target_url), params={params.param_to_inject: full_payload_value})
                else: # POST
                    post_data = params.other_post_data.copy() if params.other_post_data else {}
                    post_data[params.param_to_inject] = full_payload_value
                    response = await client.post(str(params.target_url), data=post_data)
                
                if any(indicator.lower() in response.text.lower() for indicator in params.error_indicator_texts):
                    await progress_callback({"type": "progress", "message": f"VULNERABILITY FOUND with payload: {payload_fragment}"})
                    potentially_vulnerable_findings.append({"payload_used": payload_fragment})
            except Exception:
                pass
    
    result = { "total_payloads_tested": len(selected_payloads), "potentially_vulnerable_findings": potentially_vulnerable_findings }
    return result