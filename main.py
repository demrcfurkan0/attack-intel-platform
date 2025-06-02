from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
import joblib
import numpy as np
import json
from pydantic import BaseModel
from typing import List, Dict, Any

# --- Import simulation functions and Pydantic models from simulations.py ---
from simulations import (
    DDoSParams,
    BruteForceParams,
    SQLInjectionParams,
    run_ddos_simulation,
    run_bruteforce_simulation,
    run_sqlinjection_simulation
)

# ---- Pydantic Models for AI Prediction (from previous steps) ----
class PredictionInput(BaseModel):
    features: Dict[str, float]

class PredictionOutput(BaseModel):
    prediction_label: str
    prediction_id: int
    probabilities: List[float] = None
    processed_features_count: int

# ---- Load Model, Scaler, and Feature Columns at Application Startup (from previous steps) ----
MODEL_PATH = "models/final_xgboost_model.pkl"  # Make sure this path is correct
SCALER_PATH = "models/final_scaler.pkl"    # Make sure this path is correct
FEATURE_COLUMNS_PATH = "models/feature_columns.json" # Make sure this path is correct

model = None
scaler = None
feature_columns = None
model_load_error: Optional[str] = None

try:
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    with open(FEATURE_COLUMNS_PATH, 'r') as f:
        feature_columns = json.load(f)
    print("✅ AI Model, Scaler, and Feature Columns loaded successfully.")
    if feature_columns:
        print(f"Model expects {len(feature_columns)} features.")
except FileNotFoundError as e:
    model_load_error = f"Model, scaler, or feature file not found: {e}"
    print(f"⚠️ Error: {model_load_error}")
except Exception as e:
    model_load_error = f"An error occurred while loading the model, scaler, or features: {e}"
    print(f"⚠️ Error: {model_load_error} (Check terminal logs for details)")

# Label map for human-readable predictions (from previous steps)
LABEL_MAP = {
    0: "BENIGN",
    1: "DoS/DDoS",
    2: "BruteForce",
    3: "SQL_Injection"
}

# ---- FastAPI Application ----
app = FastAPI(
    title="AI-Driven Cyber Attack Simulation and Response Tool",
    description="API for simulating cyber attacks and predicting threats using AI.",
    version="0.1.0"
)

# CORS Settings
origins = [
    "http://localhost:3000",  # Your React app's address
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

@app.get("/", tags=["General"])
async def read_root():
    """
    Root endpoint of the API. Returns a welcome message.
    """
    return {"message": "Welcome to the AI-Driven Cyber Attack Simulation API!"}

# --- AI Prediction Endpoint ---
@app.post("/api/predict", response_model=PredictionOutput, tags=["AI Prediction"])
async def predict_attack_endpoint(data: PredictionInput): # Renamed for clarity
    """
    Predicts the type of cyber attack based on the provided features.
    """
    if model_load_error or model is None or scaler is None or feature_columns is None:
        raise HTTPException(
            status_code=503,
            detail=f"AI Model, scaler, or feature list could not be loaded. Please check server logs. Error: {model_load_error}"
        )

    try:
        # Ensure features are in the same order as when the model was trained
        input_features_ordered = [data.features[col_name] for col_name in feature_columns]
    except KeyError as e:
        missing_feature = str(e).strip("'")
        raise HTTPException(
            status_code=400,
            detail=f"Missing feature: '{missing_feature}'. Please send all expected features ({len(feature_columns)} total)."
        )
    
    if len(input_features_ordered) != len(feature_columns):
        raise HTTPException(
            status_code=400,
            detail=f"Incorrect number of features sent. Expected: {len(feature_columns)}, Received: {len(input_features_ordered)}"
        )

    input_array = np.array([input_features_ordered], dtype=float)

    try:
        scaled_features = scaler.transform(input_array)
        prediction_id_array = model.predict(scaled_features)
        prediction_id = int(prediction_id_array[0])
        prediction_probabilities = model.predict_proba(scaled_features)[0].tolist()
    except Exception as e:
        print(f"Error during AI Prediction: {e}") # Log detailed error to server
        raise HTTPException(status_code=500, detail=f"An error occurred during model prediction: {str(e)}")

    prediction_label = LABEL_MAP.get(prediction_id, f"Unknown Label ({prediction_id})")

    return PredictionOutput(
        prediction_label=prediction_label,
        prediction_id=prediction_id,
        probabilities=prediction_probabilities,
        processed_features_count=len(input_features_ordered)
    )

# --- Simulation Endpoints ---
active_simulations: Dict[str, Any] = {} # In-memory store for active simulation tasks

@app.post("/api/simulate/ddos", summary="Start DDoS Attack Simulation", tags=["Simulations"])
async def simulate_ddos_bg_endpoint(params: DDoSParams, background_tasks: BackgroundTasks): # Renamed
    """
    Starts a DDoS attack simulation against the specified target.
    This operation is run in the background.
    """
    task_id = f"ddos_sim_{int(time.time() * 1000)}_{random.randint(1000,9999)}" # More unique task ID
    active_simulations[task_id] = {"status": "pending", "type": "DDoS", "params": params.dict(), "start_time": None, "result": None}
    
    print(f"DDoS simulation ({task_id}) being started as a background task for: {params.target_url}")
    
    async def ddos_task_wrapper(task_id_local: str, sim_params: DDoSParams):
        active_simulations[task_id_local]["status"] = "running"
        active_simulations[task_id_local]["start_time"] = time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime())
        try:
            result = await run_ddos_simulation(sim_params)
            active_simulations[task_id_local]["status"] = "completed"
            active_simulations[task_id_local]["result"] = result
            print(f"DDoS simulation ({task_id_local}) completed.")
        except Exception as e:
            error_message = f"Error during DDoS simulation ({task_id_local}): {str(e)}"
            print(error_message)
            active_simulations[task_id_local]["status"] = "failed"
            active_simulations[task_id_local]["result"] = {"error": error_message}

    background_tasks.add_task(ddos_task_wrapper, task_id, params)
    
    return {
        "message": "DDoS simulation started in the background.",
        "task_id": task_id,
        "target_url": str(params.target_url),
        "status_check_url": f"/api/simulate/status/{task_id}"
    }

@app.post("/api/simulate/bruteforce", summary="Start Brute Force Attack Simulation", tags=["Simulations"])
async def simulate_bruteforce_bg_endpoint(params: BruteForceParams, background_tasks: BackgroundTasks): # Renamed
    """
    Starts a Brute Force attack simulation against the specified target.
    This operation is run in the background.
    """
    task_id = f"bruteforce_sim_{int(time.time() * 1000)}_{random.randint(1000,9999)}"
    active_simulations[task_id] = {"status": "pending", "type": "BruteForce", "params": params.dict(), "start_time": None, "result": None}

    print(f"Brute Force simulation ({task_id}) being started as a background task for: {params.target_url}")

    async def bruteforce_task_wrapper(task_id_local: str, sim_params: BruteForceParams):
        active_simulations[task_id_local]["status"] = "running"
        active_simulations[task_id_local]["start_time"] = time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime())
        try:
            result = await run_bruteforce_simulation(sim_params)
            active_simulations[task_id_local]["status"] = "completed"
            active_simulations[task_id_local]["result"] = result
            print(f"Brute Force simulation ({task_id_local}) completed.")
        except Exception as e:
            error_message = f"Error during Brute Force simulation ({task_id_local}): {str(e)}"
            print(error_message)
            active_simulations[task_id_local]["status"] = "failed"
            active_simulations[task_id_local]["result"] = {"error": error_message}

    background_tasks.add_task(bruteforce_task_wrapper, task_id, params)

    return {
        "message": "Brute Force simulation started in the background.",
        "task_id": task_id,
        "target_url": str(params.target_url),
        "status_check_url": f"/api/simulate/status/{task_id}"
    }

@app.post("/api/simulate/sqlinjection", summary="Start SQL Injection Attack Simulation", tags=["Simulations"])
async def simulate_sqlinjection_bg_endpoint(params: SQLInjectionParams, background_tasks: BackgroundTasks): # Renamed
    """
    Starts an SQL Injection attack simulation against the specified target.
    This operation is run in the background.
    """
    task_id = f"sqlinjection_sim_{int(time.time() * 1000)}_{random.randint(1000,9999)}"
    active_simulations[task_id] = {"status": "pending", "type": "SQLInjection", "params": params.dict(), "start_time": None, "result": None}
    
    print(f"SQL Injection simulation ({task_id}) being started as a background task for: {params.target_url}")

    async def sqlinjection_task_wrapper(task_id_local: str, sim_params: SQLInjectionParams):
        active_simulations[task_id_local]["status"] = "running"
        active_simulations[task_id_local]["start_time"] = time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime())
        try:
            result = await run_sqlinjection_simulation(sim_params)
            active_simulations[task_id_local]["status"] = "completed"
            active_simulations[task_id_local]["result"] = result
            print(f"SQL Injection simulation ({task_id_local}) completed.")
        except Exception as e:
            error_message = f"Error during SQL Injection simulation ({task_id_local}): {str(e)}"
            print(error_message)
            active_simulations[task_id_local]["status"] = "failed"
            active_simulations[task_id_local]["result"] = {"error": error_message}

    background_tasks.add_task(sqlinjection_task_wrapper, task_id, params)
    
    return {
        "message": "SQL Injection simulation started in the background.",
        "task_id": task_id,
        "target_url": str(params.target_url),
        "status_check_url": f"/api/simulate/status/{task_id}"
    }

@app.get("/api/simulate/status/{task_id}", summary="Check the Status of a Simulation", tags=["Simulations"])
async def get_simulation_status_endpoint(task_id: str): # Renamed
    """
    Returns the current status and result (if completed) of the simulation with the given task_id.
    """
    if task_id in active_simulations:
        return active_simulations[task_id]
    else:
        raise HTTPException(status_code=404, detail="No simulation found with the specified task_id.")

# To run the app directly with Python (for development):
if __name__ == "__main__":
    import uvicorn
    # reload=True automatically detects changes during development
    # For production, reload should be False.
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)