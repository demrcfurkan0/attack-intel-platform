from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel # PredictionInput/Output için temel
from typing import List, Dict, Any, Optional # Tipler için
from datetime import datetime, timezone
import traceback
from bson import ObjectId
import joblib # AI Modeli yüklemek için
import json   # feature_columns.json yüklemek için
import numpy as np # AI Modeli için numpy gerekebilir
import os
print(f"Uygulamanın çalıştığı dizin: {os.getcwd()}")

# Yerel modüllerden importlar
from database import db_manager, log_to_db # database.py'dan import et
from simulations import (
    DDoSParams,
    BruteForceParams,
    SQLInjectionParams,
    HTTPMethod, # Enum'ı da import edelim (kullanılmasa bile referans olabilir)
    run_ddos_simulation,
    run_bruteforce_simulation,
    run_sqlinjection_simulation
)

# --- AI Modeli ve Etiket Ayarları ---
# Lütfen bu yolları kendi projenize göre güncelleyin!
MODEL_PATH = "models/final_xgboost_model.pkl"
SCALER_PATH = "models/final_scaler.pkl"
FEATURE_COLUMNS_PATH = "models/feature_columns.json"

model = None
scaler = None
feature_columns = None

# Etiketleri insan tarafından okunabilir hale getirmek için bir harita
# Colab'daki encode_label fonksiyonunuza göre güncelleyin
LABEL_MAP = {
    0: "BENIGN",
    1: "DoS/DDoS",
    2: "BruteForce",
    3: "SQL_Injection"
}

# --- Pydantic Modelleri (AI Tahmini için) ---
# Bu modelleri daha önce tanımlamıştınız, buraya ekliyorum.
# Özellik sayısı dinamik olduğu için Dict kullanmıştık.
class PredictionInput(BaseModel):
    features: Dict[str, float]

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
    # Veritabanı bağlantısını başlat
    db_manager.connect()

    # AI Modelini yükle
    global model, scaler, feature_columns
    try:
        model = joblib.load(MODEL_PATH)
        scaler = joblib.load(SCALER_PATH)
        with open(FEATURE_COLUMNS_PATH, 'r') as f:
            feature_columns = json.load(f)
        print("✅ AI Model, Scaler ve Özellik Sütunları başarıyla yüklendi.")
        print(f"Modelin beklediği özellik sayısı: {len(feature_columns)}")
    except FileNotFoundError as e:
        print(f"❌ Hata: Model, scaler veya özellik dosyası bulunamadı: {e}")
        print("Tahmin endpoint'i düzgün çalışmayabilir.")
        # Burada uygulama durdurulabilir veya bir hata durumu yönetilebilir.
    except Exception as e:
        print(f"❌ AI Model, scaler veya özellikler yüklenirken bir hata oluştu: {e}")
        print(traceback.format_exc())
    print("Uygulama başlatma işlemleri tamamlandı.")

@app.on_event("shutdown")
async def shutdown_event():
    print("Uygulama kapatılıyor...")
    db_manager.close()
    print("Uygulama kapatıldı.")

# --- CORS Ayarları ---
# Frontend adresinizi buraya ekleyin (örn: http://localhost:3000)
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    # Gerekirse diğer origin'leri ekleyebilirsiniz
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # GET, POST, PUT, DELETE vb. tüm metodlara izin ver
    allow_headers=["*"], # Tüm başlıklara izin ver
)

# ---- API Endpoint'leri ----

@app.get("/", tags=["General"])
async def read_root():
    """API'nin kök endpoint'i, hoş geldiniz mesajı döndürür."""
    return {"message": "AI-Driven Cyber Attack Simulation API'ye hoş geldiniz!"}

# --- AI Modeli Endpoint'i ---
@app.post("/api/predict", response_model=PredictionOutput, tags=["AI Model"])
async def predict_attack_endpoint(data: PredictionInput):
    """
    Verilen özelliklere göre bir siber saldırı tahmini yapar ve sonucu loglar.
    """
    if model is None or scaler is None or feature_columns is None:
        print("⚠️ Tahmin isteği geldi ancak AI model/scaler/özellikler yüklenememiş.")
        raise HTTPException(status_code=503, detail="AI Model, scaler veya özellik listesi şu anda kullanılamıyor. Lütfen sunucu loglarını kontrol edin.")

    try:
        input_features_ordered = [data.features[col_name] for col_name in feature_columns]
    except KeyError as e:
        raise HTTPException(
            status_code=400,
            detail=f"Eksik özellik: '{e.args[0]}'. Lütfen beklenen tüm özellikleri ({len(feature_columns)} adet) gönderin."
        )
    
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
        prediction_probabilities = model.predict_proba(scaled_features)[0].tolist()
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
        "prediction_run_id": str(ObjectId()), # Tahmin için de bir ID
        "source_of_data": data.features.get("source_info", "manual_api_call"), # Opsiyonel: verinin kaynağı
        "input_features_snapshot": data.features,
        "model_details": {"model_name": MODEL_PATH.split('/')[-1] if MODEL_PATH else "N/A"},
        "prediction_result": prediction_output_dict,
        "is_attack": prediction_label != LABEL_MAP.get(0, "BENIGN") # BENIGN değilse saldırıdır
        # created_at otomatik eklenecek (log_to_db içinde)
    }
    await log_to_db("predictions_log", log_data, db_manager)

    return PredictionOutput(**prediction_output_dict)


# --- Simülasyon Endpoint'leri ---

async def handle_simulation_and_log(
    sim_type: str,
    params: Any, # DDoSParams, BruteForceParams, etc.
    simulation_function: callable,
    background_tasks: BackgroundTasks
):
    """Genel simülasyon ve loglama işleyicisi."""
    start_time = datetime.now(timezone.utc)
    simulation_run_id = str(ObjectId())

    async def simulation_task():
        try:
            print(f"{sim_type.upper()} simülasyonu ({simulation_run_id}) arka planda başlatılıyor...")
            sim_result_details = await simulation_function(params)
            end_time = datetime.now(timezone.utc)
            duration = (end_time - start_time).total_seconds()

            # Özet alanlarını simülasyon tipine göre ayıkla
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
                "target_details": {"url": str(params.target_url), "method": params.method.value if hasattr(params, 'method') else "N/A"},
                "parameters_used": params.dict(),
                "status": "completed",
                "start_time": start_time,
                "end_time": end_time,
                "duration_seconds": round(duration, 3),
                "summary": summary_data,
                "raw_result": sim_result_details
            }
            await log_to_db("simulations_log", log_data, db_manager)
            print(f"{sim_type.upper()} simülasyonu ({simulation_run_id}) tamamlandı ve loglandı.")
            # İsteğe bağlı: Simülasyon sonrası AI modelini tetikle
            # Veya bir bildirim gönder.

        except Exception as e:
            end_time = datetime.now(timezone.utc)
            duration = (end_time - start_time).total_seconds()
            print(f"❌ {sim_type.upper()} simülasyonu ({simulation_run_id}) sırasında hata: {e}")
            print(traceback.format_exc())
            log_data_error = {
                "simulation_id": simulation_run_id,
                "simulation_type": sim_type,
                "target_details": {"url": str(params.target_url), "method": params.method.value if hasattr(params, 'method') else "N/A"},
                "parameters_used": params.dict(),
                "status": "failed",
                "start_time": start_time,
                "end_time": end_time,
                "duration_seconds": round(duration, 3),
                "error_message": str(e),
                "error_traceback": traceback.format_exc() # Detaylı hata kaydı
            }
            await log_to_db("simulations_log", log_data_error, db_manager)

    background_tasks.add_task(simulation_task)
    return {
        "status": f"{sim_type.upper()} simulation started in background",
        "simulation_run_id": simulation_run_id,
        "params_received": params.dict()
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


# --- Raporlama Endpoint'leri (MongoDB'den Veri Çekmek İçin) ---
# Bunlar daha sonra eklenecek. Örnek:
@app.get("/api/reports/simulations", summary="Tamamlanmış Simülasyon Loglarını Getir", tags=["Reports"])
async def get_simulation_reports(limit: int = 20, skip: int = 0, sim_type: Optional[str] = None):
    """
    MongoDB'den simülasyon loglarını getirir.
    - `limit`: Döndürülecek maksimum kayıt sayısı.
    - `skip`: Atlanacak kayıt sayısı (sayfalama için).
    - `sim_type`: Filtrelemek için simülasyon tipi (ddos, brute_force, sql_injection).
    """
    db_conn = db_manager.get_db()
    if not db_conn:
        raise HTTPException(status_code=503, detail="Veritabanı bağlantısı mevcut değil.")
    
    query = {}
    if sim_type:
        query["simulation_type"] = sim_type.lower()
        
    try:
        # ObjectId'leri string'e çevirmek için bir yardımcı fonksiyon
        def serialize_doc(doc):
            if "_id" in doc and isinstance(doc["_id"], ObjectId):
                doc["_id"] = str(doc["_id"])
            if "start_time" in doc and isinstance(doc["start_time"], datetime):
                doc["start_time"] = doc["start_time"].isoformat()
            if "end_time" in doc and isinstance(doc["end_time"], datetime):
                doc["end_time"] = doc["end_time"].isoformat()
            if "created_at" in doc and isinstance(doc["created_at"], datetime):
                 doc["created_at"] = doc["created_at"].isoformat()
            return doc

        logs_cursor = db_conn.simulations_log.find(query).sort("start_time", -1).skip(skip).limit(limit)
        logs = [serialize_doc(doc) for doc in logs_cursor]
        
        total_count_query = db_conn.simulations_log.count_documents(query)
        
        return {"total_count": total_count_query, "data": logs}
    except Exception as e:
        print(f"❌ Raporları çekerken hata: {e}")
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail=f"Simülasyon raporları alınırken bir hata oluştu: {str(e)}")


# İsteğe bağlı: Uygulamayı doğrudan çalıştırmak için (geliştirme sırasında)
# if __name__ == "__main__":
#     import uvicorn
#     # AI model dosyalarının ve database.py, simulations.py'nin main.py ile aynı dizinde olduğundan emin olun.
#     uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)