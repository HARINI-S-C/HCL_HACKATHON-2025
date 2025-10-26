# test_models_readonly.py
from sqlalchemy import inspect
from app.db.session import engine, Base
from app.db import models  # import all your models to register them

# --- 1. Create tables if they don't exist (safe, no data added) ---
Base.metadata.create_all(engine)
print("✅ Tables checked/created successfully")

# --- 2. Inspect tables ---
inspector = inspect(engine)
table_names = inspector.get_table_names()

print("\n--- All tables in the database ---")
for t in table_names:
    print(t)

# --- 3. Inspect columns for each table ---
print("\n--- Columns for each table ---")
for table in table_names:
    columns = inspector.get_columns(table)
    print(f"\nTable: {table}")
    for col in columns:
        print(f"  {col['name']} ({col['type']})")
