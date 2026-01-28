from fastapi import FastAPI
from app.api.health import router as health_router

app = FastAPI(
    title="Secure DevSecOps API",
    description="Minimal API for DevSecOps pipeline demonstration",
    version="1.0.0"
)

app.include_router(health_router)
