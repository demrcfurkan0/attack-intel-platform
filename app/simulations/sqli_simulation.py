from typing import Optional, List, Dict, Any
import httpx
import asyncio
from app.simulations.simulation_params import SQLInjectionParams
import time
from urllib.parse import urlencode 
from app.simulations.utils import SQLI_PAYLOADS, HTTPMethod


async def run_sqlinjection_simulation(params: SQLInjectionParams) -> Dict[str, Any]:
    print(f"Starting SQL Injection Simulation: Target={params.target_url}, Parameter={params.param_to_inject}")
    potentially_vulnerable_findings: List[Dict[str, Any]] = []
    total_payloads_tested = 0
    
    selected_payloads: List[str] = []
    for category in params.payload_categories:
        selected_payloads.extend(SQLI_PAYLOADS.get(category, []))
    
    if not selected_payloads:
        return {
            "message": "No SQLi payload found for the selected categories.",
            "target_url": str(params.target_url),
            "total_payloads_tested": 0,
            "potentially_vulnerable_findings": []
        }

    base_target_url_str = str(params.target_url)

    async with httpx.AsyncClient(verify=False, timeout=20.0) as client:
        for payload_fragment in selected_payloads:
            total_payloads_tested += 1
            full_payload_value = (params.base_value_for_param or "") + payload_fragment
            
            request_data_post: Optional[Dict[str, str]] = None
            final_url_for_request = base_target_url_str 

            if params.method == HTTPMethod.GET:
                target_url_obj = httpx.URL(base_target_url_str) 
                query_params_dict = dict(target_url_obj.params)
                query_params_dict[params.param_to_inject] = full_payload_value
                
                query_string = urlencode(query_params_dict)
                query_bytes = query_string.encode('utf-8') # <<< --- YENİ SATIR: String'i byte'a çevir ---
                
                final_url_for_request = str(target_url_obj.copy_with(query=query_bytes)) # <<< --- DEĞİŞİKLİK: query_bytes kullan ---
            else: # POST
                request_data_post = params.other_post_data.copy() if params.other_post_data else {}
                request_data_post[params.param_to_inject] = full_payload_value

            try:
                start_time_req = time.time()
                if params.method == HTTPMethod.GET:
                    response = await client.get(final_url_for_request)
                else: 
                    response = await client.post(final_url_for_request, data=request_data_post)
                end_time_req = time.time()
                response_time_seconds = end_time_req - start_time_req
                
                response_text_lower = response.text.lower()
                vulnerability_detected = False
                detection_reasons: List[str] = []

                for error_indicator in params.error_indicator_texts:
                    if error_indicator.lower() in response_text_lower:
                        vulnerability_detected = True
                        detection_reasons.append(f"Error indicator found: '{error_indicator}'")
                        break

                if "time_based" in params.payload_categories:
                    expected_sleep_duration = 0
                    if "sleep(" in payload_fragment.lower():
                        try:
                            sleep_val_str = payload_fragment.lower().split("sleep(")[1].split(")")[0].strip()
                            if sleep_val_str.isdigit():
                                expected_sleep_duration = int(sleep_val_str)
                        except IndexError:
                            pass 
                    
                    if expected_sleep_duration > 0 and response_time_seconds >= (expected_sleep_duration * 0.8 + 0.5):
                        vulnerability_detected = True
                        detection_reasons.append(f"Potential time-based detection: Response time {response_time_seconds:.2f}s with payload '{payload_fragment}' (expected ~{expected_sleep_duration}s)")

                if vulnerability_detected:
                    print(f"🎯 Potential SQL Injection Found! Payload: {payload_fragment}, Reasons: {detection_reasons}")
                    potentially_vulnerable_findings.append({
                        "payload_used": payload_fragment,
                        "full_value_sent": full_payload_value,
                        "response_status": response.status_code,
                        "response_time_seconds": round(response_time_seconds, 3),
                        "detection_reasons": detection_reasons
                    })

            except httpx.TimeoutException:
                 if "time_based" in params.payload_categories and "sleep" in payload_fragment.lower():
                    print(f"⏳ Potential Time-Based SQL Injection (Timeout)! Payload: {payload_fragment}")
                    timeout_value_for_log = 20.0 
                    potentially_vulnerable_findings.append({
                        "payload_used": payload_fragment,
                        "full_value_sent": full_payload_value,
                        "response_status": "Timeout",
                        "response_time_seconds": timeout_value_for_log, 
                        "detection_reasons": ["Request timed out, potential time-based SQLi"]
                    })
            except httpx.RequestError:
                pass
            except Exception:
                pass

    result = {
        "target_url": str(params.target_url),
        "parameter_tested": params.param_to_inject,
        "method_used": params.method.value,
        "total_payloads_tested": total_payloads_tested,
        "potentially_vulnerable_findings": potentially_vulnerable_findings
    }
    print(f"SQL Injection Simulation Completed: {result}")
    return result