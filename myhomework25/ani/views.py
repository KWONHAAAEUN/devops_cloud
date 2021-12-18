from django.shortcuts import render
from django.views.generic import ListView

from ani.models import Ani

ani_list=ListView.as_view(
    model=Ani,
)