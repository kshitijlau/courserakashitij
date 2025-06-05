import os
from typing import List
import openai

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

def generate_questions(role: str, skills: List[str]) -> List[str]:
    """Generate interview questions using OpenAI GPT-4."""
    prompt = (
        f"Generate 5 interview questions for the role {role} "
        f"covering skills {', '.join(skills)}."
    )
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
    )
    content = response.choices[0].message["content"]
    questions = [q.strip() for q in content.split('\n') if q.strip()]
    return questions
