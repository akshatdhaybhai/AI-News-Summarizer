from fastapi import FastAPI
from .scraper import fetch_news
from .summarizer import summarize_text
from .sentiment import analyze_sentiment
from .tts import generate_audio

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI News Summarizer API"}

@app.post("/analyze")
def analyze(topic: str):
    articles = fetch_news(topic)
    content = articles[0]["content"]
    summary = summarize_text(content)
    sentiment = analyze_sentiment(summary)
    generate_audio(summary)

    return {
        "summary": summary,
        "sentiment": sentiment
    }
