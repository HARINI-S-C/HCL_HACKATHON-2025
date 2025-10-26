from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
JWT_SECRET = os.getenv("JWT_SECRET")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 60))

if not DATABASE_URL:
    raise ValueError("DATABASE_URL not found in environment variables!")
if not JWT_SECRET:
    raise ValueError("JWT_SECRET not found in environment variables!")
if not JWT_ALGORITHM:
    raise ValueError("JWT_ALGORITHM not found in environment variables!")
