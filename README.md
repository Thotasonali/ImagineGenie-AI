# ImagineGenie AI

ImagineGenie AI is a full-stack AI creative platform foundation built with React, TypeScript, FastAPI, SQLite, and Python.

This is **Part 1 MVP** of a production-style flagship project for AI Engineer, Backend Engineer, and Software Engineer portfolios.

## Features in Part 1

- React + TypeScript frontend
- FastAPI backend
- SQLite database
- Prompt enhancement service
- Image generation workflow
- Local image storage
- Generation history
- Delete history item
- Professional UI
- GitHub-ready structure

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | React, TypeScript, Vite, Axios |
| Backend | FastAPI, SQLAlchemy, Pydantic |
| Database | SQLite |
| Image Processing | Pillow |
| Future AI | Stable Diffusion / Hugging Face / Replicate |

## Project Structure

```text
visionforge-ai/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── db/
│   │   ├── models/
│   │   ├── schemas/
│   │   └── services/
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── services/
│   │   └── types/
│   └── package.json
├── docs/
└── README.md
```

## Run Backend

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

API docs:

```text
http://127.0.0.1:8000/docs
```

## Run Frontend

Open a second terminal:

```bash
cd frontend
npm install
npm run dev
```

Frontend URL:

```text
http://localhost:5173
```

## Roadmap

### Part 2
- User authentication
- JWT login/register
- Protected dashboard

### Part 3
- Real AI image generation
- Hugging Face / Replicate integration
- Image download

### Part 4
- Background removal
- Upscaling
- Semantic search

### Part 5
- Docker
- PostgreSQL
- Redis
- Celery workers

### Part 6
- CI/CD
- Deployment
- Tests

## Resume Bullet

Built ImagineGenie AI, a full-stack generative AI creative platform using React, TypeScript, FastAPI, SQLAlchemy, and SQLite, implementing prompt enhancement, image generation workflow, persistent history, local image storage, and a scalable architecture for future AI model integration.
