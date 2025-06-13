# attack-simulation/app/main.py

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from app.core.event_handler import startup_event, shutdown_event
from app.routes import router as api_router
from app.core.ws_manager import manager as ws_manager
from fastapi.security import OAuth2PasswordBearer


app = FastAPI(
    title="AI-Driven Cyber Attack Simulation and Response Tool",
    description="Cyber attack simulation, AI-based detection, and reporting.",
    version="1.0.0"
)

# Olayları ve Middleware'i ekle
app.add_event_handler("startup", startup_event)
app.add_event_handler("shutdown", shutdown_event)

origins = [
    "http://localhost:8080",  # 5173 ?
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # geçici olarak wildcard aç
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Tüm API rotalarını uygulamaya dahil et
app.include_router(api_router)

# WebSocket endpoint'i
@app.websocket("/ws/simulation/{simulation_id}")
async def websocket_endpoint(websocket: WebSocket, simulation_id: str):
    await ws_manager.connect(websocket, simulation_id)
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        ws_manager.disconnect(simulation_id)