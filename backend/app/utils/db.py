from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

def get_db_client():
    client = MongoClient(DATABASE_URL)
    db = client["knit"]
    return db