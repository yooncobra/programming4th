from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100, help_text='포스팅 제목을 100자 이내로 써주세요.')
    content = models.TextField()
    photo = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
