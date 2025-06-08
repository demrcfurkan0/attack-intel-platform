# database.py

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, OperationFailure # OperationFailure eklendi
from datetime import datetime, timezone
import traceback
from typing import Optional, Dict, Any
from bson import ObjectId

# --- MongoDB Ayarları ---
# Bu ayarları ortam değişkenlerinden (environment variables) almak daha güvenli ve esnektir.
MONGO_URI = "mongodb://localhost:27017/"  # Yerel MongoDB adresiniz veya Docker'daki adres
DATABASE_NAME = "cyber_attack_sim_db"

class Database:
    client: Optional[MongoClient] = None
    db = None # Bu PyMongo'nun Database nesnesi olacak

    def connect(self):
        """MongoDB'ye bağlanır ve başlangıç kontrollerini yapar."""
        if self.client is not None and self.db is not None:
            # Zaten bağlıysa tekrar bağlanmaya çalışma
            try:
                # Hafif bir komutla bağlantının hala canlı olup olmadığını kontrol et
                self.client.admin.command('ping')
                print("MongoDB bağlantısı zaten aktif ve geçerli.")
                return
            except (ConnectionFailure, OperationFailure):
                print("Mevcut MongoDB bağlantısı kopmuş, yeniden bağlanılıyor...")
                self.client = None
                self.db = None
        
        try:
            print(f"MongoDB'ye bağlanılıyor: {MONGO_URI}...")
            self.client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000) # Bağlantı için zaman aşımı
            # Bağlantıyı test etmek için bir komut gönder (önerilir)
            self.client.admin.command('ping')
            self.db = self.client[DATABASE_NAME]
            print(f"✅ MongoDB'ye başarıyla bağlanıldı. Veritabanı: {DATABASE_NAME}")
            
            # self.db atandıktan sonra ve None olmadığı kontrol edilerek index'leri oluşturmayı dene
            if self.db is not None:
                self._create_indexes()
            else:
                # Bu durumun olmaması lazım eğer yukarıdaki atama başarılıysa.
                print("⚠️ Index oluşturma atlandı çünkü veritabanı nesnesi (self.db) None olarak kaldı (beklenmedik durum).")

        except ConnectionFailure as e:
            print(f"❌ MongoDB bağlantı hatası: {MONGO_URI}. Hata: {e}")
            self.client = None
            self.db = None
        except Exception as e:
            print(f"❌ MongoDB'ye bağlanırken veya başlangıç ayarları yapılırken beklenmedik bir hata oluştu: {e}")
            # Hatanın detayını görmek için bunu açabilirsiniz
            # print(traceback.format_exc())
            self.client = None
            self.db = None

    def close(self):
        """MongoDB bağlantısını kapatır."""
        if self.client is not None:
            try:
                self.client.close()
                print("MongoDB bağlantısı kapatıldı.")
            except Exception as e:
                print(f"MongoDB bağlantısını kapatırken hata oluştu: {e}")
            finally: # Her durumda client ve db'yi None yap
                self.client = None
                self.db = None
        else:
            print("Kapatılacak aktif MongoDB bağlantısı yok.")


    def get_db(self):
        """
        Veritabanı nesnesini döndürür. 
        Bağlantı yoksa veya kopmuşsa yeniden bağlanmayı dener.
        """
        if self.db is None or self.client is None:
            print("⚠️ Veritabanı bağlantısı (self.db veya self.client) None. Yeniden bağlanmaya çalışılıyor...")
            self.connect()
        else: # Bağlantı var gibi görünüyor, canlılığını test edelim
            try:
                self.client.admin.command('ping') # Hafif bir kontrol
            except (ConnectionFailure, OperationFailure):
                print("⚠️ Mevcut MongoDB bağlantısı kopmuş (ping başarısız). Yeniden bağlanmaya çalışılıyor...")
                self.connect() # Bağlantı kopmuşsa yeniden bağlan
        
        return self.db # Eğer connect başarılı olursa self.db set edilmiş olacak, değilse None dönecek

    def _create_indexes(self):
        """
        Gerekli koleksiyonlar için index'leri oluşturur (eğer yoksa).
        Performans için önemlidir.
        Bu metod sadece self.db None değilse çağrılmalı.
        """
        if self.db is None:
            print("⚠️ Index oluşturma atlandı çünkü veritabanı nesnesi (self.db) None.")
            return
            
        try:
            print("MongoDB index'leri kontrol ediliyor/oluşturuluyor...")
            # simulations_log için index'ler
            self.db.simulations_log.create_index([("simulation_id", 1)], unique=True, sparse=True, background=True)
            self.db.simulations_log.create_index([("simulation_type", 1)], background=True)
            self.db.simulations_log.create_index([("start_time", -1)], background=True)
            self.db.simulations_log.create_index([("status", 1)], background=True)

            # predictions_log için index'ler
            self.db.predictions_log.create_index([("created_at", -1)], background=True)
            self.db.predictions_log.create_index([("prediction_result.predicted_label", 1)], background=True)
            self.db.predictions_log.create_index([("is_attack", 1)], background=True)
            
            # alerts_log için index'ler (eğer kullanıyorsanız)
            # self.db.alerts_log.create_index([("created_at", -1)], background=True)
            # self.db.alerts_log.create_index([("alert_type", 1)], background=True)
            # self.db.alerts_log.create_index([("severity", 1)], background=True)
            print("✅ MongoDB index'leri başarıyla kontrol edildi/oluşturuldu.")
        except OperationFailure as e: # Index oluşturma sırasında spesifik hatalar
            if "IndexOptionsConflict" in str(e) or "already exists with different options" in str(e):
                print(f"⚠️ MongoDB index oluşturulurken seçenek çakışması veya mevcut index ile uyuşmazlık: {e}")
            elif "NamespaceNotFound" in str(e):
                 print(f"ℹ️ MongoDB index oluşturulurken koleksiyon bulunamadı (ilk çalıştırmada normal): {e}")
            else:
                print(f"❌ MongoDB index oluşturulurken OperationFailure: {e}")
                # print(traceback.format_exc())
        except Exception as e:
            print(f"❌ MongoDB index oluşturulurken genel bir hata oluştu: {e}")
            # print(traceback.format_exc())


# --- Veritabanı İşlem Fonksiyonları ---
async def log_to_db(collection_name: str, data: Dict[str, Any], db_instance: Database) -> Optional[ObjectId]:
    """
    Belirtilen koleksiyona veri ekler.
    db_instance: Global db_manager nesnesi.
    """
    # Her loglama denemesinde db bağlantısını almayı/test etmeyi dene
    db_conn = db_instance.get_db() 
    
    if db_conn is None:
        print(f"❌ Veritabanı bağlantısı yok (db_conn is None). Log yazılamadı: {collection_name}")
        return None
    try:
        if "created_at" not in data:
             data["created_at"] = datetime.now(timezone.utc)
        
        result = await asyncio.to_thread(db_conn[collection_name].insert_one, data)
        # Pymongo'nun bazı operasyonları bloklayıcı olabilir, to_thread ile async hale getirmek iyi bir pratiktir
        # Ancak insert_one genellikle hızlıdır. Duruma göre karar verilebilir.
        # Basitlik için direkt: result = db_conn[collection_name].insert_one(data) de kullanılabilir.
        
        print(f"'{collection_name}' koleksiyonuna log eklendi, ID: {result.inserted_id}")
        return result.inserted_id
    except Exception as e:
        print(f"❌ MongoDB'ye log yazma hatası ({collection_name}): {e}")
        print(traceback.format_exc())
        return None

# Global bir veritabanı yöneticisi örneği oluşturuyoruz
# Bu, FastAPI uygulamasının farklı yerlerinden aynı veritabanı bağlantısını kullanabilmesini sağlar.
db_manager = Database()