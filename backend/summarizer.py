from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text):
    if len(text) > 1024:
        text = text[:1024]
    summary = summarizer(text, max_length=150, min_length=50)
    return summary[0]["summary_text"]
