from pydantic import BaseModel, HttpUrl
from typing import List, Dict, Any, Optional


class PredictionInput(BaseModel):
    features: Dict[str, float]
    source_info: Optional[str] = "manual_api_call"


class PredictionOutput(BaseModel):
    prediction_label: str
    prediction_id: int
    probabilities: Optional[List[float]] = None
    processed_features_count: int