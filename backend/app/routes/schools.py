from fastapi import APIRouter, HTTPException
from app.utils.db import get_db_client
from psycopg2.extras import RealDictCursor

router = APIRouter()

@router.get("/{id}/revenue")
async def get_school_revenue(id: int):
    db = get_db_client()
    cursor = db.cursor(cursor_factory=RealDictCursor)

    cursor.execute("""
        SELECT SUM(amount) AS total_collected, SUM(knit_fee) AS total_knit_fees, SUM(school_amount) AS total_paid_to_school
        FROM Payment
        WHERE school_id = %s
    """, (id,))

    revenue = cursor.fetchone()
    cursor.close()

    if not revenue:
        raise HTTPException(status_code=404, detail="No revenue data found")

    return revenue