from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from star.forms import KirbyForm, ReviewForm
from star.models import Kirby

kirby_list=ListView.as_view(
    model=Kirby,
)

kirby_detail=DetailView.as_view(
    model=Kirby,
)

kirby_new = CreateView.as_view(
    model=Kirby,
    form_class=KirbyForm,
    success_url=reverse_lazy("star:kirby_list"),
)

kirby_edit = UpdateView.as_view(
    model=Kirby,
    form_class=KirbyForm,
    success_url=reverse_lazy("star:kirby_list"),
)

kirby_delete=DeleteView.as_view(
    model=Kirby,
    success_url=reverse_lazy("star:kirby_list"),
)

review_new=CreateView.as_view(
    model=Kirby,
    form_class=ReviewForm,
)

review_edit=CreateView.as_view(
    model=Kirby,
    form_class=ReviewForm,
    success_url=reverse_lazy("star:kirby_list"),
)

review_delete=CreateView.as_view(
    model=Kirby,
    success_url=reverse_lazy("star:kirby_list"),
)
