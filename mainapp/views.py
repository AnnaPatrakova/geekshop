from django.shortcuts import render


def index(request):
    context = {'title': 'GeekShop'}
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {'title': 'GeekShop - Каталог'}
    return render(request, 'mainapp/products.html', context)

def test_context(request):
    context = {
        'title': 'Text Context',
        'header': 'Добро пожаловать на сайт!',
        'username': 'Иван Иванов',
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': 6090.00},
            {'name': 'Синяя куртка The North Face', 'price': 23725.00},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': 3390.00},
            {'name': 'Черный рюкзак Nike Heritage', 'price': 2340.00},
            {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex', 'price': 13590.00},
            {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN', 'price': 2890.00},

        ],

    }
    return render(request, 'mainapp/test_context.html', context)






