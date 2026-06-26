STYLE_PRESETS = {
    "realistic": "photorealistic, natural lighting, high-detail textures",
    "cinematic": "cinematic lighting, dramatic composition, film-grade color grading",
    "anime": "anime style, clean line art, expressive character design",
    "digital art": "digital painting, concept art, rich colors, sharp details",
    "3D render": "3D render, studio lighting, octane render style",
    "logo design": "minimal logo design, vector-like, clean branding, modern typography",
    "marketing banner": "advertising banner, commercial layout, bold visual hierarchy",
}

def enhance_prompt(prompt: str, style: str) -> str:
    clean_prompt = prompt.strip()
    style_detail = STYLE_PRESETS.get(style, STYLE_PRESETS["realistic"])
    return (
        f"{clean_prompt}. Style: {style_detail}. "
        "Ultra detailed, professional composition, high resolution, sharp focus, "
        "balanced colors, polished commercial quality."
    )
