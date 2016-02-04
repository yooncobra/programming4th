import os
import sys
from django.conf.urls import url
from django.http import HttpResponse
os.environ.setdefault('DJANGO_SETTINGS_MODULE', __name__)

'''How to run

python micro_django.py runserver
'''

DEBUG = True
SECRET_KEY = 'foo'
ROOT_URLCONF = __name__

urlpatterns = []


def route(pattern, *pattern_args, **pattern_kwargs):
    def wrap_fn(view_fn):
        urlpatterns.append(url(pattern, view_fn, *pattern_args, **pattern_kwargs))
        def wrap(request, *args, **kwargs):
            return view_fn(request, *args, **kwargs)
        return wrap
    return wrap_fn


@route(r'^$')
def index(request):
    return HttpResponse('Hello World')


@route(r'^(?P<name>\w+)/$')
def hello(request, name):
    return HttpResponse('Hello, {}'.format(name))


if __name__ == '__main__':
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

