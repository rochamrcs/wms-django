from django import forms
from products.models import Product


class ProductForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            classes = self.fields[field].widget.attrs.get("class", "")

            if self[field].errors:
                classes += " border border-red-500 bg-red-50"
            else:
                classes += " border border-gray-200"

            self.fields[field].widget.attrs["class"] = classes

    class Meta:
        model = Product
        fields = ["product_code", "name", "umb", "product_type"]

        widgets = {
            "product_code": forms.TextInput(attrs={
                "class": "w-full p-3 rounded-lg bg-gray-100 text-sm text-gray-800 placeholder-gray-400",
                "placeholder": "ex: PRF-001"
            }),
            "name": forms.TextInput(attrs={
                "class": "w-full p-3 rounded-lg bg-gray-100 text-sm text-gray-800",
                "placeholder": "ex: Parafuso Sextavado M8"
            }),
            "umb": forms.Select(attrs={
                "class": "w-full p-3 rounded-lg bg-gray-100 text-sm text-gray-800 cursor-pointer"
            }),
            "product_type": forms.Select(attrs={
                "class": "w-full p-3 rounded-lg bg-gray-100 text-sm text-gray-800 cursor-pointer"
            }),
        }