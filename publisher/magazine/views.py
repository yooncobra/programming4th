from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import redirect, render
from .models import Article
from .forms import ArticleForm


def index(request):
    return render(request, 'magazine/index.html')


def article_list(request):
    article_list = Article.objects.all()
    return render(request, 'magazine/article_list.html', {
        'article_list': article_list,
    })


@staff_member_required
def article_new(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('magazine:article_list')
    else:
        form = ArticleForm()
    return render(request, 'form.html', {
        'form': form,
    })

