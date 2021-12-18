from django.shortcuts import render
from django.views.generic import ListView, DetailView

from ani.models import Ani, Category


class AniListView(ListView):
    model=Ani

    def get_context_data(self,**kwargs):
        context_date=super().get_context_data(**kwargs)
        context_date["category_list"]=Category.objects.all()
        return context_date

ani_list=AniListView.as_view()

ani_detail=DetailView.as_view(
    model=Ani,
)