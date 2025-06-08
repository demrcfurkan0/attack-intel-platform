from app.core import state
from app.core.config import Config
from app.models import PredictionInput, PredictionOutput
from fastapi import FastAPI, HTTPException, BackgroundTasks, APIRouter
import traceback
import numpy as np
from bson import ObjectId
from app.database.database import db_manager, log_to_db
from app.simulations import *
from datetime import datetime
from typing import List, Dict, Any, Optional
from app.services.simulation_handler import handle_simulation_and_log


router = APIRouter()

@router.get("/", tags=["General"])
async def read_root():
    return {"message": "AI-Driven Cyber Attack Simulation API'ye hoş geldiniz!"}

# --- AI Modeli Endpoint'i ---
@router.post("/api/predict", response_model=PredictionOutput, tags=["AI Model"])
async def predict_attack_endpoint(data: PredictionInput):
    if state.model is None or state.scaler is None or state.feature_columns is None:
        print("⚠️ Tahmin isteği geldi ancak AI model/scaler/özellikler yüklenememiş.")
        raise HTTPException(status_code=503, detail="AI Model, scaler veya özellik listesi şu anda kullanılamıyor.")

    try:
        input_features_ordered = [data.features[col_name] for col_name in state.feature_columns]
    except KeyError as e:
        raise HTTPException(
            status_code=400,
            detail=f"Eksik özellik: '{e.args[0]}'. Lütfen beklenen tüm özellikleri ({len(state.feature_columns)} adet) gönderin." 
        ) # feature_columns listesini hata mesajına eklemeyi şimdilik çıkardım, çok uzun olabilir.
    
    if len(input_features_ordered) != len(state.feature_columns):
        raise HTTPException(
            status_code=400,
            detail=f"Yanlış sayıda özellik gönderildi. Beklenen: {len(state.feature_columns)}, Alınan: {len(input_features_ordered)}"
        )

    input_array = np.array([input_features_ordered], dtype=float)

    try:
        scaled_features = state.scaler.transform(input_array)
        prediction_id_array = state.model.predict(scaled_features)
        prediction_id = int(prediction_id_array[0])
        
        try:
            prediction_probabilities = state.model.predict_proba(scaled_features)[0].tolist()
        except AttributeError:
            prediction_probabilities = None
        except Exception as proba_e:
            print(f"Olasılıklar alınırken hata: {proba_e}")
            prediction_probabilities = None

    except Exception as e:
        print(f"❌ Model tahmini sırasında hata: {e}")
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail=f"Model tahmini sırasında bir hata oluştu: {str(e)}")

    prediction_label = Config.LABEL_MAP.get(prediction_id, f"Bilinmeyen Etiket ({prediction_id})")

    prediction_output_dict = {
        "prediction_label": prediction_label,
        "prediction_id": prediction_id,
        "probabilities": prediction_probabilities,
        "processed_features_count": len(input_features_ordered)
    }

    log_data = {
        "prediction_run_id": str(ObjectId()),
        "source_of_data": data.source_info,
        "input_features_snapshot": data.features,
        "model_details": {"model_name": Config.MODEL_PATH.split('/')[-1] if Config.MODEL_PATH else "N/A"},
        "prediction_result": prediction_output_dict,
        "is_attack": prediction_label != Config.LABEL_MAP.get(0, "BENIGN")
    }
    await log_to_db("predictions_log", log_data, db_manager)

    return PredictionOutput(**prediction_output_dict)

@router.post("/api/simulate/ddos", summary="DDoS Simülasyonu Başlat", tags=["Simulations"])
async def simulate_ddos_endpoint(params: DDoSParams, background_tasks: BackgroundTasks):
    return await handle_simulation_and_log("ddos", params, run_ddos_simulation, background_tasks)

@router.post("/api/simulate/bruteforce", summary="Brute Force Simülasyonu Başlat", tags=["Simulations"])
async def simulate_bruteforce_endpoint(params: BruteForceParams, background_tasks: BackgroundTasks):
    return await handle_simulation_and_log("brute_force", params, run_bruteforce_simulation, background_tasks)

@router.post("/api/simulate/sqlinjection", summary="SQL Injection Simülasyonu Başlat", tags=["Simulations"])
async def simulate_sqlinjection_endpoint(params: SQLInjectionParams, background_tasks: BackgroundTasks):
    return await handle_simulation_and_log("sql_injection", params, run_sqlinjection_simulation, background_tasks)


# --- Raporlama Endpoint'leri ---
@router.get("/api/reports/simulations", summary="Tamamlanmış Simülasyon Loglarını Getir", tags=["Reports"])
async def get_simulation_reports(limit: int = 20, skip: int = 0, sim_type: Optional[str] = None):
    db_conn = db_manager.get_db()
    if db_conn is None: # Kontrol zaten doğru
        raise HTTPException(status_code=503, detail="Veritabanı bağlantısı mevcut değil.")
    
    query: Dict[str, Any] = {}
    if sim_type:
        query["simulation_type"] = sim_type.lower()
        
    try:
        def serialize_doc_for_response(doc):
            if "_id" in doc and isinstance(doc["_id"], ObjectId):
                doc["_id"] = str(doc["_id"])
            for key, value in doc.items():
                if isinstance(value, datetime):
                    doc[key] = value.isoformat()
            return doc

        logs_cursor = db_conn.simulations_log.find(query).sort("start_time", -1).skip(skip).limit(limit)
        logs = [serialize_doc_for_response(doc) for doc in logs_cursor]
        
        total_count_query = db_conn.simulations_log.count_documents(query)
        
        return {"total_count": total_count_query, "data": logs}
    except Exception as e:
        print(f" Raporları çekerken hata: {e}")
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail=f"Simülasyon raporları alınırken bir hata oluştu: {str(e)}")