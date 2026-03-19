from django import forms
from products.models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ["product_code", "name", "umb", "product_type"]