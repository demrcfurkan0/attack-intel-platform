# attack-simulation/app/main.py

import os
import json
import joblib
import traceback
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from app.routes import router as api_router
from app.core.ws_manager import manager as ws_manager
from app.database import db_manager
from app.core import state
from app.core.event_handler import create_initial_admin_user, shutdown_event

app = FastAPI(
    title="AI-Driven Cyber Attack Simulation and Response Tool",
    description="Cyber attack simulation, AI-based detection, and reporting.",
    version="1.0.0"
)

# --- Startup Event ---
@app.on_event("startup")
async def startup_event():
    print("Uygulama başlatılıyor...")
    db_manager.connect()
    
    await create_initial_admin_user()

    print("Model dosyaları yükleniyor...")
    try:
        model_path = os.getenv("MODEL_PATH", "models/final_xgboost_model.pkl")
        scaler_path = os.getenv("SCALER_PATH", "models/final_scaler.pkl")
        features_path = os.getenv("FEATURE_COLUMNS_PATH", "models/feature_columns.json")

        with open(model_path, "rb") as f:
            state.model = joblib.load(f)
        with open(scaler_path, "rb") as f:
            state.scaler = joblib.load(f)

        with open(features_path, "r") as f:
            state.feature_columns = json.load(f)

        print("✅ AI Model, Scaler ve Özellik Sütunları başarıyla yüklendi.")
    except Exception as e:
        print(f"❌ AI Model yüklenirken hata: {e}")
        print(traceback.format_exc())

    print("Uygulama başlatma işlemleri tamamlandı.")

# --- Shutdown Event ---
app.add_event_handler("shutdown", shutdown_event)

# --- CORS ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # frontend'ten gelen her şeyi kabul eder
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Router ---
app.include_router(api_router)

# --- WebSocket ---
@app.websocket("/ws/simulation/{simulation_id}")
async def websocket_endpoint(websocket: WebSocket, simulation_id: str):
    await ws_manager.connect(websocket, simulation_id)
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        ws_manager.disconnect(simulation_id)