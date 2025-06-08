from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, HttpUrl
from typing import List, Dict, Any, Optional
from datetime import datetime, timezone
import traceback
from bson import ObjectId
import joblib
import json
import numpy as np
import os
from enum import Enum # Enum'ı import etmeyi unutmuyoruz

# Yerel modüllerden importlar
from database import db_manager, log_to_db
from simulations import (
    DDoSParams,
    BruteForceParams,
    SQLInjectionParams,
    HTTPMethod,
    run_ddos_simulation,
    run_bruteforce_simulation,
    run_sqlinjection_simulation
)

# --- AI Modeli ve Etiket Ayarları ---
MODEL_PATH = "models/final_xgboost_model.pkl" # Model dosyalarınızın yolu 'models' klasörü altındaysa
SCALER_PATH = "models/final_scaler.pkl"
FEATURE_COLUMNS_PATH = "models/feature_columns.json"

model = None
scaler = None
feature_columns = None

LABEL_MAP = {
    0: "BENIGN",
    1: "DoS/DDoS",
    2: "BruteForce",
    3: "SQL_Injection"
}

# --- Pydantic Modelleri (AI Tahmini için) ---
class PredictionInput(BaseModel):
    features: Dict[str, float]
    source_info: Optional[str] = "manual_api_call"


class PredictionOutput(BaseModel):
    prediction_label: str
    prediction_id: int
    probabilities: Optional[List[float]] = None
    processed_features_count: int

# --- Uygulama Başlangıç ve Kapanış Olayları ---
app = FastAPI(
    title="AI-Driven Cyber Attack Simulation and Response Tool",
    description="Cyber attack simulation, AI-based detection, and reporting.",
    version="0.1.0"
)

@app.on_event("startup")
async def startup_event():
    print("Uygulama başlatılıyor...")
    db_manager.connect()

    global model, scaler, feature_columns
    # main.py'nin bulunduğu dizini al
    current_script_directory = os.path.dirname(os.path.abspath(__file__))
    
    # Model yollarını ana dizine göre birleştir
    actual_model_path = os.path.join(current_script_directory, MODEL_PATH)
    actual_scaler_path = os.path.join(current_script_directory, SCALER_PATH)
    actual_feature_columns_path = os.path.join(current_script_directory, FEATURE_COLUMNS_PATH)

    print(f"Model dosyaları aranıyor:\n  Model: {actual_model_path}\n  Scaler: {actual_scaler_path}\n  Features: {actual_feature_columns_path}")

    try:
        if not os.path.exists(actual_model_path):
            raise FileNotFoundError(f"Model dosyası bulunamadı: {actual_model_path}")
        if not os.path.exists(actual_scaler_path):
            raise FileNotFoundError(f"Scaler dosyası bulunamadı: {actual_scaler_path}")
        if not os.path.exists(actual_feature_columns_path):
            raise FileNotFoundError(f"Özellik sütunları dosyası bulunamadı: {actual_feature_columns_path}")

        model = joblib.load(actual_model_path)
        scaler = joblib.load(actual_scaler_path)
        with open(actual_feature_columns_path, 'r') as f:
            feature_columns = json.load(f)
        print("✅ AI Model, Scaler ve Özellik Sütunları başarıyla yüklendi.")
        if feature_columns:
             print(f"Modelin beklediği özellik sayısı: {len(feature_columns)}")
        else:
            print("⚠️ Özellik sütunları yüklenemedi veya boş.")

    except FileNotFoundError as e:
        print(f"❌ Hata: {e}")
        print("Tahmin endpoint'i düzgün çalışmayabilir.")
    except Exception as e:
        print(f"❌ AI Model, scaler veya özellikler yüklenirken beklenmedik bir hata oluştu: {e}")
        print(traceback.format_exc())
    
    print("Uygulama başlatma işlemleri tamamlandı.")

@app.on_event("shutdown")
async def shutdown_event():
    print("Uygulama kapatılıyor...")
    db_manager.close()
    print("Uygulama kapatıldı.")

# --- CORS Ayarları ---
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---- API Endpoint'leri ----

@app.get("/", tags=["General"])
async def read_root():
    return {"message": "AI-Driven Cyber Attack Simulation API'ye hoş geldiniz!"}

# --- AI Modeli Endpoint'i ---
@app.post("/api/predict", response_model=PredictionOutput, tags=["AI Model"])
async def predict_attack_endpoint(data: PredictionInput):
    if model is None or scaler is None or feature_columns is None:
        print("⚠️ Tahmin isteği geldi ancak AI model/scaler/özellikler yüklenememiş.")
        raise HTTPException(status_code=503, detail="AI Model, scaler veya özellik listesi şu anda kullanılamıyor.")

    try:
        input_features_ordered = [data.features[col_name] for col_name in feature_columns]
    except KeyError as e:
        raise HTTPException(
            status_code=400,
            detail=f"Eksik özellik: '{e.args[0]}'. Lütfen beklenen tüm özellikleri ({len(feature_columns)} adet) gönderin." 
        ) # feature_columns listesini hata mesajına eklemeyi şimdilik çıkardım, çok uzun olabilir.
    
    if len(input_features_ordered) != len(feature_columns):
        raise HTTPException(
            status_code=400,
            detail=f"Yanlış sayıda özellik gönderildi. Beklenen: {len(feature_columns)}, Alınan: {len(input_features_ordered)}"
        )

    input_array = np.array([input_features_ordered], dtype=float)

    try:
        scaled_features = scaler.transform(input_array)
        prediction_id_array = model.predict(scaled_features)
        prediction_id = int(prediction_id_array[0])
        
        try:
            prediction_probabilities = model.predict_proba(scaled_features)[0].tolist()
        except AttributeError:
            prediction_probabilities = None
        except Exception as proba_e:
            print(f"Olasılıklar alınırken hata: {proba_e}")
            prediction_probabilities = None

    except Exception as e:
        print(f"❌ Model tahmini sırasında hata: {e}")
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail=f"Model tahmini sırasında bir hata oluştu: {str(e)}")

    prediction_label = LABEL_MAP.get(prediction_id, f"Bilinmeyen Etiket ({prediction_id})")

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
        "model_details": {"model_name": MODEL_PATH.split('/')[-1] if MODEL_PATH else "N/A"},
        "prediction_result": prediction_output_dict,
        "is_attack": prediction_label != LABEL_MAP.get(0, "BENIGN")
    }
    await log_to_db("predictions_log", log_data, db_manager)

    return PredictionOutput(**prediction_output_dict)


# --- Simülasyon Endpoint'leri ---

def serialize_pydantic_for_mongo(pydantic_model_instance: BaseModel) -> dict:
    data_dict = pydantic_model_instance.dict(exclude_none=True) 
    
    serialized_dict = {}
    for key, value in data_dict.items():
        if isinstance(value, HttpUrl):
            serialized_dict[key] = str(value)
        elif isinstance(value, Enum):
            serialized_dict[key] = value.value
        elif isinstance(value, datetime):
            serialized_dict[key] = value.isoformat()
        # Diğer tipler için basit atama, eğer iç içe Pydantic modelleri veya karmaşık tipler varsa
        # bu fonksiyonun daha kapsamlı olması gerekebilir.
        else:
            serialized_dict[key] = value
    return serialized_dict


async def handle_simulation_and_log(
    sim_type: str,
    params: Any, 
    simulation_function: callable,
    background_tasks: BackgroundTasks
):
    start_time = datetime.now(timezone.utc)
    simulation_run_id = str(ObjectId())
    params_for_mongo = serialize_pydantic_for_mongo(params)
    
    target_url_str = str(getattr(params, 'target_url', 'N/A'))
    target_method_value = "N/A"
    if hasattr(params, 'method') and isinstance(params.method, Enum): # Enum kontrolü eklendi
        target_method_value = params.method.value

    async def simulation_task():
        try:
            print(f"{sim_type.upper()} simülasyonu ({simulation_run_id}) arka planda başlatılıyor...")
            sim_result_details = await simulation_function(params)
            end_time = datetime.now(timezone.utc)
            duration = (end_time - start_time).total_seconds()

            summary_data = {}
            if sim_type == "ddos":
                summary_data = {
                    "total_requests_attempted": sim_result_details.get("total_requests_attempted"),
                    "successful_requests": sim_result_details.get("successful_requests"),
                    "failed_requests": sim_result_details.get("failed_requests"),
                    "requests_per_second": sim_result_details.get("requests_per_second"),
                    "average_request_time_ms": sim_result_details.get("average_request_time_ms"),
                    "status_codes_distribution": sim_result_details.get("status_codes_distribution")
                }
            elif sim_type == "brute_force":
                summary_data = {
                    "total_attempts_made": sim_result_details.get("total_attempts_made"),
                    "credentials_found_count": len(sim_result_details.get("credentials_found", [])),
                    "simulation_halted_early": sim_result_details.get("simulation_halted_early")
                }
            elif sim_type == "sql_injection":
                summary_data = {
                    "total_payloads_tested": sim_result_details.get("total_payloads_tested"),
                    "potentially_vulnerable_findings_count": len(sim_result_details.get("potentially_vulnerable_findings", []))
                }
            
            log_data = {
                "simulation_id": simulation_run_id,
                "simulation_type": sim_type,
                "target_details": {"url": target_url_str, "method": target_method_value},
                "parameters_used": params_for_mongo,
                "status": "completed",
                "start_time": start_time,
                "end_time": end_time,
                "duration_seconds": round(duration, 3),
                "summary": summary_data,
                "raw_result": sim_result_details
            }
            await log_to_db("simulations_log", log_data, db_manager)
            print(f"{sim_type.upper()} simülasyonu ({simulation_run_id}) tamamlandı ve loglandı.")

        except Exception as e:
            end_time = datetime.now(timezone.utc)
            duration = (end_time - start_time).total_seconds()
            print(f"❌ {sim_type.upper()} simülasyonu ({simulation_run_id}) sırasında hata: {e}")
            print(traceback.format_exc())
            log_data_error = {
                "simulation_id": simulation_run_id,
                "simulation_type": sim_type,
                "target_details": {"url": target_url_str, "method": target_method_value},
                "parameters_used": params_for_mongo,
                "status": "failed",
                "start_time": start_time,
                "end_time": end_time,
                "duration_seconds": round(duration, 3),
                "error_message": str(e),
                "error_traceback": traceback.format_exc()
            }
            await log_to_db("simulations_log", log_data_error, db_manager)

    background_tasks.add_task(simulation_task)
    return {
        "status": f"{sim_type.upper()} simulation started in background",
        "simulation_run_id": simulation_run_id,
        "params_received": params_for_mongo
    }

@app.post("/api/simulate/ddos", summary="DDoS Simülasyonu Başlat", tags=["Simulations"])
async def simulate_ddos_endpoint(params: DDoSParams, background_tasks: BackgroundTasks):
    return await handle_simulation_and_log("ddos", params, run_ddos_simulation, background_tasks)

@app.post("/api/simulate/bruteforce", summary="Brute Force Simülasyonu Başlat", tags=["Simulations"])
async def simulate_bruteforce_endpoint(params: BruteForceParams, background_tasks: BackgroundTasks):
    return await handle_simulation_and_log("brute_force", params, run_bruteforce_simulation, background_tasks)

@app.post("/api/simulate/sqlinjection", summary="SQL Injection Simülasyonu Başlat", tags=["Simulations"])
async def simulate_sqlinjection_endpoint(params: SQLInjectionParams, background_tasks: BackgroundTasks):
    return await handle_simulation_and_log("sql_injection", params, run_sqlinjection_simulation, background_tasks)


# --- Raporlama Endpoint'leri ---
@app.get("/api/reports/simulations", summary="Tamamlanmış Simülasyon Loglarını Getir", tags=["Reports"])
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
        print(f"❌ Raporları çekerken hata: {e}")
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail=f"Simülasyon raporları alınırken bir hata oluştu: {str(e)}")

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)