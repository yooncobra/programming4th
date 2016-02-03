from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^articles/$', views.article_list, name='article_list'),
    url(r'^articles/new/$', views.article_new, name='article_new'),
    url(r'^articles/(?P<pk>\d+)/$', views.article_detail, name='article_detail'),
    url(r'^articles/(?P<pk>\d+)/edit/$', views.article_edit, name='article_edit'),
    url(r'^articles/(?P<pk>\d+)/delete/$', views.article_delete, name='article_delete'),
    url(r'^articles/(?P<article_pk>\d+)/comments/new/$', views.comment_new, name='comment_new'),
    url(r'^articles/(?P<article_pk>\d+)/comments/(?P<pk>\d+)/edit/$', views.comment_edit, name='comment_edit'),
    url(r'^articles/(?P<article_pk>\d+)/comments/(?P<pk>\d+)/delete/$', views.comment_delete, name='comment_delete'),
]

