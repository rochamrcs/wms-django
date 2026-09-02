from django.urls import path

from .views import locations

app_name = 'wharehouses'

urlpatterns = [
    path('', locations, name='locations'),
]
