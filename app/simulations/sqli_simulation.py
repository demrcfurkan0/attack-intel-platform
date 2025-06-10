# attack-simulation/app/simulations/sqli_simulation.py

from typing import Dict, Any, List, Callable, Coroutine
import httpx
import asyncio
from app.simulations.simulation_params import SQLInjectionParams
import time
from app.simulations.utils import SQLI_PAYLOADS, HTTPMethod

async def run_sqlinjection_simulation(
    params: SQLInjectionParams,
    progress_callback: Callable[[Dict[str, Any]], Coroutine[Any, Any, None]]
) -> Dict[str, Any]:
    print(f"Starting SQL Injection Simulation: Target={params.target_url}, Parameter={params.param_to_inject}")
    potentially_vulnerable_findings: List[Dict[str, Any]] = []
    
    selected_payloads: List[str] = []
    for category in params.payload_categories:
        selected_payloads.extend(SQLI_PAYLOADS.get(category, []))
    
    total_payloads_to_test = len(selected_payloads)
    total_payloads_tested = 0
    
    if not selected_payloads:
        await progress_callback({"type": "error", "message": "No SQLi payload found for the selected categories."})
        return {"message": "No SQLi payload found...", "total_payloads_tested": 0, "potentially_vulnerable_findings": []}

    await progress_callback({
        "type": "progress", "message": f"Starting to test {total_payloads_to_test} payloads...",
        "completed": 0, "total": total_payloads_to_test
    })
    
    base_target_url_str = str(params.target_url)

    async with httpx.AsyncClient(verify=False, timeout=20.0) as client:
        for i, payload_fragment in enumerate(selected_payloads):
            total_payloads_tested += 1
            if (i + 1) % 5 == 0 or (i + 1) == total_payloads_to_test:
                await progress_callback({
                    "type": "progress", "message": f"Testing payload {i+1}/{total_payloads_to_test}...",
                    "completed": i + 1, "total": total_payloads_to_test
                })

            full_payload_value = (params.base_value_for_param or "") + payload_fragment
            
            try:
                start_time_req = time.time()
                response: httpx.Response

                # --- DÜZELTİLMİŞ İSTEK MANTIĞI ---
                if params.method == HTTPMethod.GET:
                    # httpx'in kendi 'params' argümanını kullanalım, bu daha güvenli.
                    request_params = {params.param_to_inject: full_payload_value}
                    response = await client.get(base_target_url_str, params=request_params)
                else: # POST
                    request_data_post = params.other_post_data.copy() if params.other_post_data else {}
                    request_data_post[params.param_to_inject] = full_payload_value
                    response = await client.post(base_target_url_str, data=request_data_post)
                # --- DÜZELTME SONU ---
                
                end_time_req = time.time()
                response_time_seconds = end_time_req - start_time_req
                
                response_text_lower = response.text.lower()
                vulnerability_detected = False
                detection_reasons: List[str] = []

                for error_indicator in params.error_indicator_texts:
                    if error_indicator.lower() in response_text_lower:
                        vulnerability_detected = True
                        detection_reasons.append(f"Error indicator found: '{error_indicator}'")
                        break # İlk hatayı bulunca döngüden çık

                # ... (time-based detection mantığı aynı) ...

                if vulnerability_detected:
                    await progress_callback({
                        "type": "progress", "message": f"POTENTIAL VULNERABILITY FOUND!",
                        "found": True, "payload": payload_fragment
                    })
                    potentially_vulnerable_findings.append({
                        "payload_used": payload_fragment,
                        "full_value_sent": full_payload_value,
                        "response_status": response.status_code,
                        "response_time_seconds": round(response_time_seconds, 3),
                        "detection_reasons": detection_reasons
                    })

            except httpx.TimeoutException:
                await progress_callback({ "type": "progress", "message": f"POTENTIAL TIME-BASED VULNERABILITY (Timeout)", "found": True, "payload": payload_fragment})
                potentially_vulnerable_findings.append({ "payload_used": payload_fragment, "response_status": "Timeout", "detection_reasons": ["Request timed out"] })
            except Exception as e:
                print(f"Error during SQLi request with payload '{payload_fragment}': {e}")
                # Bu hatayı da WebSocket'e gönderebiliriz ama şimdilik sadece loglayalım
                pass

    await progress_callback({"type": "final_summary", "message": "SQL Injection simulation completed."})

    result = {
        "target_url": str(params.target_url),
        "parameter_tested": params.param_to_inject,
        "method_used": params.method.value,
        "total_payloads_tested": total_payloads_tested,
        "potentially_vulnerable_findings": potentially_vulnerable_findings
    }
    return result