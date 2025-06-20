import asyncio
import os
import traceback
from datetime import datetime, timezone
from typing import Any, Dict, Optional

from bson import ObjectId
from fastapi import HTTPException
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, OperationFailure

# Load MongoDB 
MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")


class Database:
    client: Optional[MongoClient] = None
    db: Optional[Any] = None

    def connect(self):
        # Avoid reconnecting if already connected.
        if self.client and self.db:
            try:
                # Check if the connection is still alive.
                self.client.admin.command('ping')
                print("MongoDB connection is already active and valid.")
                return
            except (ConnectionFailure, OperationFailure):
                print("Current MongoDB connection is lost, reconnecting...")
                self.client = None
                self.db = None
        
        try:
            print(f"Connecting to MongoDB: {MONGO_URI}...")
            self.client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
            self.client.admin.command('ping') # Verify connection
            self.db = self.client[DATABASE_NAME]
            print(f"Connected to MongoDB: '{DATABASE_NAME}'")
            self._create_indexes()

        except ConnectionFailure as e:
            print(f"MongoDB connection error: {MONGO_URI}. Error: {e}")
            self.client = None
            self.db = None
        except Exception as e:
            print(f"Error connecting to MongoDB: {MONGO_URI}. Error: {e}")
            self.client = None
            self.db = None

    def close(self):
        if self.client:
            try:
                self.client.close()
                print("MongoDB connection closed.")
            except Exception as e:
                print(f"Error closing MongoDB connection: {e}")
            finally:
                self.client = None
                self.db = None
        else:
            print("No active MongoDB connection to close.")

    def get_db(self):
            if self.client is None or self.db is None:
                print("Database connection (self.client or self.db) is None. Trying to reconnect...")
                self.connect()
            else: 
                try:
                    self.client.admin.command('ping') 
                except (ConnectionFailure, OperationFailure):
                    print("Current MongoDB connection is lost (ping failed). Trying to reconnect...")
                    self.connect() 
            
            return self.db

    def _create_indexes(self):
        if self.db is None:
            print("Index creation skipped because database object (self.db) is None.")
            return
            
        try:
            print("Checking/Creating MongoDB indexes...")
            
            self.db.simulations_log.create_index([("simulation_id", 1)], unique=True, background=True)
            self.db.simulations_log.create_index([("simulation_type", 1)], background=True)
            self.db.simulations_log.create_index([("start_time", -1)], background=True)

            self.db.predictions_log.create_index([("created_at", -1)], background=True)
            self.db.predictions_log.create_index([("simulation_id", 1)], background=True, sparse=True)
            # TTL 
            self.db.blocked_ips.create_index([("blocked_at", 1)], expireAfterSeconds=3600)
            self.db.blocked_ips.create_index([("ip_address", 1)], unique=True)

            print("MongoDB indexes checked/created successfully.")
            
        except OperationFailure as e:
            if "IndexOptionsConflict" in str(e) or "already exists with different options" in str(e):
                print(f"Error creating MongoDB index: {e}")
            elif "NamespaceNotFound" in str(e):
                 print(f"Collection not found while creating MongoDB index (normal on first run): {e}")
            else:
                print(f"Error creating MongoDB index: {e}")
        except Exception as e:
            print(f"Error creating MongoDB index: {e}")
            
async def log_to_db(collection_name: str, data: Dict[str, Any], db_instance: 'Database') -> Optional[ObjectId]:
    db_conn = db_instance.get_db()
    if db_conn is None:
        print(f"Database connection is not available. '{collection_name}' collection could not be logged.")
        return None
    try:
        if "created_at" not in data:
             data["created_at"] = datetime.now(timezone.utc)
             
        # Run the blocking DB operation in a separate thread.
        result = await asyncio.to_thread(db_conn[collection_name].insert_one, data)
        print(f"'{collection_name}' collection logged, ID: {result.inserted_id}")
        return result.inserted_id
        
    except Exception as e:
        print(f"Error logging to MongoDB: ({collection_name}): {e}")
        print(traceback.format_exc())
        return None

db_manager = Database()

def get_db_dependency():
    db = db_manager.get_db()
    if db is None:
        raise HTTPException(status_code=503, detail="Database connection is not available.")
    return db