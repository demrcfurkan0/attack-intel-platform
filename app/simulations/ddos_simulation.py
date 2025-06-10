# attack-simulation/app/simulations/ddos_simulation.py

from app.simulations.simulation_params import DDoSParams
from typing import List, Dict, Any, Callable, Coroutine
import httpx
import asyncio
import random
import time
import os

# --- YENİ BÖLÜM: AI MODELİNİ BESLEMEK İÇİN ---

# Kendi API'mizin adresini ortam değişkeninden almak en iyisidir.
# Docker içinde servisler arası iletişim için 'http://fastapi:8000' veya 'http://localhost:8000' kullanılabilir.
# docker-compose.yml dosyasındaki servis adınıza bağlıdır. Varsayılan olarak 'fastapi' konulabilir.
# Veya Docker ana makine portunu kullanmak daha güvenilir olabilir.
INTERNAL_API_BASE_URL = os.getenv("INTERNAL_API_BASE_URL", "http://localhost:8000")

def generate_fake_ddos_features():
    """
    DDoS saldırısını taklit eden ve modelin beklediği 78 özellik için
    anlamlı ama sahte veriler üreten bir yardımcı fonksiyon.
    Değerler, DDoS trafiğinin tipik özelliklerine göre ayarlanmalıdır.
    """
    # Bu özellik adları ve sıraları, 'feature_columns.json' dosyanızdaki ile eşleşmelidir.
    # Örnek olarak birkaç önemli özellik:
    features = {
        'Flow Duration': random.uniform(1_000_000, 50_000_000),  # Uzun süren akışlar
        'Total Fwd Packets': random.uniform(5, 50),
        'Total Backward Packets': random.uniform(5, 50),
        'Fwd Packet Length Max': random.uniform(0, 500), # Genellikle küçük paketler
        'Fwd Packet Length Min': random.uniform(0, 10),
        'Fwd Packet Length Mean': random.uniform(5, 100),
        'Flow IAT Mean': random.uniform(100, 10000), # Paketler arası süre düşük
        'Flow IAT Max': random.uniform(50000, 500000),
        'Min Packet Length': random.uniform(0, 10),
        'Max Packet Length': random.uniform(0, 500),
        'Packet Length Mean': random.uniform(5, 100),
        'FIN Flag Count': 0, # Genellikle FIN bayrağı olmaz
        'SYN Flag Count': 1, # SYN bayrağı olur
        'PSH Flag Count': random.randint(0, 1),
        'ACK Flag Count': random.randint(0, 1),
        'URG Flag Count': 0,
        'Down/Up Ratio': random.uniform(0.5, 1.5),
        'Average Packet Size': random.uniform(5, 100),
        'Avg Fwd Segment Size': random.uniform(5, 100),
        'Init_Win_bytes_forward': random.randint(8192, 65535),
        'Init_Win_bytes_backward': random.randint(200, 65535),
        'Active Mean': random.uniform(100, 1000),
        'Idle Mean': random.uniform(1_000_000, 10_000_000),
    }

    # Modelin beklediği 78 özelliği tamamlamak için geri kalanları rastgele doldur
    # Önemli: Gerçek bir sistemde, tüm özellikler anlamlı olmalıdır.
    # Bu kısım sadece bir yer tutucudur.
    current_feature_count = len(features)
    for i in range(current_feature_count, 78):
        # Var olmayan özellik adları için genel bir adlandırma kullanalım
        # VEYA feature_columns.json dosyasından tam listeyi alıp burada kullanmak en doğrusudur.
        # Şimdilik yer tutucu olarak ekliyoruz.
        features[f'placeholder_feature_{i}'] = random.random()

    return features

async def trigger_prediction(simulation_id: str):
    """
    Sahte trafik verisi üretir ve bunu AI modelinin tahmin endpoint'ine gönderir.
    """
    try:
        features = generate_fake_ddos_features()
        
        # Backend'in kendi kendine istek atması için yeni bir client oluştur
        async with httpx.AsyncClient() as internal_client:
            predict_url = f"{INTERNAL_API_BASE_URL}/api/predict"
            await internal_client.post(
                predict_url, 
                json={
                    "features": features, 
                    "source_info": f"ddos_simulation_run_{simulation_id}"
                },
                timeout=10.0
            )
        # print(f"Prediction triggered for sim_id: {simulation_id}")
    except Exception as e:
        print(f"❌ Error during internal prediction call: {e}")

# --- ESKİ KODUN GÜNCELLENMİŞ HALİ ---

async def run_ddos_simulation(
    params: DDoSParams, 
    progress_callback: Callable[[Dict[str, Any]], Coroutine[Any, Any, None]],
    simulation_run_id: str # Hangi simülasyona ait olduğunu bilmek için ID'yi de alalım
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
            if params.method.value == "POST":
                response = await session.post(str(params.target_url), json=params.payload, headers=params.headers, timeout=params.timeout_seconds)
            else:
                response = await session.get(str(params.target_url), headers=params.headers, timeout=params.timeout_seconds)
            
            request_times.append(time.time() - start_req_time)
            status_code_str = str(response.status_code)
            status_codes_distribution[status_code_str] = status_codes_distribution.get(status_code_str, 0) + 1
            
            if 200 <= response.status_code < 400: successful_requests += 1
            else: failed_requests += 1

        except (httpx.TimeoutException, httpx.RequestError):
            failed_requests += 1
        finally:
            total_requests_made += 1
            
            # --- YENİ: Her istekten sonra hem ilerlemeyi bildir hem de AI tahminini tetikle ---
            # 1. AI Tahminini tetikle (bunu beklemeden devam etmesi için bir görev olarak başlatabiliriz)
            asyncio.create_task(trigger_prediction(simulation_run_id))
            
            # 2. WebSocket'e ilerleme bildir (her 50 istekte bir)
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

    async with httpx.AsyncClient(verify=False) as client:
        tasks = [worker(client, i) for i in range(params.num_requests)]
        await asyncio.gather(*tasks)

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
    
    await progress_callback({"type": "final_summary", "message": "DDoS simulation completed."})
    return result