from django import forms
from wharehouses.models import Location


class LocationForm(forms.ModelForm):

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
        model = Location
        fields = ["address", "storage", "capacity", "capacity_unit", "location_type"]

        widgets = {
            "address": forms.TextInput(attrs={
                "class": "w-full p-3 rounded-lg bg-gray-100 text-sm text-gray-800 placeholder-gray-400",
                "placeholder": "ex: POS001"
            }),
            "storage": forms.Select(attrs={
                "class": "w-full p-3 rounded-lg bg-gray-100 text-sm text-gray-800 cursor-pointer"
            }),
            "capacity": forms.NumberInput(attrs={
                "class": "w-full p-3 rounded-lg bg-gray-100 text-sm text-gray-800"
            }),
            "capacity_unit": forms.Select(attrs={
                "class": "w-full p-3 rounded-lg bg-gray-100 text-sm text-gray-800 cursor-pointer"
            }),
            "location_type": forms.Select(attrs={
                "class": "w-full p-3 rounded-lg bg-gray-100 text-sm text-gray-800 cursor-pointer"
            }),
        }