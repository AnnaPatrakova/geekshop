from django.shortcuts import render
import os
import json

module_dir = os.path.dirname(__file__)


def index(request):
    context = {'title': 'GeekShop'}
    return render(request, 'mainapp/index.html', context)


def products(request):
    file_path = os.path.join(module_dir, 'fixtures/products.json')
    products = json.load(open(file_path, encoding='utf-8'))
    context = {'title': 'GeekShop - Каталог',
             'products': products }

    return render(request, 'mainapp/products.html', context)









