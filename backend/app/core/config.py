from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
GENERATED_IMAGE_DIR = BASE_DIR / "generated_images"
DATABASE_URL = f"sqlite:///{BASE_DIR / 'visionforge.db'}"
API_BASE_URL = "http://127.0.0.1:8000"
PROJECT_NAME = "VisionForge AI"
