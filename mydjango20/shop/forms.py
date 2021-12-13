from django import forms
from shop.models import Shop

class ShopForm(forms.ModelForm):
    tags=forms.CharField()
    class Meta:
        model=Shop
        fields=[
            "category",
            "name",
            "description",
            "telephone",
        ]