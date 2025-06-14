from app.simulations.simulation_params import BruteForceParams
from app.services.simulation_handler import handle_simulation_and_log
from typing import Dict, Any, List, Callable, Coroutine
import httpx
import asyncio
import traceback
import os
from app.core import state
import random

INTERNAL_API_BASE_URL = os.getenv("INTERNAL_API_BASE_URL", "http://localhost:8000")

def generate_fake_brute_force_features():
    if not state.feature_columns:
        print("⚠️ Feature columns not loaded in state.")
        return {}
    features = {key: 0.0 for key in state.feature_columns}
    features.update({
        'Flow Duration': random.uniform(30_000, 100_000),
        'Fwd Packet Length Max': random.uniform(10, 80),
        'Flow IAT Mean': random.uniform(5_000, 40_000),
        'Packet Length Mean': random.uniform(10, 60),
        'Init_Win_bytes_forward': -1.0,
        'Init_Win_bytes_backward': -1.0
    })
    return features

async def trigger_prediction(simulation_id: str):
    try:
        features = generate_fake_brute_force_features()
        async with httpx.AsyncClient() as client:
            await client.post(
                f"{INTERNAL_API_BASE_URL}/api/predict",
                json={
                    "features": features,
                    "source_info": f"bruteforce_simulation_run_{simulation_id}"
                },
                timeout=10.0
            )
    except Exception as e:
        print(f"❌ Error during brute-force prediction trigger: {e}")

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

    await progress_callback({
        "type": "progress", "message": "Starting brute force attack...", 
        "completed": 0, "total": total_possible_attempts
    })

    async def try_single_login(session: httpx.AsyncClient, username: str, password: str) -> bool:
        nonlocal total_attempts_made
        login_payload = {params.username_field: username, params.password_field: password}
        try:
            response = await session.post(str(params.target_url), data=login_payload, timeout=15.0, follow_redirects=True)
            success = False
            response_text_lower = response.text.lower()

            if params.success_status_code and response.status_code == params.success_status_code:
                success = True
            if not success and params.success_text_indicator and params.success_text_indicator.lower() in response_text_lower:
                success = True

            if success:
                credentials_found.append({"username": username, "password": password})
                await progress_callback({ "type": "progress", "message": f"✅ SUCCESS! Found credentials for {username}!" })
                # AI'ı her başarılı girişte tetikle
                asyncio.create_task(trigger_prediction(simulation_run_id))
                return True

        except httpx.RequestError as e:
            print(f"Brute force request error for {username}: {e}")
        except Exception as e:
            print(f"Unexpected error in try_single_login for {username}: {e}")
            print(traceback.format_exc())
        finally:
            total_attempts_made += 1
            # Her 5 denemede bir ilerleme ve AI tetikleme
            if total_attempts_made % 5 == 0 or total_attempts_made == total_possible_attempts:
                await progress_callback({
                    "type": "progress", 
                    "message": f"Attempt {total_attempts_made}/{total_possible_attempts}...",
                    "completed": total_attempts_made, 
                    "total": total_possible_attempts
                })
                asyncio.create_task(trigger_prediction(simulation_run_id))  # Periyodik olarak tetikle
        return False

    semaphore = asyncio.Semaphore(params.concurrency)

    async def worker(session: httpx.AsyncClient, username: str, password: str) -> bool:
        async with semaphore:
            return await try_single_login(session, username, password)

    async with httpx.AsyncClient(verify=False) as client:
        for username in params.usernames:
            if simulation_halted: break
            password_tasks = [worker(client, username, password) for password in params.passwords]
            results = await asyncio.gather(*password_tasks, return_exceptions=True)

            for res in results:
                if isinstance(res, Exception):
                    print(f"A worker failed with an exception: {res}")

            successful_logins = [res for res in results if isinstance(res, bool) and res]
            if successful_logins and params.stop_on_first_success:
                simulation_halted = True
                break

    result = {
        "target_url": str(params.target_url),
        "username_field": params.username_field,
        "password_field": params.password_field,
        "total_attempts_made": total_attempts_made,
        "credentials_found": credentials_found,
        "simulation_halted_early": simulation_halted
    }

    await progress_callback({"type": "final_summary", "message": "🔒 Brute-force simulation completed."})
    return result