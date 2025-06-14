# attack-simulation/app/simulations/ddos_simulation.py

from app.simulations.simulation_params import DDoSParams
from typing import List, Dict, Any, Callable, Coroutine
import httpx
import asyncio
import random
import time
import os
from app.core import state
from app.services.simulation_handler import handle_simulation_and_log


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
    """
    # Önce tüm özellikleri 0.0 ile başlat
    if not state.feature_columns:
        # Eğer özellik listesi yüklenemediyse boş bir dict döndür, bu bir hata durumudur.
        print("⚠️ Feature columns not loaded in state. Cannot generate fake features.")
        return {}

    # state'den gelen tam özellik listesini kullanarak bir sözlük oluştur
    features = {key: 0.0 for key in state.feature_columns}
    
    # Şimdi sadece bildiğimiz ve önemli olan özellikleri anormal değerlerle üzerine yazalım
    # Eğer bir özellik adı yanlış yazılmışsa, bu yapı sayesinde hata vermez, sadece üzerine yazılmaz.
    features.update({
        'Flow Duration': random.uniform(50_000, 200_000),
        'Total Fwd Packets': random.uniform(2, 6),
        'Total Backward Packets': random.uniform(0, 4),
        'Fwd Packet Length Max': random.uniform(0, 100),
        'Flow IAT Mean': random.uniform(10_000, 80_000),
        'Flow IAT Min': random.uniform(1, 100),
        'Packet Length Mean': random.uniform(0, 50),
        'Average Packet Size': random.uniform(0, 60),
        'Init_Win_bytes_forward': -1.0,
        'Init_Win_bytes_backward': -1.0
    })

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
            print(f"[TRIGGER] Sending fake features to prediction endpoint for sim_id: {simulation_run_id}")
            
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