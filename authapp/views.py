from django.shortcuts import render

def login(request):
    context = {'title': 'GeekShop - Авторизация'}
    return render(request, 'authapp/login.html', context)

# Create your views here.
