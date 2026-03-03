from fastapi import APIRouter, HTTPException
from app.utils.db import get_db_client
from psycopg2.extras import RealDictCursor

router = APIRouter()

@router.get("/{id}/payments")
async def list_payments_for_student(id: int):
    db = get_db_client()
    cursor = db.cursor(cursor_factory=RealDictCursor)

    cursor.execute("SELECT * FROM Payment WHERE student_id = %s", (id,))
    payments = cursor.fetchall()
    cursor.close()

    if not payments:
        raise HTTPException(status_code=404, detail="No payments found")

    return payments