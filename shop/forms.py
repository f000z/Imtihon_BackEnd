from django import forms
from shop.models import Furniture


class FurnitureForm(forms.ModelForm):
    class Meta:
        model = Furniture
        fields = ['name', 'image', 'price']

