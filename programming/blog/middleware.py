from django.db.models.query import QuerySet
from django.http import JsonResponse


class JsonResponseMiddleware(object):
    def process_response(self, request, response):
        if isinstance(response, QuerySet):
            queryset = response
            mylist = []
            for instance in queryset:
                mylist.append(instance.as_dict())
            return JsonResponse(mylist, safe=False)
        return response
