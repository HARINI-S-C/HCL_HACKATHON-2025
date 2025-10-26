import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

# Load .env file
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set!")

# Create engine
engine = create_engine(DATABASE_URL, echo=True)

# Test connection
with engine.connect() as conn:
    result = conn.execute(text("SELECT 1"))
    print("✅ Connection successful:", result.fetchone())



# import psycopg2

# # Try default values first
# conn = psycopg2.connect(
#     host="localhost",
#     port=5432,
#     user="postgres",
#     password="your_password",
#     dbname="postgres"
# )
# cur = conn.cursor()

# # List all databases
# cur.execute("SELECT datname FROM pg_database;")
# print("Databases:", cur.fetchall())

# # List all roles/users
# cur.execute("SELECT rolname FROM pg_roles;")
# print("Users/Roles:", cur.fetchall())

# cur.close()
# conn.close()
