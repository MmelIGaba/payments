from pydantic import BaseModel
from bson import ObjectId
from typing import Optional

class School(BaseModel):
    id: Optional[ObjectId] = None
    name: str
    bank_account: str

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }