from fastapi import APIRouter, BackgroundTasks, HTTPException, Body, Depends
from fastapi.concurrency import run_in_threadpool
from fastapi.security import OAuth2PasswordRequestForm
import numpy as np
from bson import ObjectId
from typing import Optional, List, Dict, Any
from datetime import datetime, timedelta

from app.core.security import get_password_hash, verify_password, create_access_token

from app.core import state
from app.core.config import Config
from app.models import *
from app.database import db_manager, log_to_db
from app.simulations import *
from app.services.simulation_handler import handle_simulation_and_log

router = APIRouter(prefix="/api")

# --- YARDIMCI FONKSİYON ---
def serialize_mongo_doc(doc):
    if not doc: return None
    if '_id' in doc:
        doc['id'] = str(doc['_id'])
        del doc['_id'] # Pydantic modelinde _id olmadığı için bunu silmek önemli
    for key, value in doc.items():
        if isinstance(value, datetime):
            doc[key] = value.isoformat()
    return doc

# --- ENDPOINT'LER ---

@router.get("/", tags=["General"])
async def read_root():
    return {"message": "API is running!"}

@router.post("/predict", response_model=PredictionOutput, tags=["AI Model"])
async def predict_attack_endpoint(data: PredictionInput):
    # Bu endpoint'in doğru çalıştığını varsayıyoruz
    if state.model is None: raise HTTPException(503, "Model not available")
    features_ordered = [data.features.get(col, 0.0) for col in state.feature_columns]
    input_array = np.array([features_ordered], dtype=float)
    scaled_features = state.scaler.transform(input_array)
    prediction_id = int(state.model.predict(scaled_features)[0])
    probabilities = getattr(state.model, 'predict_proba', lambda _: [[]])(scaled_features)[0].tolist() or None
    label = Config.LABEL_MAP.get(prediction_id, "Unknown")
    output = {"prediction_label": label, "prediction_id": prediction_id, "probabilities": probabilities, "processed_features_count": len(features_ordered)}
    log_data = {"prediction_run_id": str(ObjectId()), "source_of_data": data.source_info, "prediction_result": output, "is_attack": label != "BENIGN"}
    await log_to_db("predictions_log", log_data, db_manager)
    return PredictionOutput(**output)

# --- Simülasyonlar ---
@router.post("/simulate/ddos", tags=["Simulations"])
async def simulate_ddos_endpoint(params: DDoSParams, background_tasks: BackgroundTasks):
    return await handle_simulation_and_log("ddos", params, run_ddos_simulation, background_tasks)

@router.post("/simulate/bruteforce", tags=["Simulations"])
async def simulate_bruteforce_endpoint(params: BruteForceParams, background_tasks: BackgroundTasks):
    return await handle_simulation_and_log("brute_force", params, run_bruteforce_simulation, background_tasks)

@router.post("/simulate/sqlinjection", tags=["Simulations"])
async def simulate_sqlinjection_endpoint(params: SQLInjectionParams, background_tasks: BackgroundTasks):
    return await handle_simulation_and_log("sql_injection", params, run_sqlinjection_simulation, background_tasks)

# --- Raporlar ve İstatistikler (TÜM KONTROLLER DÜZELTİLDİ) ---
@router.get("/reports/simulations", tags=["Reports"])
async def get_simulation_reports(limit: int = 20, skip: int = 0, sim_type: Optional[str] = None):
    db_conn = db_manager.get_db()
    if db_conn is None: raise HTTPException(503, "DB connection failed")
    def db_task():
        query = {}
        if sim_type: query["simulation_type"] = sim_type.lower()
        cursor = db_conn.simulations_log.find(query).sort("start_time", -1).skip(skip).limit(limit)
        logs = [serialize_mongo_doc(doc) for doc in cursor]
        total_count = db_conn.simulations_log.count_documents(query)
        return {"total_count": total_count, "data": logs}
    return await run_in_threadpool(db_task)

@router.get("/reports/predictions", tags=["Reports"])
async def get_prediction_reports(limit: int = 10, skip: int = 0):
    db_conn = db_manager.get_db()
    if db_conn is None: raise HTTPException(503, "DB connection failed")
    def db_task():
        query = {"is_attack": True}
        cursor = db_conn.predictions_log.find(query).sort("created_at", -1).skip(skip).limit(limit)
        logs = [serialize_mongo_doc(doc) for doc in cursor]
        total_count = db_conn.predictions_log.count_documents(query)
        return {"total_count": total_count, "data": logs}
    return await run_in_threadpool(db_task)

@router.get("/stats/attack_trends", tags=["Statistics"])
async def get_attack_trends():
    db_conn = db_manager.get_db()
    if db_conn is None: raise HTTPException(503, "DB connection failed")
    def db_task():
        pipeline = [{"$match": {"start_time": {"$gte": datetime.utcnow() - timedelta(hours=24)}}},{"$group": {"_id": {"hour": {"$hour": "$start_time"}, "type": "$simulation_type"}, "count": {"$sum": 1}}}]
        results = list(db_conn.simulations_log.aggregate(pipeline))
        formatted = {f"{h:02d}:00": {'ddos': 0, 'brute_force': 0, 'sql_injection': 0} for h in range(24)}
        for res in results:
            hour_str, attack_type = f"{res['_id']['hour']:02d}:00", res['_id']['type']
            if attack_type in formatted.get(hour_str, {}): formatted[hour_str][attack_type] = res['count']
        return formatted
    return await run_in_threadpool(db_task)

@router.get("/stats/detection_metrics", tags=["Statistics"])
async def get_detection_metrics():
    db_conn = db_manager.get_db()
    if db_conn is None:
        raise HTTPException(status_code=503, detail="DB connection failed")
    
    def db_task():
        pipeline = [{"$group": {"_id": "$is_attack", "count": {"$sum": 1}}}]
        results = list(db_conn.predictions_log.aggregate(pipeline))
        metrics = {"detected_attacks": 0, "benign_traffic": 0}
        for res in results:
            if res.get('_id'):
                metrics["detected_attacks"] = res['count']
            else:
                metrics["benign_traffic"] = res['count']
        return metrics
    
    return await run_in_threadpool(db_task)


def serialize_mongo_doc(doc):
    if not doc: return None
    if '_id' in doc:
        doc['id'] = str(doc['_id'])
        del doc['_id']
    for key, value in doc.items():
        if isinstance(value, datetime):
            doc[key] = value.isoformat()
    return doc

# --- KULLANICI YÖNETİMİ (NİHAİ, EN SAĞLAM VERSİYON) ---

@router.get("/users", response_model=List[UserInDB], tags=["Users"])
async def get_users():
    """Tüm kullanıcıları listeler."""
    db_conn = db_manager.get_db()
    if db_conn is None: raise HTTPException(503, "Database connection failed")
    
    def db_task():
        # Veritabanından gelen her dokümanı manuel olarak serileştir
        return [serialize_mongo_doc(user) for user in db_conn.users.find()]
    
    return await run_in_threadpool(db_task)

# --- KULLANICI YÖNETİMİ (NİHAİ VERSİYON) ---

@router.post("/users", response_model=UserInDB, status_code=201, tags=["Users"])
async def create_user(user: UserCreate):
    db_conn = db_manager.get_db()
    if db_conn is None: raise HTTPException(503, "Database not connected")
    
    def db_action():
        if db_conn.users.find_one({"$or": [{"username": user.username}, {"email": user.email}]}):
            return {"error": "Username or email already exists."}
        user_dict = user.dict()
        result = db_conn.users.insert_one(user_dict)
        return db_conn.users.find_one({"_id": result.inserted_id})

    created_user = await run_in_threadpool(db_action)

    if not created_user:
        raise HTTPException(500, "Failed to create user.")
    if "error" in created_user:
        raise HTTPException(409, detail=created_user["error"])
    
    # --- DÖNÜŞÜ MANUEL OLARAK SERİLEŞTİR ---
    return serialize_mongo_doc(created_user)

@router.get("/users", response_model=List[UserInDB], tags=["Users"])
async def get_users():
    db_conn = db_manager.get_db()
    if db_conn is None: raise HTTPException(503, "Database not connected")
    def db_call():
        # --- DÖNÜŞÜ MANUEL OLARAK SERİLEŞTİR ---
        return [serialize_mongo_doc(doc) for doc in db_conn.users.find()]
    return await run_in_threadpool(db_call)


@router.patch("/users/{user_id}", response_model=UserInDB, tags=["Users"])
async def update_user(user_id: str, payload: UserUpdate):
    db_conn = db_manager.get_db()
    if db_conn is None: raise HTTPException(503, "Database not connected")
    try: obj_id = ObjectId(user_id)
    except: raise HTTPException(400, "Invalid ID format")
    
    def db_action():
        update_data = payload.dict(exclude_unset=True)
        if not update_data: return "NoData"
        
        result = db_conn.users.update_one({"_id": obj_id}, {"$set": update_data})
        if result.matched_count == 0: return None
        
        return db_conn.users.find_one({"_id": obj_id})

    updated_user = await run_in_threadpool(db_action)
    
    if updated_user == "NoData": raise HTTPException(400, "No update data provided")
    if updated_user is None: raise HTTPException(404, "User not found")
        
    # --- DÖNÜŞÜ MANUEL OLARAK SERİLEŞTİR ---
    return serialize_mongo_doc(updated_user)

@router.delete("/users/{user_id}", status_code=204, tags=["Users"])
async def delete_user(user_id: str):
    """Belirtilen ID'ye sahip kullanıcıyı siler."""
    db_conn = db_manager.get_db()
    if db_conn is None: raise HTTPException(503, "Database connection failed")
    try:
        obj_id = ObjectId(user_id)
    except Exception:
        raise HTTPException(400, "Invalid User ID format")

    def db_task():
        return db_conn.users.delete_one({"_id": obj_id}).deleted_count

    deleted_count = await run_in_threadpool(db_task)
    if deleted_count == 0:
        raise HTTPException(404, "User not found")
    return

@router.get("/responses/actions", response_model=List[ResponseAction], tags=["Response"])
async def get_recommended_actions():
    """
    Önceden tanımlanmış yanıt eylemlerini döndürür. Gelecekte bu dinamik olabilir.
    """
    actions = [
        {"_id": "block_ip", "title": "Block Malicious IP", "description": "Immediately block the attacking IP address...", "severity": "High", "automated": True, "commands": ["iptables -A INPUT -s ... -j DROP"], "risk": "Low"},
        {"_id": "isolate_host", "title": "Isolate Infected Host", "description": "Quarantine the compromised workstation...", "severity": "Critical", "automated": True, "commands": ["network isolate ..."], "risk": "Medium"},
        {"_id": "enable_ddos_protection", "title": "Enable DDoS Protection", "description": "Activate advanced DDoS mitigation...", "severity": "High", "automated": True, "commands": ["cloudflare enable_ddos_protection"], "risk": "Low"},
    ]
    return actions

@router.get("/responses/history", response_model=List[ResponseHistory], tags=["Response"])
async def get_response_history(limit: int = 10):
    """Yanıt eylem geçmişini döndürür."""
    db_conn = db_manager.get_db()
    if db_conn is None: raise HTTPException(503, "DB connection failed")
    def db_task():
        return list(db_conn.response_history.find().sort("timestamp", -1).limit(limit))
    return await run_in_threadpool(db_task)

@router.post("/responses/execute", response_model=ResponseHistory, status_code=201, tags=["Response"])
async def execute_response_action(
    action_title: str = Body(...), 
    target_prediction_id: str = Body(default="custom"),
    executed_by: str = Body(default="analyst")
):
    """
    Bir yanıt eylemini 'yürütür' ve geçmişe kaydeder.
    """
    db_conn = db_manager.get_db()
    if db_conn is None: raise HTTPException(503, "DB connection failed")

    new_history_entry = {
        "action_title": action_title,
        "target": f"Alert ID: {target_prediction_id}",
        "status": "completed", # Şimdilik her eylemi anında başarılı sayalım
        "executed_by": executed_by,
        "result_message": f"Action '{action_title}' was executed successfully.",
        "timestamp": datetime.utcnow()
    }
    
    def db_task():
        result = db_conn.response_history.insert_one(new_history_entry)
        return db_conn.response_history.find_one({"_id": result.inserted_id})
        
    return await run_in_threadpool(db_task)

@router.post("/auth/token", tags=["Authentication"])
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    db_conn = db_manager.get_db()
    if db_conn is None: raise HTTPException(503, "DB connection failed")

    def get_user_from_db(username: str):
        return db_conn.users.find_one({"username": username})
    
    user = await run_in_threadpool(get_user_from_db, form_data.username)

    # --- HASH'LENMİŞ ŞİFREYİ DOĞRULA ---
    if not user or not verify_password(form_data.password, user.get("hashed_password", "")):
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=Config.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["username"], "role": user["role"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}