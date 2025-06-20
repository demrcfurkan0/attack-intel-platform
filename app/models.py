from datetime import datetime
from pydantic import BaseModel, Field, EmailStr, ConfigDict
from typing import List, Dict, Any, Optional
from bson import ObjectId

# --- API Data Models ---

class PredictionInput(BaseModel):
    features: Dict[str, float]
    source_info: Optional[str] = "manual_api_call"
    simulation_id: Optional[str] = None 

class PredictionOutput(BaseModel):
    prediction_label: str
    prediction_id: int
    probabilities: Optional[List[float]] = None
    processed_features_count: int

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return str(v) # Return as ObjectId

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
    
class UserInDB(BaseModel):
    id: str
    username: str
    email: str
    role: str
    status: str
    
    # --- Response Action Models ---
    
class ResponseAction(BaseModel):
    id: str = Field(..., alias="_id")
    title: str
    description: str
    severity: str
    automated: bool
    commands: List[str]
    risk: str
    model_config = ConfigDict(populate_by_name=True, from_attributes=True)

class ResponseHistory(BaseModel):
    id: str = Field(..., alias="_id")
    action_title: str
    target: str
    status: str
    executed_by: str
    result_message: str
    timestamp: datetime
    model_config = ConfigDict(
        populate_by_name=True,
        from_attributes=True,
        arbitrary_types_allowed=True,
        json_encoders={ObjectId: str, datetime: lambda dt: dt.isoformat()},
    )