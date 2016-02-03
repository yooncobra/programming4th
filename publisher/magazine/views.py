from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .models import Article, Comment
from .forms import ArticleForm, CommentForm


def index(request):
    recent_article_list = Article.objects.all().order_by('id')[:10]
    return render(request, 'magazine/index.html', {
        'recent_article_list': recent_article_list,
    })


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
            messages.success(request, '새 Article을 저장했습니다.')
            return redirect('magazine:article_list')
    else:
        form = ArticleForm()
    return render(request, 'form.html', {
        'form': form,
    })


@staff_member_required
def article_edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, 'Article을 수정했습니다.')
            return redirect(article)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'form.html', {
        'form': form,
    })


def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'magazine/article_detail.html', {
        'article': article,
        'comment_form': CommentForm(),
    })



@staff_member_required
def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article.delete()
        messages.success(request, 'Article 을 삭제했습니다.')
        return redirect('magazine:article_list')
    return render(request, 'magazine/article_confirm_delete.html', {
        'article': article,
    })


@login_required
def comment_new(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.author = request.user
            comment.save()
            messages.success(request, '새 Comment를 저장했습니다.')
            return redirect(article)
    else:
        form = CommentForm()
    return render(request, 'form.html', {
        'form': form,
    })


@login_required
def comment_edit(request, article_pk, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if comment.author != request.user:
        messages.warning(request, '댓글 작성자만 수정할 수 있습니다.')
        return redirect(comment.article)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Comment를 수정했습니다.')
            return redirect(comment.article)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'form.html', {
        'form': form,
    })


@staff_member_required
def comment_delete(request, article_pk, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if comment.author != request.user:
        messages.warning(request, '댓글 작성자만 삭제할 수 있습니다.')
        return redirect(comment.article)

    if request.method == 'POST':
        comment.delete()
        messages.success(request, 'Comment를 삭제했습니다.')
        return redirect(comment.article)
    return render(request, 'magazine/comment_confirm_delete.html', {
        'comment': comment,
    })

