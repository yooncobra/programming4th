from django.shortcuts import render
from .models import Article


def index(request):
    return render(request, 'magazine/index.html')


def article_list(request):
    article_list = Article.objects.all()
    return render(request, 'magazine/article_list.html', {
        'article_list': article_list,
    })

