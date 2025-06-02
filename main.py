from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, conlist # conlist: list of constrained items
from typing import List, Dict, Any # Any eklendi
import joblib
import numpy as np
import pandas as pd # Pandas eklendi
import json # json eklendi

# ---- Uygulama Başlangıcında Model, Scaler ve Özellikleri Yükle ----
MODEL_PATH = "models/final_xgboost_model.pkl"  
SCALER_PATH = "models/final_scaler.pkl"
FEATURE_COLUMNS_PATH = "models/feature_columns.json"

model = None
scaler = None
feature_columns = None 

try:
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    with open(FEATURE_COLUMNS_PATH, 'r') as f:
        feature_columns = json.load(f)
    print(" AI Model, Scaler ve Özellik Sütunları başarıyla yüklendi.")
    print(f"Modelin beklediği özellik sayısı: {len(feature_columns)}")
except FileNotFoundError as e:
    print(f" Hata: Model, scaler veya özellik dosyası bulunamadı: {e}")
    print("Tahmin endpoint'i düzgün çalışmayabilir.")
except Exception as e:
    print(f" Model, scaler veya özellikler yüklenirken bir hata oluştu: {e}")

# ---- Pydantic Modelleri (API Girdi/Çıktı Tanımları) ----


class PredictionInput(BaseModel):
    # features: conlist(float, min_items=len(feature_columns) if feature_columns else 1, max_items=len(feature_columns) if feature_columns else 100) -> hata verdi?
    features: Dict[str, float] 

# Tahmin sonucu için model
class PredictionOutput(BaseModel):
    prediction_label: str
    prediction_id: int
    probabilities: List[float] = None 
    processed_features_count: int

LABEL_MAP = {
    0: "BENIGN",
    1: "DoS/DDoS",
    2: "BruteForce",
    3: "SQL_Injection" # Colab
}

# ---- FastAPI Uygulaması ----
app = FastAPI(title="AI-Driven Cyber Attack Simulation API")

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

# ---- API Endpoints ----
@app.get("/")
async def read_root():
    return {"message": "AI-Driven Cyber Attack Simulation API'ye hoş geldiniz!"}

@app.post("/api/predict", response_model=PredictionOutput)
async def predict_attack(data: PredictionInput):
    if model is None or scaler is None or feature_columns is None:
        raise HTTPException(status_code=503, detail="AI Model, scaler veya özellik listesi yüklenemedi. Lütfen sunucu loglarını kontrol edin.")

    try:
        input_features_ordered = [data.features[col_name] for col_name in feature_columns]
    except KeyError as e:
        raise HTTPException(
            status_code=400,
            detail=f"Eksik özellik: '{e.args[0]}'. Lütfen beklenen tüm özellikleri ({len(feature_columns)} adet) gönderin: {feature_columns}"
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Özellikleri işlerken hata: {str(e)}")


    if len(input_features_ordered) != len(feature_columns):
        raise HTTPException(
            status_code=400,
            detail=f"Yanlış sayıda özellik gönderildi. Beklenen: {len(feature_columns)}, Alınan: {len(input_features_ordered)}"
        )

    # Numpy to array
    input_array = np.array([input_features_ordered], dtype=float) # Model 2D array 

    # 2. Özellikleri ölçeklendir (eğitilmiş scaler ile)
    try:
        scaled_features = scaler.transform(input_array)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Özellikleri ölçeklendirirken hata: {str(e)}")

    # 3. Prediction model
    try:
        prediction_id_array = model.predict(scaled_features)
        prediction_id = int(prediction_id_array[0]) 

        # XGBoost  predict_proba)
        prediction_probabilities = model.predict_proba(scaled_features)[0].tolist()

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Model tahmini sırasında hata: {str(e)}")

    prediction_label = LABEL_MAP.get(prediction_id, f"Bilinmeyen Etiket ({prediction_id})")

    return PredictionOutput(
        prediction_label=prediction_label,
        prediction_id=prediction_id,
        probabilities=prediction_probabilities,
        processed_features_count=len(input_features_ordered)
    )

# Simülasyon placeholder'ları (önceki gibi, bunları da doldurabilirsin)
@app.post("/api/simulate/ddos")
async def simulate_ddos(params: dict):
    print(f"DDoS simulation triggered with params: {params}")
    return {"status": "DDoS simulation started (placeholder)", "params": params}

@app.post("/api/simulate/bruteforce")
async def simulate_bruteforce(params: dict):
    print(f"Brute force simulation triggered with params: {params}")
    return {"status": "Brute force simulation started (placeholder)", "params": params}

#To run the app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)