from django.contrib import admin
from django.urls import include, path
from .views import home_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home'),
    path('products/', include('products.urls')),
    path('auth/', include('accounts.urls'))
]
