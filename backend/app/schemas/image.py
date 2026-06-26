from datetime import datetime
from pydantic import BaseModel, Field

class GenerateImageRequest(BaseModel):
    prompt: str = Field(..., min_length=1, max_length=1000)
    style: str = "realistic"

class EnhancePromptRequest(BaseModel):
    prompt: str = Field(..., min_length=1, max_length=1000)
    style: str = "realistic"

class ImageResponse(BaseModel):
    id: int
    prompt: str
    enhanced_prompt: str
    style: str
    image_url: str
    status: str
    created_at: datetime

    model_config = {"from_attributes": True}

class EnhancePromptResponse(BaseModel):
    original_prompt: str
    enhanced_prompt: str
    style: str
