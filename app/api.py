from fastapi import APIRouter, UploadFile, File, Form
from app.utils.file_reader import extract_text_from_file
from app.services.text_processing import preprocess_text
from app.services.ai_service import analyze_email
from app.schemas.email_schema import EmailTextRequest

router = APIRouter(prefix="/api")

@router.post("/analyze-email/json")
def analyze_email_json(payload: EmailTextRequest):
    clean_text = preprocess_text(payload.text)
    result = analyze_email(clean_text)
    return result

@router.post("/analyze-email/file")
async def analyze_email_file(
    file: UploadFile = File(...)
):
    content = extract_text_from_file(file)
    clean_text = preprocess_text(content)
    result = analyze_email(clean_text)
    return result
