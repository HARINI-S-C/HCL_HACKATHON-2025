# # import os
# # from dotenv import load_dotenv

# # load_dotenv()

# # DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg2://user:password@localhost:5432/smartbankdb")
# # SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")
# # ALGORITHM = "HS256"
# # ACCESS_TOKEN_EXPIRE_MINUTES = 60

# # app/core/config.py
# # import os
# # from dotenv import load_dotenv
# # from sqlalchemy import create_engine

# # # Load environment variables from .env
# # load_dotenv()

# # # Get database URL and secret key from environment
# # DATABASE_URL = os.getenv("DATABASE_URL")
# # SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")
# # ALGORITHM = "HS256"
# # ACCESS_TOKEN_EXPIRE_MINUTES = 60

# # # Create SQLAlchemy engine
# # engine = create_engine(DATABASE_URL)

# # # Optional: test connection
# # try:
# #     with engine.connect() as connection:
# #         print("✅ Database connection successful!")
# # except Exception as e:
# #     print("❌ Database connection failed!")
# #     print("Error:", e)




# import secrets
# import os
# from dotenv import load_dotenv
# from sqlalchemy import create_engine

# # Path to your .env file
# ENV_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), ".env")

# # Generate a 32-byte secret key if it doesn't exist in .env
# if not os.path.exists(ENV_PATH):
#     SECRET_KEY = secrets.token_hex(32)
#     with open(ENV_PATH, "w") as f:
#         f.write(f"SECRET_KEY={SECRET_KEY}\n")
#     print(f".env file created with SECRET_KEY={SECRET_KEY}")
# else:
#     # Load existing .env first
#     load_dotenv(ENV_PATH)
#     SECRET_KEY = os.getenv("SECRET_KEY")
#     if not SECRET_KEY:
#         # Append new SECRET_KEY if missing
#         SECRET_KEY = secrets.token_hex(32)
#         with open(ENV_PATH, "a") as f:
#             f.write(f"SECRET_KEY={SECRET_KEY}\n")
#         print(f"SECRET_KEY={SECRET_KEY} added to existing .env")

# # Load other environment variables
# load_dotenv(ENV_PATH)
# DATABASE_URL = os.getenv("DATABASE_URL")
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 60
# # Create SQLAlchemy engine
# engine = create_engine(DATABASE_URL)

# # Optional: test connection
# # try:
# #     with engine.connect() as connection:
# #         print("✅ Database connection successful!")
# # except Exception as e:
# #     print("❌ Database connection failed!")
# #     print("Error:", e)


# if __name__ == "__main__":
#     print("🔑 SECRET_KEY:", SECRET_KEY)
#     print("🗄 DATABASE_URL:", DATABASE_URL)
    
#     # Test database connection
#     try:
#         with engine.connect() as connection:
#             print("✅ Database connection successful!")
#             result = connection.execute("SELECT version();")
#             print("PostgreSQL version:", result.fetchone())
#     except Exception as e:
#         print("❌ Database connection failed!")
#         print("Error:", e)



# app/core/config.py

import os
import secrets
from dotenv import load_dotenv
from sqlalchemy import create_engine

# -------------------------------
# Path to your .env file (project root)
# -------------------------------
ENV_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__))), ".env"
)

# -------------------------------
# Auto-generate SECRET_KEY if missing
# -------------------------------
if not os.path.exists(ENV_PATH):
    SECRET_KEY = secrets.token_hex(32)
    with open(ENV_PATH, "w") as f:
        f.write(f"SECRET_KEY={SECRET_KEY}\n")
    print(f".env file created with SECRET_KEY={SECRET_KEY}")
else:
    # Load existing .env
    load_dotenv(ENV_PATH)
    SECRET_KEY = os.getenv("SECRET_KEY")
    if not SECRET_KEY:
        SECRET_KEY = secrets.token_hex(32)
        with open(ENV_PATH, "a") as f:
            f.write(f"SECRET_KEY={SECRET_KEY}\n")
        print(f"SECRET_KEY={SECRET_KEY} added to existing .env")

# -------------------------------
# Load other environment variables
# -------------------------------
load_dotenv(ENV_PATH)
DATABASE_URL = os.getenv("DATABASE_URL")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

# -------------------------------
# Create SQLAlchemy engine
# -------------------------------
engine = create_engine(DATABASE_URL)

# -------------------------------
# Optional test when running directly
# -------------------------------
if __name__ == "__main__":
    print("🔑 SECRET_KEY:", SECRET_KEY)
    print("🗄 DATABASE_URL:", DATABASE_URL)
    
    try:
        with engine.connect() as connection:
            print("✅ Database connection successful!")
            result = connection.execute("SELECT version();")
            print("PostgreSQL version:", result.fetchone())
    except Exception as e:
        print("❌ Database connection failed!")
        print("Error:", e)
