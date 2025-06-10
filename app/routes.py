# attack-simulation/app/routes.py

from fastapi import APIRouter, BackgroundTasks, HTTPException
import traceback
import numpy as np
from bson import ObjectId
from typing import Optional, List, Dict, Any
from datetime import datetime

from app.core import state
from app.core.config import Config
from app.models import PredictionInput, PredictionOutput
from app.database import db_manager, log_to_db
from app.simulations import (
    DDoSParams,
    BruteForceParams,
    SQLInjectionParams,
    run_ddos_simulation,
    run_bruteforce_simulation,
    run_sqlinjection_simulation
)
from app.services.simulation_handler import handle_simulation_and_log

# Router'ı /api öneki ile oluşturuyoruz.
router = APIRouter(
    prefix="/api"
)

# --- Genel Endpoint ---
# Yolu: /api/
@router.get("/", tags=["General"])
async def read_root():
    return {"message": "AI-Driven Cyber Attack Simulation API'ye hoş geldiniz!"}

# --- AI Modeli Endpoint'i ---
# Yolu: /api/predict
@router.post("/predict", response_model=PredictionOutput, tags=["AI Model"])
async def predict_attack_endpoint(data: PredictionInput):
    if state.model is None or state.scaler is None or state.feature_columns is None:
        print("⚠️ Tahmin isteği geldi ancak AI model/scaler/özellikler yüklenememiş.")
        raise HTTPException(status_code=503, detail="AI Model, scaler veya özellik listesi şu anda kullanılamıyor.")

    try:
        # feature_columns listesindeki sıraya göre gelen veriyi sırala
        # Eğer bir özellik eksikse, hata vermek yerine 0.0 kullan
        input_features_ordered = [data.features.get(col_name, 0.0) for col_name in state.feature_columns]
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Özellikler işlenirken bir hata oluştu: {e}"
        )

    if len(input_features_ordered) != len(state.feature_columns):
        # Bu kontrol genellikle gereksizdir çünkü yukarıdaki list comprehension her zaman doğru uzunlukta bir liste oluşturur,
        # ancak bir güvenlik önlemi olarak kalabilir.
        raise HTTPException(
            status_code=400,
            detail=f"Yanlış sayıda özellik işlendi. Beklenen: {len(state.feature_columns)}, İşlenen: {len(input_features_ordered)}"
        )

    input_array = np.array([input_features_ordered], dtype=float)

    try:
        scaled_features = state.scaler.transform(input_array)
        prediction_id_array = state.model.predict(scaled_features)
        prediction_id = int(prediction_id_array[0])
        
        try:
            prediction_probabilities = state.model.predict_proba(scaled_features)[0].tolist()
        except AttributeError:
            prediction_probabilities = None # Bazı modellerde bu metot olmayabilir
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
    # log_to_db fonksiyonunun doğru parametre sırası: collection_name, data, db_instance
    await log_to_db("predictions_log", log_data, db_manager)

    return PredictionOutput(**prediction_output_dict)

# --- Simülasyon Endpoint'leri ---
# Yolu: /api/simulate/ddos
@router.post("/simulate/ddos", summary="DDoS Simülasyonu Başlat", tags=["Simulations"])
async def simulate_ddos_endpoint(params: DDoSParams, background_tasks: BackgroundTasks):
    return await handle_simulation_and_log("ddos", params, run_ddos_simulation, background_tasks)

# Yolu: /api/simulate/bruteforce
@router.post("/simulate/bruteforce", summary="Brute Force Simülasyonu Başlat", tags=["Simulations"])
async def simulate_bruteforce_endpoint(params: BruteForceParams, background_tasks: BackgroundTasks):
    return await handle_simulation_and_log("brute_force", params, run_bruteforce_simulation, background_tasks)

# Yolu: /api/simulate/sqlinjection
@router.post("/simulate/sqlinjection", summary="SQL Injection Simülasyonu Başlat", tags=["Simulations"])
async def simulate_sqlinjection_endpoint(params: SQLInjectionParams, background_tasks: BackgroundTasks):
    return await handle_simulation_and_log("sql_injection", params, run_sqlinjection_simulation, background_tasks)

# --- Raporlama Endpoint'leri ---
# Yolu: /api/reports/simulations
@router.get("/reports/simulations", summary="Tamamlanmış Simülasyon Loglarını Getir", tags=["Reports"])
async def get_simulation_reports(limit: int = 20, skip: int = 0, sim_type: Optional[str] = None):
    db_conn = db_manager.get_db()
    if db_conn is None:
        raise HTTPException(status_code=503, detail="Veritabanı bağlantısı mevcut değil.")
    
    query: Dict[str, Any] = {}
    if sim_type:
        query["simulation_type"] = sim_type.lower()
        
    try:
        def serialize_doc_for_response(doc: Dict[str, Any]) -> Dict[str, Any]:
            if "_id" in doc and isinstance(doc["_id"], ObjectId):
                doc["_id"] = str(doc["_id"])
            
            # ObjectId veya datetime içeren diğer alanları da burada dönüştürebilirsin
            # Örnek:
            if "start_time" in doc and isinstance(doc["start_time"], datetime):
                doc["start_time"] = doc["start_time"].isoformat()
            if "end_time" in doc and isinstance(doc["end_time"], datetime):
                doc["end_time"] = doc["end_time"].isoformat()

            return doc

        # --- DÜZELTME: Standart (senkron) Pymongo kullanımı ---
        # `await` ve `.to_list()` kaldırıldı, cursor üzerinde doğrudan döngü kuruluyor.
        logs_cursor = db_conn.simulations_log.find(query).sort("start_time", -1).skip(skip).limit(limit)
        logs = [serialize_doc_for_response(doc) for doc in logs_cursor]
        
        # `count_documents` senkron bir fonksiyondur, `await` gerekmez.
        total_count = db_conn.simulations_log.count_documents(query)
        
        return {"total_count": total_count, "data": logs}

    except Exception as e:
        print(f"Raporları çekerken hata: {e}")
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail=f"Simülasyon raporları alınırken bir hata oluştu: {str(e)}")