import os
from datetime import datetime, timedelta, timezone
from ipaddress import ip_address
from typing import Any, Dict, List, Optional

import google.generativeai as genai
import numpy as np
import pandas as pd
from bson import ObjectId
from fastapi import (APIRouter, BackgroundTasks, Body, Depends, HTTPException)
from fastapi.concurrency import run_in_threadpool
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel, validator

from app.core import state
from app.core.config import Config
from app.core.security import (ACCESS_TOKEN_EXPIRE_MINUTES,
                               create_access_token, get_password_hash,
                               verify_password)
from app.core.utils import send_alert_email, serialize_mongo_doc
from app.database import db_manager, get_db_dependency, log_to_db
from app.models import *
from app.services.simulation_handler import handle_simulation_and_log
from app.simulations import *

# --- Pydantic Models for Request Validation ---

class BlockIPPayload(BaseModel):
    ip_address: str
    @validator('ip_address')
    def validate_ip(cls, v):
        try:
            ip_address(v)
            return v
        except ValueError:
            raise ValueError(f"{v} is not a valid IP address")

class TagsPayload(BaseModel):
    tags: List[str]

class UpdatePredictionStatus(BaseModel):
    status: str

class ChatPromptPayload(BaseModel):
    prompt: str
    incident_details: Dict[str, Any]
    
# --- API Router Initialization ---

router = APIRouter(prefix="/api")

# --- Helper Functions ---

def serialize_user(doc: Dict[str, Any]) -> Dict[str, Any]:
    if not doc: return {}
    return { "id": str(doc.get("_id", "")), "username": doc.get("username", ""), "email": doc.get("email", ""), "role": doc.get("role", ""), "status": doc.get("status", "inactive") }

# --- General Endpoints ---

@router.get("/", tags=["General"])
async def read_root():
    return {"message": "API is running!"}

# --- AI Model Endpoints ---

@router.post("/predict", response_model=PredictionOutput, tags=["AI Model"])
async def predict_attack_endpoint(data: PredictionInput, background_tasks: BackgroundTasks, db_conn: any = Depends(get_db_dependency)):
    if state.model is None or state.scaler is None or not state.feature_columns:
        raise HTTPException(status_code=503, detail="AI Model, Scaler, or Feature Columns are not available.")
    # Preprocess features and make a prediction
    input_df = pd.DataFrame([data.features])
    input_df = input_df.reindex(columns=state.feature_columns, fill_value=0.0)
    scaled_features = state.scaler.transform(input_df)
    prediction_id = int(state.model.predict(scaled_features)[0])
    probabilities = getattr(state.model, 'predict_proba', lambda _: [[]])(scaled_features)[0].tolist() or None
    label = Config.LABEL_MAP.get(prediction_id, "Unknown")
    is_attack = label != "BENIGN"
    
    # Send an email alert if an attack is detected
    
    if is_attack:
        subject = f"SECURITY ALERT: {label} Attack Detected!"
        body = f"A potential security threat has been detected.\n\nType: {label}\nSource: {data.source_info}\nTimestamp: {datetime.now(timezone.utc).isoformat()}"
        background_tasks.add_task(send_alert_email, subject, body)

    output = {"prediction_label": label, "prediction_id": prediction_id, "probabilities": probabilities, "processed_features_count": len(input_df.columns)}
    
      # Log the prediction to the database
      
    log_data = {
        "prediction_run_id": str(ObjectId()),
        "source_of_data": data.source_info,
        "prediction_result": output,
        "is_attack": is_attack,
        "simulation_id": data.simulation_id
    }
    await log_to_db("predictions_log", log_data, db_manager)
    
    return PredictionOutput(**output)

# --- Simulation Endpoints ---

@router.post("/simulate/ddos", tags=["Simulations"])
async def simulate_ddos_endpoint(params: DDoSParams, background_tasks: BackgroundTasks):
    return await handle_simulation_and_log("ddos", params, run_ddos_simulation, background_tasks, ground_truth_label=Config.LABEL_MAP.get(1, "DoS/DDoS"))

@router.post("/simulate/bruteforce", tags=["Simulations"])
async def simulate_bruteforce_endpoint(params: BruteForceParams, background_tasks: BackgroundTasks):
    return await handle_simulation_and_log("brute_force", params, run_bruteforce_simulation, background_tasks, ground_truth_label=Config.LABEL_MAP.get(2, "BruteForce"))

@router.post("/simulate/sqlinjection", tags=["Simulations"])
async def simulate_sqlinjection_endpoint(params: SQLInjectionParams, background_tasks: BackgroundTasks):
    return await handle_simulation_and_log("sql_injection", params, run_sqlinjection_simulation, background_tasks, ground_truth_label=Config.LABEL_MAP.get(3, "SQL_Injection"))

@router.post("/simulate/synflood", tags=["Simulations"])
async def simulate_synflood_endpoint(params: SYNFloodParams, background_tasks: BackgroundTasks):
    return await handle_simulation_and_log("syn_flood", params, run_synflood_simulation, background_tasks, ground_truth_label=Config.LABEL_MAP.get(1, "DoS/DDoS"))

# --- Reporting and Statistics Endpoints ---

@router.get("/reports/simulations", tags=["Reports"])
async def get_simulation_reports(limit: int = 20, skip: int = 0, sim_type: Optional[str] = None, db_conn: any = Depends(get_db_dependency)):
    def db_task():
        query = {}
        if sim_type and sim_type.strip(): query["simulation_type"] = sim_type.lower().strip()
        cursor = db_conn.simulations_log.find(query).sort("start_time", -1).skip(skip).limit(limit)
        return {"total_count": db_conn.simulations_log.count_documents(query), "data": [serialize_mongo_doc(doc) for doc in cursor]}
    return await run_in_threadpool(db_task)

@router.get("/reports/predictions", tags=["Reports"])
async def get_prediction_reports(limit: int = 10, skip: int = 0, db_conn: any = Depends(get_db_dependency)):
    def db_task():
        query = {"is_attack": True}
        cursor = db_conn.predictions_log.find(query).sort("created_at", -1).skip(skip).limit(limit)
        return {"total_count": db_conn.predictions_log.count_documents(query), "data": [serialize_mongo_doc(doc) for doc in cursor]}
    return await run_in_threadpool(db_task)

@router.get("/reports/predictions/{prediction_id}", tags=["Reports"])
async def get_single_prediction_report(prediction_id: str, db_conn: any = Depends(get_db_dependency)):
    if not ObjectId.is_valid(prediction_id): raise HTTPException(status_code=400, detail="Invalid Prediction ID format")
    prediction_doc = await run_in_threadpool(db_conn.predictions_log.find_one, {"_id": ObjectId(prediction_id)})
    if prediction_doc is None: raise HTTPException(status_code=404, detail="Prediction log not found")
    return serialize_mongo_doc(prediction_doc)

@router.patch("/reports/predictions/{prediction_id}/status", tags=["Reports"])
async def update_prediction_status(prediction_id: str, payload: UpdatePredictionStatus, db_conn: any = Depends(get_db_dependency)):
    if not ObjectId.is_valid(prediction_id): raise HTTPException(status_code=400, detail="Invalid Prediction ID format")
    update_data = {"$set": {"status": payload.status, "last_updated": datetime.now(timezone.utc)}}
    result = await run_in_threadpool(db_conn.predictions_log.update_one, {"_id": ObjectId(prediction_id)}, update_data)
    if result.matched_count == 0: raise HTTPException(status_code=404, detail="Prediction log not found to update")
    return {"message": f"Status updated to '{payload.status}' successfully."}

@router.patch("/reports/predictions/{prediction_id}/tags", tags=["Reports"])
async def update_prediction_tags(prediction_id: str, payload: TagsPayload, db_conn: any = Depends(get_db_dependency)):
    if not ObjectId.is_valid(prediction_id): raise HTTPException(status_code=400, detail="Invalid Prediction ID format")
    cleaned_tags = [tag.strip().lower() for tag in payload.tags if tag.strip()]
    update_data = {"$set": {"tags": cleaned_tags, "last_updated": datetime.now(timezone.utc)}}
    result = await run_in_threadpool(db_conn.predictions_log.update_one, {"_id": ObjectId(prediction_id)}, update_data)
    if result.matched_count == 0: raise HTTPException(status_code=404, detail="Prediction log not found to update")
    return {"message": "Tags updated successfully.", "tags": cleaned_tags}

@router.get("/stats/attack_trends", tags=["Statistics"])
async def get_attack_trends(db_conn: any = Depends(get_db_dependency)):
    def db_task():
        pipeline = [{"$match": {"start_time": {"$gte": datetime.now(timezone.utc) - timedelta(hours=24)}}},
                    {"$group": {"_id": {"hour": {"$hour": "$start_time"}, "type": "$simulation_type"}, "count": {"$sum": 1}}}]
        results = list(db_conn.simulations_log.aggregate(pipeline))
        formatted = {f"{h:02d}:00": {'ddos': 0, 'brute_force': 0, 'sql_injection': 0} for h in range(24)}
        for res in results:
            hour_str = f"{res['_id']['hour']:02d}:00"
            attack_type = res['_id']['type']
            if hour_str in formatted and attack_type in formatted[hour_str]:
                formatted[hour_str][attack_type] = res['count']
        return formatted
    return await run_in_threadpool(db_task)

@router.get("/stats/detection_metrics", tags=["Statistics"])
async def get_detection_metrics(db_conn: any = Depends(get_db_dependency)):
    def db_task():
        pipeline = [{"$group": {"_id": "$is_attack", "count": {"$sum": 1}}}]
        results = list(db_conn.predictions_log.aggregate(pipeline))
        metrics = {"detected_attacks": 0, "benign_traffic": 0}
        for res in results:
            if res.get('_id') is True: metrics["detected_attacks"] = res.get('count', 0)
            else: metrics["benign_traffic"] = res.get('count', 0)
        return metrics
    return await run_in_threadpool(db_task)

@router.get("/stats/model-performance", tags=["Statistics"])
async def get_model_performance(db_conn: any = Depends(get_db_dependency)):
    all_labels = list(Config.LABEL_MAP.values())
    pipeline = [
        {"$match": {"status": "completed", "ground_truth_label": {"$exists": True}}},
        {"$lookup": {"from": "predictions_log", "localField": "simulation_id", "foreignField": "simulation_id", "as": "predictions"}},
        {"$unwind": "$predictions"},
        {"$group": {"_id": {"ground_truth": "$ground_truth_label", "predicted": "$predictions.prediction_result.prediction_label"}, "count": {"$sum": 1}}},
        {"$group": {"_id": "$_id.ground_truth", "predictions": {"$push": {"predicted_label": "$_id.predicted", "count": "$count"}}}}
    ]
    def db_task():
        confusion_matrix = {true_label: {pred_label: 0 for pred_label in all_labels} for true_label in all_labels}
        results = list(db_conn.simulations_log.aggregate(pipeline))
        for result in results:
            true_label = result["_id"]
            if true_label in confusion_matrix:
                for pred in result["predictions"]:
                    predicted_label = pred["predicted_label"]
                    if predicted_label in confusion_matrix[true_label]:
                        confusion_matrix[true_label][predicted_label] = pred["count"]
        return confusion_matrix
    return await run_in_threadpool(db_task)

# --- Authentication ---
@router.post("/auth/token", tags=["Authentication"])
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db_conn: any = Depends(get_db_dependency)):
    user = await run_in_threadpool(db_conn.users.find_one, {"username": form_data.username})
    if not user or not verify_password(form_data.password, user.get("password", "")):
        raise HTTPException(status_code=401, detail="Incorrect username or password", headers={"WWW-Authenticate": "Bearer"})
    token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user["username"]}, expires_delta=token_expires)
    return {"access_token": access_token, "token_type": "bearer"}

# --- User Management ---
@router.post("/users", response_model=UserInDB, status_code=201, tags=["Users"])
async def create_user(user: UserCreate, db_conn: any = Depends(get_db_dependency)):
    def db_task():
        if db_conn.users.find_one({"$or": [{"username": user.username}, {"email": user.email}]}): return {"error": "Username or email already exists"}
        user_dict = user.dict()
        user_dict["password"] = get_password_hash(user.password)
        result = db_conn.users.insert_one(user_dict)
        return db_conn.users.find_one({"_id": result.inserted_id})
    new_user_doc = await run_in_threadpool(db_task)
    if new_user_doc and "error" in new_user_doc: raise HTTPException(status_code=409, detail=new_user_doc["error"])
    
    return serialize_user(new_user_doc)

@router.get("/users", response_model=List[UserInDB], tags=["Users"])
async def get_users(db_conn: any = Depends(get_db_dependency)):
    return [serialize_user(doc) for doc in await run_in_threadpool(list, db_conn.users.find())]

@router.patch("/users/{user_id}", response_model=UserInDB, tags=["Users"])
async def update_user(user_id: str, payload: UserUpdate, db_conn: any = Depends(get_db_dependency)):
    if not ObjectId.is_valid(user_id): raise HTTPException(status_code=400, detail="Invalid User ID format")
    update_data = payload.dict(exclude_unset=True)
    if not update_data: raise HTTPException(status_code=400, detail="No update data provided")
    result = await run_in_threadpool(db_conn.users.update_one, {"_id": ObjectId(user_id)}, {"$set": update_data})
    if result.matched_count == 0: raise HTTPException(status_code=404, detail="User not found")
    updated_user_doc = await run_in_threadpool(db_conn.users.find_one, {"_id": ObjectId(user_id)})
    return serialize_user(updated_user_doc)

@router.delete("/users/{user_id}", status_code=204, tags=["Users"])
async def delete_user(user_id: str, db_conn: any = Depends(get_db_dependency)):
    if not ObjectId.is_valid(user_id): raise HTTPException(status_code=400, detail="Invalid User ID format")
    result = await run_in_threadpool(db_conn.users.delete_one, {"_id": ObjectId(user_id)})
    if result.deleted_count == 0: raise HTTPException(status_code=404, detail="User not found")
    return

# --- Response Actions ---
@router.post("/responses/block-ip", status_code=201, tags=["Response"])
async def block_ip_address(payload: BlockIPPayload, db_conn: any = Depends(get_db_dependency)):
    ip_to_block = payload.ip_address
    block_record = { "ip_address": ip_to_block, "blocked_at": datetime.now(timezone.utc), "reason": "Blocked in response to a detected threat." }
    result = await run_in_threadpool(db_conn.blocked_ips.update_one, {"ip_address": ip_to_block}, {"$set": block_record}, upsert=True)
    if result.upserted_id is not None or result.matched_count > 0:
        return {"message": f"IP address {ip_to_block} has been successfully added to the blocklist."}
    raise HTTPException(status_code=500, detail="Failed to update blocklist.")

@router.get("/responses/actions", response_model=List[ResponseAction], tags=["Response"])
async def get_recommended_actions(db_conn: any = Depends(get_db_dependency)):
    return await run_in_threadpool(list, db_conn.response_actions.find())

@router.post("/responses/execute", response_model=ResponseHistory, status_code=201, tags=["Response"])
async def execute_response_action(action_title: str = Body(...), target_prediction_id: str = Body(...), executed_by: str = Body(default="analyst"), db_conn: any = Depends(get_db_dependency)):
    if not ObjectId.is_valid(target_prediction_id): raise HTTPException(status_code=400, detail="Invalid Prediction ID format")
    new_history_entry = { "action_title": action_title, "target": f"Prediction ID: {target_prediction_id}", "target_prediction_id": ObjectId(target_prediction_id), "status": "completed", "executed_by": executed_by, "result_message": f"Action '{action_title}' was logged.", "timestamp": datetime.now(timezone.utc) }
    result = await run_in_threadpool(db_conn.response_history.insert_one, new_history_entry)
    inserted_doc = await run_in_threadpool(db_conn.response_history.find_one, {"_id": result.inserted_id})
    return serialize_mongo_doc(inserted_doc)

@router.get("/responses/history", response_model=List[ResponseHistory], tags=["Response"])
async def get_response_history(limit: int = 10, db_conn: any = Depends(get_db_dependency)):
    cursor = await run_in_threadpool(db_conn.response_history.find().sort, "timestamp", -1)
    return [serialize_mongo_doc(doc) for doc in cursor.limit(limit)]

@router.get("/responses/history/{prediction_id}", response_model=List[ResponseHistory], tags=["Response"])
async def get_incident_response_history(prediction_id: str, db_conn: any = Depends(get_db_dependency)):
    if not ObjectId.is_valid(prediction_id): raise HTTPException(status_code=400, detail="Invalid Prediction ID format")
    cursor = await run_in_threadpool(db_conn.response_history.find({"target_prediction_id": ObjectId(prediction_id)}).sort, "timestamp", 1)
    return [serialize_mongo_doc(doc) for doc in cursor]

# --- CHATBOT ---
@router.post("/chatbot/query", tags=["Chatbot"])
async def handle_chatbot_query(payload: ChatPromptPayload):
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise HTTPException(status_code=500, detail="Google API key is not configured on the server.")

    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(model_name="gemini-1.5-flash-latest")
        
        full_prompt = f"""
        **Role and Goal:** You are 'CyberShield Co-Pilot', a helpful AI assistant for Security Operations Center (SOC) analysts. Your role is to analyze the provided incident data and give clear, concise, and actionable advice.
        **Instructions:**
        1. Base your answers ONLY on the provided incident data. Do not invent information.
        2. Provide your response in clear, easy-to-understand language.
        3. Use markdown for formatting, especially for lists.
        ---
        **Security Incident Data:**
        ```json
        {payload.incident_details}
        ```
        **User's Question:**
        {payload.prompt}
        """
        
        response = await model.generate_content_async(full_prompt)
        return {"response": response.text}

    except Exception as e:
        print(f"Error communicating with Google AI: {e}")
        error_message = "Could not get a response from the AI assistant."
        if "API key not valid" in str(e):
            error_message = "The configured Google API key is not valid."
        raise HTTPException(status_code=503, detail=error_message)