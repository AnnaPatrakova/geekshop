from django.urls import path

from basketapp.views import basket_add

app_name = 'basketapp'

urlpatterns = [
    path('add/<int:product_id>/', basket_add, name='basket_add'),
]