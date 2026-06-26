# VisionForge AI Part 1 Setup

## 1. Move folder to your projects directory

```bash
cd ~/Desktop/projects
```

Put the extracted `VisionForgeAI-Part1` folder here or rename it to `visionforge-ai`.

## 2. Start backend

```bash
cd ~/Desktop/projects/visionforge-ai/backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## 3. Start frontend

Open a second terminal:

```bash
cd ~/Desktop/projects/visionforge-ai/frontend
npm install
npm run dev
```

## 4. Open app

```text
http://localhost:5173
```

## 5. Push to GitHub

```bash
cd ~/Desktop/projects/visionforge-ai
git init
git add .
git commit -m "Initial commit: VisionForge AI Part 1"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/visionforge-ai.git
git push -u origin main
```
