from django.shortcuts import render
from django.views.generic.base import TemplateView



def index(request):
    return render(request, 'index.html', context={'who': 'World'})


def about(request):
    return render(request, 'about.html', context={'tags': ['Python', 'C+', 'PHP']})


# def base(request):
#     return render(request, 'base.html')


class BaseView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['who'] = 'World'
        return context
