
from django.shortcuts import render

from menu_app.models import Menu


def index(request):
    menus = Menu.objects.filter(title='some-coup')
    return render(request, 'index.html', {'menus': menus})
