from fastapi import FastAPI
from app.routes import payments, schools, students

app = FastAPI()

app.include_router(payments.router, prefix="/payments", tags=["payments"])
app.include_router(schools.router, prefix="/schools", tags=["schools"])
app.include_router(students.router, prefix="/students", tags=["students"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Knit Payment System"}