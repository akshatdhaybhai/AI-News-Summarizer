import requests

API_KEY = "6468168931a6484993d3ab7a87bacacd"

def fetch_news(topic):
    url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={API_KEY}"
    response = requests.get(url).json()
    return response["articles"]
