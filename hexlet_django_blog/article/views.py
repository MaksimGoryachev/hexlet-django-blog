from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.urls import reverse
from django.shortcuts import render

from .models import Article

# def index(request):
#     return HttpResponse('article')


class IndexView(View):
    def get(self,request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'articles/index.html', {'articles': articles})

    def get1(self, request):
        # return HttpResponse('Articles')
        tags = request.GET.get('tags', 'python')  # По умолчанию 'python'
        article_id = request.GET.get('article_id', 42)  # По умолчанию 42
        # Используем reverse для получения URL
        url = reverse('article', args=[tags, article_id])
        return HttpResponseRedirect(url)

def get_tags(request, tags, article_id):
    return HttpResponse(f'Статья номер {article_id}. Тег {tags}')
