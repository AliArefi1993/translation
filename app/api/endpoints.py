from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.translation_service import TranslationService

router = APIRouter()

# Create an instance of TranslationService
translation_service = TranslationService()

class ASRInput(BaseModel):
    text: str

@router.post("/translate/")
async def translate_text(input: ASRInput):
    try:
        translated_text = translation_service.translate_text(input.text)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=f"Translation failed: {str(e)}")
    return {"translated_text": translated_text}


