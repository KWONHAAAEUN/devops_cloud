from django import forms
from car.models import Review, Shop


class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields=["author_name","message"]

class ShopForm(forms.ModelForm):
    class Meta:
        model=Shop
        fields=[
            "name",
            "type",
            "option",
            "cost",
            "photo",
            "tag_set",
        ]