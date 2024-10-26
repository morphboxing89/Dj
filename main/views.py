from django.http import HttpResponse
from django.shortcuts import render


def index(request) -> HttpResponse:
    context: dict = {
        'title': 'Home',
        'content': 'Главная страница магазина Мебель от moRph-а',
        'list': ['first', 'second'],
        'dict': {'first': 1},
        'is_authenticated': False
    }
    return render(request, 'main/index.html', context)


def about(request) -> HttpResponse:
    return HttpResponse('About page')
