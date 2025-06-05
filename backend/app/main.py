from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api import question

app = FastAPI(title="AI Interview App")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(question.router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "AI-Assisted Interviewer Backend"}
