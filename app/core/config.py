import os 
from dotenv import load_dotenv
import os

load_dotenv()

class Config:
  MODEL_PATH = os.getenv("MODEL_PATH") 
  SCALER_PATH = os.getenv("SCALER_PATH")
  FEATURE_COLUMNS_PATH = os.getenv("FEATURE_COLUMNS_PATH")

  LABEL_MAP = {
    0: "BENIGN",
    1: "DoS/DDoS",
    2: "BruteForce",
    3: "SQL_Injection"
}

