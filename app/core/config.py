# import os
# import secrets
# from dotenv import load_dotenv
# from sqlalchemy import create_engine

# # -------------------------------
# # Load or create .env file
# # -------------------------------
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# ENV_PATH = os.path.join(BASE_DIR, ".env")

# if not os.path.exists(ENV_PATH):
#     SECRET_KEY = secrets.token_hex(32)
#     with open(ENV_PATH, "w") as f:
#         f.write(f"SECRET_KEY={SECRET_KEY}\n")
#     print(f".env file created with SECRET_KEY={SECRET_KEY}")
# else:
#     load_dotenv(ENV_PATH)
#     SECRET_KEY = os.getenv("SECRET_KEY") or secrets.token_hex(32)

# # -------------------------------
# # JWT Settings
# # -------------------------------
# ALGORITHM = "HS256"  # Default algorithm for JWT
# ACCESS_TOKEN_EXPIRE_MINUTES = 60

# # Optional: you can also define JWT_SECRET
# JWT_SECRET = os.getenv("JWT_SECRET", SECRET_KEY)
# JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", ALGORITHM)

# # -------------------------------
# # Database
# # -------------------------------
# DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")
# engine = create_engine(DATABASE_URL)

# # -------------------------------
# # Test config when running directly
# # -------------------------------
# if __name__ == "__main__":
#     print("SECRET_KEY:", SECRET_KEY)
#     print("JWT_ALGORITHM:", JWT_ALGORITHM)
#     print("DATABASE_URL:", DATABASE_URL)





import os
import secrets
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Load .env
ENV_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")
if not os.path.exists(ENV_PATH):
    SECRET_KEY = secrets.token_hex(32)
    with open(ENV_PATH, "w") as f:
        f.write(f"SECRET_KEY={SECRET_KEY}\n")
else:
    load_dotenv(ENV_PATH)
    SECRET_KEY = os.getenv("SECRET_KEY") or secrets.token_hex(32)

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")  # fallback
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

# SQLAlchemy engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {})
