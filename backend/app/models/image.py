from datetime import datetime
from sqlalchemy import DateTime, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column
from app.db.database import Base

class ImageRecord(Base):
    __tablename__ = "image_records"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    prompt: Mapped[str] = mapped_column(Text, nullable=False)
    enhanced_prompt: Mapped[str] = mapped_column(Text, nullable=False)
    style: Mapped[str] = mapped_column(String(80), nullable=False)
    image_url: Mapped[str] = mapped_column(String(500), nullable=False)
    status: Mapped[str] = mapped_column(String(50), default="completed")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
