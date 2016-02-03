from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^articles/$', views.article_list, name='article_list'),
    url(r'^articles/new/$', views.article_new, name='article_new'),
    url(r'^articles/(?P<pk>\d+)/$', views.article_detail, name='article_detail'),
    url(r'^articles/(?P<pk>\d+)/edit/$', views.article_edit, name='article_edit'),
    url(r'^articles/(?P<pk>\d+)/delete/$', views.article_delete, name='article_delete'),
]

