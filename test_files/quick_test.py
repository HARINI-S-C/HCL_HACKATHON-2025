from dotenv import load_dotenv
import os
import psycopg2

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")  # full URL from .env

try:
    conn = psycopg2.connect(DATABASE_URL)
    print("✅ Connected successfully using DATABASE_URL!")
    conn.close()
except Exception as e:
    print("❌ Connection failed:", e)
