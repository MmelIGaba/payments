from pydantic import BaseModel
from bson import ObjectId
from typing import Optional
from datetime import datetime

class Payment(BaseModel):
    id: Optional[ObjectId] = None
    student_id: ObjectId
    school_id: ObjectId
    amount: float
    knit_fee: float
    school_amount: float
    status: str
    reference: str
    created_at: Optional[datetime] = None

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }