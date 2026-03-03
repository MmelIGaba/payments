from fastapi import APIRouter, HTTPException
from app.models.payment import Payment
from app.utils.db import get_db_client
from bson import ObjectId
from datetime import datetime

router = APIRouter()

@router.post("/")
async def create_payment(payment_request: Payment):
    db = get_db_client()
    collection = db["payments"]

    # Check for duplicate reference
    existing_payment = collection.find_one({"reference": payment_request.reference})
    if existing_payment:
        return {"id": str(existing_payment["_id"]), "status": existing_payment["status"]}

    knit_fee = payment_request.amount * 0.02
    school_amount = payment_request.amount * 0.98

    payment_data = {
        "student_id": ObjectId(payment_request.student_id),
        "school_id": ObjectId(payment_request.school_id),
        "amount": payment_request.amount,
        "knit_fee": knit_fee,
        "school_amount": school_amount,
        "status": "SUCCESS",
        "reference": payment_request.reference,
        "created_at": datetime.utcnow()
    }

    result = collection.insert_one(payment_data)
    return {
        "id": str(result.inserted_id),
        "amount": payment_request.amount,
        "knit_fee": knit_fee,
        "school_amount": school_amount,
        "status": "SUCCESS"
    }

@router.get("/{id}")
async def get_payment(id: str):
    db = get_db_client()
    collection = db["payments"]

    payment = collection.find_one({"_id": ObjectId(id)})
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")

    payment["id"] = str(payment["_id"])
    return payment