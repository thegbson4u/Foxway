from fastapi import FastAPI

from backend.app.api.routes.health import router as health_router


app = FastAPI(
    title="FOXWAY",
    description="AI-Powered Threat Intelligence Framework",
    version="0.1.0",
)


app.include_router(health_router)


@app.get("/")
def root():
    return {
        "project": "FOXWAY",
        "status": "under development",
    }