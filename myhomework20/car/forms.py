from django import forms
from car.models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields=["author_name","message"]