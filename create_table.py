# create_tables.py
from app.db.session import Base, engine
from app.db import models  # ensure all models are imported

# Create all tables in the database
Base.metadata.create_all(bind=engine)

print("✅ All tables created successfully")
