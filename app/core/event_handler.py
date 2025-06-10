# attack-simulation/app/core/event_handler.py

import os, json, joblib, traceback
from app.database.database import db_manager
from app.core.config import Config
from app.core import state 

async def startup_event():
    print("Uygulama başlatılıyor...")
    db_manager.connect()

    # --- DEĞİŞİKLİK: Yolları doğrudan ve basit bir şekilde kullan ---
    # Dockerfile'da WORKDIR /app olarak ayarlandığı için,
    # Config'den gelen yollar zaten /app'e göre çözümlenecektir.
    actual_model_path = Config.MODEL_PATH
    actual_scaler_path = Config.SCALER_PATH
    actual_feature_columns_path = Config.FEATURE_COLUMNS_PATH
    # --- DEĞİŞİKLİK SONU ---

    print(f"Model dosyaları aranıyor:\n  Model: {actual_model_path}\n  Scaler: {actual_scaler_path}\n  Features: {actual_feature_columns_path}")

    try:
        # Dosyaların var olup olmadığını kontrol et
        if not os.path.exists(actual_model_path):
            raise FileNotFoundError(f"Model dosyası bulunamadı: {actual_model_path}")
        if not os.path.exists(actual_scaler_path):
            raise FileNotFoundError(f"Scaler dosyası bulunamadı: {actual_scaler_path}")
        if not os.path.exists(actual_feature_columns_path):
            raise FileNotFoundError(f"Özellik sütunları dosyası bulunamadı: {actual_feature_columns_path}")

        # Modelleri yükle
        state.model = joblib.load(actual_model_path)
        state.scaler = joblib.load(actual_scaler_path)
        with open(actual_feature_columns_path, 'r') as f:
            state.feature_columns = json.load(f) # 'state.feature_columns' olarak ata
        
        print("✅ AI Model, Scaler ve Özellik Sütunları başarıyla yüklendi.")
        if state.feature_columns:
             print(f"Modelin beklediği özellik sayısı: {len(state.feature_columns)}")
        else:
            print("⚠️ Özellik sütunları yüklenemedi veya boş.")

    except FileNotFoundError as e:
        print(f"❌ Hata: {e}")
        print("Tahmin endpoint'i düzgün çalışmayabilir.")
    except Exception as e:
        print(f"❌ AI Model, scaler veya özellikler yüklenirken beklenmedik bir hata oluştu: {e}")
        print(traceback.format_exc())
    
    print("Uygulama başlatma işlemleri tamamlandı.")

async def shutdown_event():
    print("Uygulama kapatılıyor...")
    db_manager.close()
    print("Uygulama kapatıldı.")