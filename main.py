from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from test import EmotionAnalysis
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
emotion_analyzer = EmotionAnalysis()

class TranscriptRequest(BaseModel):
    text: str

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/analyze")
async def analyze_transcript(transcript: TranscriptRequest):
    try:
        output = emotion_analyzer.analyze(transcript.text)
        emotion_analyzer.extract(output)
    except Exception as e:
        return {"error": str(e)}
    if output and hasattr(output, 'content'):

        lines = output.content.split("\n")
        result = {}
        for line in lines:
            if ":" in line:
                key, value = line.split(":", 1)
                result[key.strip()] = value.strip()
        return result
    return {"error": "Analysis failed"}