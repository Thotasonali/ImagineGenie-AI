from pathlib import Path
from textwrap import wrap
from uuid import uuid4
from PIL import Image, ImageDraw
from app.core.config import GENERATED_IMAGE_DIR


def create_placeholder_image(enhanced_prompt: str, style: str) -> str:
    GENERATED_IMAGE_DIR.mkdir(parents=True, exist_ok=True)

    width, height = 1024, 1024
    image = Image.new("RGB", (width, height), (15, 23, 42))
    draw = ImageDraw.Draw(image)

    # Decorative blocks for a polished placeholder preview.
    draw.rounded_rectangle((70, 70, 954, 954), radius=36, outline=(99, 102, 241), width=4)
    draw.rounded_rectangle((110, 120, 914, 260), radius=24, fill=(30, 41, 59))
    draw.text((140, 150), "ImagineGenie AI", fill=(255, 255, 255))
    draw.text((140, 195), f"Mode: {style}", fill=(203, 213, 225))

    y = 330
    draw.text((120, 300), "Enhanced Prompt", fill=(255, 255, 255))
    for line in wrap(enhanced_prompt, width=58)[:18]:
        draw.text((120, y), line, fill=(226, 232, 240))
        y += 34

    draw.rounded_rectangle((120, 830, 904, 900), radius=18, fill=(79, 70, 229))
    draw.text((370, 855), "AI model integration ready", fill=(255, 255, 255))

    filename = f"{uuid4().hex}.png"
    image.save(GENERATED_IMAGE_DIR / filename)
    return filename
