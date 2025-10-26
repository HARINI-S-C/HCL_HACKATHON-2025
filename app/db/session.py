# # # session.py
# # import os
# # import sys
# # from sqlalchemy import create_engine, text
# # from sqlalchemy.orm import sessionmaker, DeclarativeBase
# # from dotenv import load_dotenv

# # # Load .env file
# # load_dotenv()

# # # --- Get DATABASE_URL from environment ---
# # DATABASE_URL = os.getenv("DATABASE_URL")

# # if not DATABASE_URL:
# #     print("❌ DATABASE_URL is not set in .env")
# #     sys.exit(1)

# # # --- Create SQLAlchemy Engine and Session ---
# # try:
# #     engine = create_engine(DATABASE_URL, echo=True, pool_pre_ping=True)
# #     SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
# #     Base = DeclarativeBase()

# #     # Optional: test connection
# #     with engine.connect() as conn:
# #         result = conn.execute(text("SELECT 1"))
# #         print("✅ Connection successful:", result.fetchone())

# #     print("✅ SQLAlchemy engine, session, and Base created successfully.")
# # except Exception as e:
# #     print("❌ Error creating SQLAlchemy engine/session:", e)
# #     sys.exit(1)



# # from sqlalchemy.orm import declarative_base, sessionmaker
# # from sqlalchemy import create_engine
# # import os
# # from dotenv import load_dotenv

# # load_dotenv()

# # DATABASE_URL = os.getenv("DATABASE_URL")
# # if not DATABASE_URL:
# #     raise ValueError("DATABASE_URL is not set!")

# # engine = create_engine(DATABASE_URL, echo=True, pool_pre_ping=True)
# # SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# # # Classic base with metadata support
# # Base = declarative_base()



# # session.py
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy import create_engine
# import os
# from dotenv import load_dotenv

# load_dotenv()

# DATABASE_URL = os.getenv("DATABASE_URL")
# engine = create_engine(DATABASE_URL, echo=True, pool_pre_ping=True)
# SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# # Classic declarative base
# from sqlalchemy.orm import declarative_base
# Base = declarative_base()

# # Dependency function for FastAPI routes
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()



from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./smartbank.db")

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency for routers
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
