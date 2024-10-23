from django.http import HttpResponse
from django.views import View


# def index(request):
#     return HttpResponse('article')


class IndexView(View):
    def get(self, request):
        return HttpResponse('Article')