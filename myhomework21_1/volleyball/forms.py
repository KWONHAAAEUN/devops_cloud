from django import forms
from volleyball.models import Player

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = [
            "category",
            "name",
            "photo",
            "team",
            "position",
            "description",
            "tag_set",
        ]