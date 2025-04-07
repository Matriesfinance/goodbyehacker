import requests

def get_google_news():
    url = "https://newsapi.org/v2/top-headlines"
    params = {'sources': 'google-news', 'apiKey': 'your-newsapi-key'}
    response = requests.get(url, params=params)
    data = response.json()
    articles = data.get("articles", [])
    news_titles = [article['title'] for article in articles]
    return news_titles
