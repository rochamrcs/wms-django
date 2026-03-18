from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_code', 'name', 'umb', 'status', 'product_type', 'quantity', 'created_at']
    search_fields = ['product_code', 'name']
    list_filter = ['status', 'umb', 'product_type']

admin.site.register(Product, ProductAdmin)