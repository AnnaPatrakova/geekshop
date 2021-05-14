from django.shortcuts import HttpResponseRedirect

from mainapp.models import Product
from basketapp.models import Basket



def basket_add(request, product_id=None):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def basket_remove(request, id):
    Basket.objects.get(id=id).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


# Create your views here.
