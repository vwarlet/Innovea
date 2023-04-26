from django.shortcuts import render
from newsapi import NewsApiClient 


'''
    Para usar o 'everything' é necessário determinar alguns parâmetros (ex: assunto 'bitcoin')
    Como não foi estipulado que tipos de notícias devem ser exibidas
    Estou utilizando as últimas 50 notícias principais
'''
def home(request):
    newsapi = NewsApiClient(api_key='3b218e85618e4d8ba1b6f24b17e87586')
    top_headlines = newsapi.get_top_headlines(page_size=50)
    top_news = top_headlines['articles']
    # everything = newsapi.get_everything(q='bitcoin')
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
