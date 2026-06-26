from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.api.routes import router
from app.core.config import GENERATED_IMAGE_DIR, PROJECT_NAME
from app.db.database import Base, engine
from app.models import image  # noqa: F401

Base.metadata.create_all(bind=engine)
GENERATED_IMAGE_DIR.mkdir(parents=True, exist_ok=True)

app = FastAPI(title=f"{PROJECT_NAME} API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/images", StaticFiles(directory=str(GENERATED_IMAGE_DIR)), name="images")
app.include_router(router)

@app.get("/")
def root():
    return {
        "message": "VisionForge AI backend is running",
        "docs": "/docs",
        "health": "/api/health",
    }
