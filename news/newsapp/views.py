from django.shortcuts import render
from newsapi import NewsApiClient 


def home(request):
    newsapi = NewsApiClient(api_key='3b218e85618e4d8ba1b6f24b17e87586')
    top_headlines = newsapi.get_top_headlines()
    # everything = newsapi.get_everything()

    top_news = top_headlines['articles']
    # top_news = everything['articles']

    title = []
    desc = []
    url = []
    author = []

    for i in range(len(top_news)):
        news = top_news[i]

        author.append(news['author'])
        title.append(news['title'])
        desc.append(news['description'])
        url.append(news['url'])

    all_news = zip(author, title, desc, url)

    context = {
        'all_news': all_news
    }

    return render(request, "index.html", context)
