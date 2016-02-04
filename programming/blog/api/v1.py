from django.conf.urls import url
from django.http import JsonResponse
from blog.models import Post


def post_list(request):
    return Post.objects.all()


urlpatterns = [
    url(r'^posts/$', post_list),
]
