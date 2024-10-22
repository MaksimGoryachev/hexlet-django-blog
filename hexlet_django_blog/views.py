from django.shortcuts import render


def index(request):
    return render(request, 'index.html', context={'who': 'World'})


def about(request):
    return render(request, 'about.html', context={'tags': ['Python', 'C+', 'PHP']})


def base(request):
    return render(request, 'base.html')