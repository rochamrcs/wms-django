from django.urls import path
from .views import products, new_product

app_name = 'products'

urlpatterns = [
    path('', products, name='products'),
    path('new_product/', view=new_product, name='new_product')
]