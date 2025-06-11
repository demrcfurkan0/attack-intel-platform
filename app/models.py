# attack-simulation/app/models.py

from pydantic import BaseModel, Field, EmailStr, ConfigDict
from typing import List, Dict, Any, Optional
from bson import ObjectId

# --- Prediction Modelleri ---
class PredictionInput(BaseModel):
    features: Dict[str, float]
    source_info: Optional[str] = "manual_api_call"
class PredictionOutput(BaseModel):
    prediction_label: str
    prediction_id: int
    probabilities: Optional[List[float]] = None
    processed_features_count: int

# --- Kullanıcı Modelleri ---
class UserBase(BaseModel):
    username: str
    email: EmailStr
    role: str
    status: str = "active"
class UserCreate(UserBase):
    password: str
class UserUpdate(BaseModel):
    role: Optional[str] = None
    status: Optional[str] = None
class UserInDB(UserBase):
    id: str = Field(..., alias='_id')
    model_config = ConfigDict(
        populate_by_name=True,
        from_attributes=True,
        arbitrary_types_allowed=True,
        json_encoders={ObjectId: str},
    )