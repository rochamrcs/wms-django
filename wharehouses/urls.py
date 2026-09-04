from django.urls import path

from .views import locations, new_location

app_name = 'wharehouses'

urlpatterns = [
    path('', locations, name='locations'),
    path('new_location', view=new_location, name='new_location')
]
