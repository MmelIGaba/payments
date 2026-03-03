from fastapi import APIRouter, HTTPException
from app.models.payment import Payment
from app.utils.db import get_db_client
from psycopg2.extras import RealDictCursor
from datetime import datetime

router = APIRouter()

@router.post("/")
async def create_payment(payment_request: Payment):
    db = get_db_client()
    cursor = db.cursor(cursor_factory=RealDictCursor)

    cursor.execute("SELECT * FROM Payment WHERE reference = %s", (payment_request.reference,))
    existing_payment = cursor.fetchone()
    if existing_payment:
        return {"id": existing_payment['id'], "status": existing_payment['status']}

    knit_fee = payment_request.amount * 0.02
    school_amount = payment_request.amount * 0.98

    cursor.execute("""
        INSERT INTO Payment (student_id, school_id, amount, knit_fee, school_amount, status, reference)
        VALUES (%s, %s, %s, %s, %s, 'SUCCESS', %s)
        RETURNING id
    """, (payment_request.student_id, payment_request.school_id, payment_request.amount, knit_fee, school_amount, payment_request.reference))

    new_payment_id = cursor.fetchone()['id']
    db.commit()
    cursor.close()

    return {
        "id": new_payment_id,
        "amount": payment_request.amount,
        "knit_fee": knit_fee,
        "school_amount": school_amount,
        "status": "SUCCESS"
    }

@router.get("/{id}")
async def get_payment(id: int):
    db = get_db_client()
    cursor = db.cursor(cursor_factory=RealDictCursor)

    cursor.execute("SELECT * FROM Payment WHERE id = %s", (id,))
    payment = cursor.fetchone()
    cursor.close()

    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")

    return payment