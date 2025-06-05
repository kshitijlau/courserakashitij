from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ..services.question_generator import generate_questions

router = APIRouter()

class QuestionRequest(BaseModel):
    role: str
    skills: list[str]

@router.post('/questions')
def create_questions(payload: QuestionRequest):
    try:
        questions = generate_questions(payload.role, payload.skills)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"questions": questions}
