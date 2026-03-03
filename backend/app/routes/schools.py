from fastapi import APIRouter, HTTPException
from app.utils.db import get_db_client
from bson import ObjectId

router = APIRouter()

@router.get("/{id}/revenue")
async def get_school_revenue(id: str):
    db = get_db_client()
    collection = db["payments"]

    pipeline = [
        {"$match": {"school_id": ObjectId(id)}},
        {"$group": {
            "_id": None,
            "total_collected": {"$sum": "$amount"},
            "total_knit_fees": {"$sum": "$knit_fee"},
            "total_paid_to_school": {"$sum": "$school_amount"}
        }}
    ]

    result = collection.aggregate(pipeline).next()
    return result