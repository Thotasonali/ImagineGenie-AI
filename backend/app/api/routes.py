from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.config import API_BASE_URL
from app.db.database import get_db
from app.models.image import ImageRecord
from app.schemas.image import (
    EnhancePromptRequest,
    EnhancePromptResponse,
    GenerateImageRequest,
    ImageResponse,
)
from app.services.image_service import create_placeholder_image
from app.services.prompt_service import enhance_prompt

router = APIRouter(prefix="/api", tags=["ImagineGenie AI"])

@router.get("/health")
def health_check():
    return {"status": "ok", "service": "ImagineGenie AI API"}

@router.post("/enhance-prompt", response_model=EnhancePromptResponse)
def enhance_prompt_endpoint(payload: EnhancePromptRequest):
    enhanced = enhance_prompt(payload.prompt, payload.style)
    return EnhancePromptResponse(
        original_prompt=payload.prompt,
        enhanced_prompt=enhanced,
        style=payload.style,
    )

@router.post("/generate", response_model=ImageResponse)
def generate_image(payload: GenerateImageRequest, db: Session = Depends(get_db)):
    enhanced = enhance_prompt(payload.prompt, payload.style)
    filename = create_placeholder_image(enhanced, payload.style)
    image_url = f"{API_BASE_URL}/images/{filename}"

    record = ImageRecord(
        prompt=payload.prompt,
        enhanced_prompt=enhanced,
        style=payload.style,
        image_url=image_url,
        status="completed",
    )
    db.add(record)
    db.commit()
    db.refresh(record)
    return record

@router.get("/history", response_model=list[ImageResponse])
def get_history(db: Session = Depends(get_db)):
    return db.query(ImageRecord).order_by(ImageRecord.id.desc()).limit(50).all()

@router.delete("/history/{image_id}")
def delete_image(image_id: int, db: Session = Depends(get_db)):
    record = db.query(ImageRecord).filter(ImageRecord.id == image_id).first()
    if not record:
        return {"deleted": False, "message": "Image not found"}
    db.delete(record)
    db.commit()
    return {"deleted": True, "id": image_id}
