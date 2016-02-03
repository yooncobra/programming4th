from django.conf.urls import url
from django.contrib.auth.views import login
from . import views


urlpatterns = [
    url(r'^login/$', login, name='login', kwargs={
        'template_name': 'form.html',
    }),
    url(r'^profile/$', views.profile, name='profile'),
]

