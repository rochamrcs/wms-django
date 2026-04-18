from django.urls import path
from .views import products, new_product, change_status

app_name = 'products'

urlpatterns = [
    path('', products, name='products'),
    path('new_product/', view=new_product, name='new_product'),
    path('<int:pk>/change_status/', view=change_status, name='change_status'),
]