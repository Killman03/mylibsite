from django.shortcuts import render
from django.http import HttpResponse


menu_name = [
    {'title': 'Главная', 'url_name': 'home'},
    {'title': 'Встречи', 'url_name': 'meetings'},
    {'title': 'Библиотека', 'url_name': 'library'},
    {'title': 'Контакты', 'url_name': 'contacts'},
             ]


def index(request):
    context = {
        'menu_name': menu_name,
    }
    return render(request, 'home/index.html', context=context)

def meetings(request):
    context = {
        'menu_name': menu_name,
    }
    return HttpResponse(request, 'hi')

def contacts(request):
    context = {
        'menu_name': menu_name,
    }
    return HttpResponse(request, 'hi')

# Create your views here.
