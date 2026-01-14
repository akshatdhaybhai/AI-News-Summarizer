import streamlit as st
import requests

st.title("📰 AI News Summarizer & Sentiment Analyzer")

topic = st.text_input("Enter topic")

if st.button("Analyze"):
    response = requests.post(
        "http://127.0.0.1:8000/analyze",
        params={"topic": topic}
    ).json()

    st.subheader("Summary")
    st.write(response["summary"])

    st.subheader("Sentiment")
    st.write(response["sentiment"]["label"])

    st.audio("summary.mp3")
