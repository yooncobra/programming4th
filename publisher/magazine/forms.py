from django import forms
from .models import Article, Comment


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('category', 'title', 'content')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('message',)
