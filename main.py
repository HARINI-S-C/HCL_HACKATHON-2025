# from fastapi import FastAPI
# from slowapi import Limiter, _rate_limit_exceeded_handler
# from slowapi.util import get_remote_address
# from slowapi.errors import RateLimitExceeded
# from app.api.routes import auth, kyc, account
# from app.db.session import engine, Base

# # Create all tables
# Base.metadata.create_all(bind=engine)

# # Initialize FastAPI app
# app = FastAPI(title="SmartBank - Modular Banking Backend")

# # Initialize rate limiter
# limiter = Limiter(key_func=get_remote_address)
# app.state.limiter = limiter
# app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# # Include routers
# app.include_router(auth.router, prefix="/auth", tags=["Auth"])
# app.include_router(account.router, prefix="/account", tags=["Account"])
# app.include_router(kyc.router, prefix="/kyc", tags=["KYC"])

# # Optional root endpoint
# @app.get("/")
# def root():
#     return {"message": "Welcome to SmartBank API!"}




# # Option 1: import from __init__.py
# # from app.api.routes import account, auth, kyc

# # app = FastAPI(title="SmartBank - Modular Banking Backend")
# # app.include_router(account.router, prefix="/account", tags=["Account"])
# # app.include_router(auth.router, prefix="/auth", tags=["Auth"])
# # app.include_router(kyc.router, prefix="/kyc", tags=["KYC"])



from fastapi import FastAPI
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from app.db.session import Base, engine
import pkgutil
import importlib
import app.api.routes as routes_package

# ------------------------
# Create database tables
# ------------------------
Base.metadata.create_all(bind=engine)

# ------------------------
# Initialize FastAPI app
# ------------------------
app = FastAPI(title="SmartBank - Modular Banking Backend")

# ------------------------
# Initialize SlowAPI rate limiter
# ------------------------
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# ------------------------
# Dynamically include all routers in app.api.routes
# ------------------------
for loader, module_name, is_pkg in pkgutil.iter_modules(routes_package.__path__):
    module = importlib.import_module(f"app.api.routes.{module_name}")
    if hasattr(module, "router"):
        router = getattr(module, "router")
        prefix = f"/{module_name}"  # Use filename as prefix
        app.include_router(router, prefix=prefix, tags=[module_name.capitalize()])

# ------------------------
# Optional root endpoint
# ------------------------
@app.get("/")
def root():
    return {"message": "Welcome to SmartBank API!"}
