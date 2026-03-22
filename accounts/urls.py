from django.urls import path
from .views import login_view, logout_view

app_name = 'accounts'

urlpatterns = [
    path('', login_view, name='login_form'),
    path('logout/', logout_view, name='logout_form')
]