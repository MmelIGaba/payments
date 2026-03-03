from fastapi import APIRouter, HTTPException
from app.utils.db import get_db_client
from bson import ObjectId

router = APIRouter()

@router.get("/{id}/payments")
async def list_payments_for_student(id: str):
    db = get_db_client()
    collection = db["payments"]

    payments = collection.find({"student_id": ObjectId(id)})
    result = []
    for payment in payments:
        payment["id"] = str(payment["_id"])
        result.append(payment)

    return result