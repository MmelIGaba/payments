from pydantic import BaseModel
from bson import ObjectId
from typing import Optional

class Student(BaseModel):
    id: Optional[ObjectId] = None
    name: str
    school_id: ObjectId

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }