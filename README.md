# AI-Assisted Interviewer Platform

This repository contains a minimal backend skeleton for an AI-assisted interviewer application. The backend is built with **FastAPI** and exposes an endpoint for generating interview questions using **OpenAI GPT-4**.

## Getting Started

1. Install dependencies:
   ```bash
   pip install -r backend/requirements.txt
   ```

2. Set your OpenAI API key in the environment variable `OPENAI_API_KEY`.

3. Run the server:
   ```bash
   uvicorn backend.app.main:app --reload
   ```

### API Endpoint

`POST /api/questions`

Request body:
```json
{
  "role": "Frontend Engineer",
  "skills": ["React", "JavaScript"]
}
```

Response contains a list of generated questions.

See `guide.txt` for the full specification document.
