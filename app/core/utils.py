from pydantic import BaseModel, HttpUrl
from enum import Enum 
from datetime import datetime, timezone

def serialize_pydantic_for_mongo(pydantic_model_instance: BaseModel) -> dict:
    data_dict = pydantic_model_instance.dict(exclude_none=True) 
    
    serialized_dict = {}
    for key, value in data_dict.items():
        if isinstance(value, HttpUrl):
            serialized_dict[key] = str(value)
        elif isinstance(value, Enum):
            serialized_dict[key] = value.value
        elif isinstance(value, datetime):
            serialized_dict[key] = value.isoformat()
        # Diğer tipler için basit atama, eğer iç içe Pydantic modelleri veya karmaşık tipler varsa
        # bu fonksiyonun daha kapsamlı olması gerekebilir.
        else:
            serialized_dict[key] = value
    return serialized_dict
