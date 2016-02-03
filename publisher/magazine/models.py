from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    udpated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    category = models.ForeignKey(Category)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    udpated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('magazine:article_detail', args=[self.pk])


class Comment(models.Model):
    article = models.ForeignKey(Article)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    udpated_at = models.DateTimeField(auto_now=True)

