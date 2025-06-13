import os, json, joblib, traceback
from app.database.database import db_manager
from app.core.config import Config
from app.core import state 
# --- YENİ İMPORTLAR ---
from .security import get_password_hash
from dotenv import load_dotenv

# .env dosyasındaki değişkenleri okumak için
load_dotenv()
# --- YENİ İMPORTLAR SONU ---

async def create_initial_admin_user():
    """
    Veritabanını kontrol eder ve eğer hiç kullanıcı yoksa,
    .env dosyasından alınan bilgilerle varsayılan bir admin kullanıcısı oluşturur.
    """
    print("İlk admin kullanıcısı kontrol ediliyor...")
    db_conn = db_manager.get_db()
    if db_conn is None:
        print("❌ Veritabanı bağlantısı yok, admin kullanıcısı oluşturulamadı.")
        return

    # 'users' koleksiyonunda herhangi bir kullanıcı var mı diye bak
    if db_conn.users.count_documents({}) == 0:
        print("ℹ️ Hiç kullanıcı bulunamadı. Varsayılan admin oluşturuluyor...")
        
        # Admin bilgilerini .env dosyasından al (daha güvenli)
        admin_username = os.getenv("ADMIN_USERNAME", "admin")
        admin_email = os.getenv("ADMIN_EMAIL", "admin@example.com")
        admin_password = os.getenv("ADMIN_PASSWORD", "admin123")
        
        admin_user = {
            "username": admin_username,
            "email": admin_email,
            "password": get_password_hash(admin_password), # Şifreyi hash'le
            "role": "Administrator",
            "status": "active"
        }
        
        try:
            db_conn.users.insert_one(admin_user)
            print(f"✅ Varsayılan admin kullanıcısı '{admin_username}' başarıyla oluşturuldu.")
            print(f"🔑 Şifre: {admin_password} (Lütfen ilk girişten sonra değiştirin)")
        except Exception as e:
            print(f"❌ Varsayılan admin kullanıcısı oluşturulurken hata: {e}")
    else:
        print("✅ Veritabanında zaten kullanıcı(lar) mevcut. Admin oluşturma atlandı.")


async def startup_event():
    print("Uygulama başlatılıyor...")
    db_manager.connect()
    
    # --- YENİ ADIM: Admin kullanıcısını kontrol et/oluştur ---
    await create_initial_admin_user()
    # --- YENİ ADIM SONU ---

    # --- Model Yükleme Kısmı (Aynı kalıyor) ---
    print("Model dosyaları yükleniyor...")
    try:
        # ... (mevcut model yükleme kodunuz) ...
        # ...
        print("✅ AI Model, Scaler ve Özellik Sütunları başarıyla yüklendi.")
    except Exception as e:
        print(f"❌ AI Model yüklenirken hata: {e}")

    print("Uygulama başlatma işlemleri tamamlandı.")

async def shutdown_event():
    print("Uygulama kapatılıyor...")
    db_manager.close()
    print("Uygulama kapatıldı.")