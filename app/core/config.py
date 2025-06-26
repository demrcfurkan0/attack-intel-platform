import os 
from dotenv import load_dotenv

load_dotenv()

class Config:
  MODEL_PATH = os.getenv("MODEL_PATH") 
  SCALER_PATH = os.getenv("SCALER_PATH")
  FEATURE_COLUMNS_PATH = os.getenv("FEATURE_COLUMNS_PATH")
  SECRET_KEY = os.getenv("SECRET_KEY", "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7")
  ALGORITHM = "HS256"
  ACCESS_TOKEN_EXPIRE_MINUTES = 30
  LABEL_MAP = {
    0: "BENIGN",
    1: "DoS/DDoS",
    2: "BruteForce",
    3: "SQL_Injection"
}

