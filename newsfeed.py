import requests
import os
from datetime import date, timedelta
import json

def create_payload():

    news_key = os.environ["NEWSFEED_KEY"]
    disease = 'OPMD'
    # need to not hardcode
    month = date.today() - timedelta(days = 28)
    payload = {'q': disease, 'from': month,'apiKey': news_key,'sortBy': 'relevancy','pageSize': '30'}
# 
    return payload


def news_results():

    payload = create_payload()

    news_search = requests.get('https://newsapi.org/v2/everything', params = payload )
    news_result = news_search.json()
    articles = news_result['articles']

    all_articles=[]
    for i in range(len(articles)):
        news_source = news_result['articles'][i].get('source').get('name')
        author = news_result['articles'][i].get('author')
        title = news_result['articles'][i].get('title')
        description = news_result['articles'][i].get('description')
        url = news_result['articles'][i].get('url')
        urlimage = news_result['articles'][i].get('urlToImage')

        article = {"news_source": news_source, "author": author, "title": title, "description": description, "url": url, "urlimage": urlimage}
        all_articles.append(article)

    articles = {"related_articles": all_articles}

    return json.dumps(articles)
   