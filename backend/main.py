from fastapi import FastAPI

from backend.database import Base, engine
from backend.auth.auth_router import router as auth_router

from fastapi import Depends
from backend.auth.dependencies import get_current_user, require_role


# Create FastAPI app
app = FastAPI(title="Marketing Dashboard API")

# Create database tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(auth_router)


# Health check endpoint (public)
@app.get("/health")
def health_check():
    return {"status": "ok"}

# Any logged-in user can access this
@app.get("/protected/test")
def protected_test(user=Depends(get_current_user)):
    return {
        "message": "You are authenticated",
        "user_id": user.id,
        "role": user.role,
    }


# Only admin can access this
@app.get("/admin/test")
def admin_test(user=Depends(require_role(["admin"]))):
    return {
        "message": "Welcome Admin",
        "user_id": user.id,
        "role": user.role,
    }
