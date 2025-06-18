import asyncio
import os
import traceback
from datetime import datetime, timezone
from typing import Any, Dict, Optional

from bson import ObjectId
from fastapi import HTTPException
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, OperationFailure

# Config import'unu doğrudan kullanmak yerine, MONGO_URI ve DATABASE_NAME'i
# başlangıçta okuyup sabit olarak kullanmak daha temizdir.
MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")


class Database:
    client: Optional[MongoClient] = None
    db: Optional[Any] = None

    def connect(self):
        """MongoDB'ye bağlanır ve başlangıç kontrollerini yapar."""
        if self.client and self.db:
            try:
                self.client.admin.command('ping')
                print("ℹ️ MongoDB bağlantısı zaten aktif ve geçerli.")
                return
            except (ConnectionFailure, OperationFailure):
                print("⚠️ Mevcut MongoDB bağlantısı kopmuş, yeniden bağlanılıyor...")
                self.client = None
                self.db = None
        
        try:
            print(f"MongoDB'ye bağlanılıyor: {MONGO_URI}...")
            self.client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
            self.client.admin.command('ping')
            self.db = self.client[DATABASE_NAME]
            print(f"✅ MongoDB'ye başarıyla bağlanıldı. Veritabanı: '{DATABASE_NAME}'")
            self._create_indexes()

        except ConnectionFailure as e:
            print(f"❌ MongoDB bağlantı hatası: {MONGO_URI}. Hata: {e}")
            self.client = None
            self.db = None
        except Exception as e:
            print(f"❌ MongoDB'ye bağlanırken veya başlangıç ayarları yapılırken beklenmedik bir hata oluştu: {e}")
            self.client = None
            self.db = None

    def close(self):
        """MongoDB bağlantısını kapatır."""
        if self.client:
            try:
                self.client.close()
                print("MongoDB bağlantısı kapatıldı.")
            except Exception as e:
                print(f"MongoDB bağlantısını kapatırken hata oluştu: {e}")
            finally:
                self.client = None
                self.db = None
        else:
            print("Kapatılacak aktif MongoDB bağlantısı yok.")

    def get_db(self):
            """
            Veritabanı nesnesini döndürür. 
            Bağlantı yoksa veya kopmuşsa yeniden bağlanmayı dener.
            """
            # DOĞRU KONTROL: 'is None' veya 'is not None' kullanılır.
            if self.client is None or self.db is None:
                print("⚠️ Veritabanı bağlantısı (self.client veya self.db) None. Yeniden bağlanmaya çalışılıyor...")
                self.connect()
            else: 
                try:
                    self.client.admin.command('ping') 
                except (ConnectionFailure, OperationFailure):
                    print("⚠️ Mevcut MongoDB bağlantısı kopmuş (ping başarısız). Yeniden bağlanmaya çalışılıyor...")
                    self.connect() 
            
            return self.db

    def _create_indexes(self):
        """Gerekli koleksiyonlar için index'leri oluşturur (eğer yoksa)."""
        if self.db is None:
            print("⚠️ Index oluşturma atlandı çünkü veritabanı nesnesi (self.db) None.")
            return
            
        try:
            print("MongoDB index'leri kontrol ediliyor/oluşturuluyor...")
            
            # simulations_log için index'ler
            self.db.simulations_log.create_index([("simulation_id", 1)], unique=True, background=True)
            self.db.simulations_log.create_index([("simulation_type", 1)], background=True)
            self.db.simulations_log.create_index([("start_time", -1)], background=True)

            # predictions_log için index'ler
            self.db.predictions_log.create_index([("created_at", -1)], background=True)
            self.db.predictions_log.create_index([("simulation_id", 1)], background=True, sparse=True)

            # --- YENİ INDEX'LER ---
            # blocked_ips için index'ler
            # Bu index, IP'lerin 1 saat (3600 saniye) sonra otomatik silinmesini sağlar.
            self.db.blocked_ips.create_index([("blocked_at", 1)], expireAfterSeconds=3600)
            self.db.blocked_ips.create_index([("ip_address", 1)], unique=True)
            # --- YENİ INDEX'LER SONU ---

            print("✅ MongoDB index'leri başarıyla kontrol edildi/oluşturuldu.")
            
        except OperationFailure as e:
            if "IndexOptionsConflict" in str(e) or "already exists with different options" in str(e):
                print(f"⚠️ MongoDB index oluşturulurken seçenek çakışması veya mevcut index ile uyuşmazlık: {e}")
            elif "NamespaceNotFound" in str(e):
                 print(f"ℹ️ MongoDB index oluşturulurken koleksiyon bulunamadı (ilk çalıştırmada normal): {e}")
            else:
                print(f"❌ MongoDB index oluşturulurken OperationFailure: {e}")
        except Exception as e:
            print(f"❌ MongoDB index oluşturulurken genel bir hata oluştu: {e}")


# --- Veritabanı İşlem ve Bağımlılık Fonksiyonları ---

async def log_to_db(collection_name: str, data: Dict[str, Any], db_instance: 'Database') -> Optional[ObjectId]:
    """Belirtilen koleksiyona veri ekler."""
    db_conn = db_instance.get_db()
    if db_conn is None:
        print(f"❌ Veritabanı bağlantısı yok. '{collection_name}' koleksiyonuna log yazılamadı.")
        return None
    try:
        if "created_at" not in data:
             data["created_at"] = datetime.now(timezone.utc)
        
        result = await asyncio.to_thread(db_conn[collection_name].insert_one, data)
        print(f"'{collection_name}' koleksiyonuna log eklendi, ID: {result.inserted_id}")
        return result.inserted_id
        
    except Exception as e:
        print(f"❌ MongoDB'ye log yazma hatası ({collection_name}): {e}")
        print(traceback.format_exc())
        return None


# Global bir veritabanı yöneticisi örneği oluşturuyoruz
db_manager = Database()


def get_db_dependency():
    """FastAPI'nin dependency injection sistemi için veritabanı bağlantısını sağlar."""
    db = db_manager.get_db()
    if db is None:
        raise HTTPException(status_code=503, detail="Database connection is not available.")
    return db