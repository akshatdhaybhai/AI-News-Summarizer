from gtts import gTTS

def generate_audio(text):
    tts = gTTS(text)
    tts.save("summary.mp3")
