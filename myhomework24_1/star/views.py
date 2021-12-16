from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from star.forms import KirbyForm
from star.models import Kirby

post_list=ListView.as_view(
    model=Kirby,
)

post_detail=DetailView.as_view(
    model=Kirby,
)

class PostCreateView(CreateView):
    model = Kirby
    form_class = KirbyForm

    def get_success_url(self):
        kirby_pk = self.object.pk
        return reverse("star:kirby_detail", args=[kirby_pk])
kirby_new=PostCreateView.as_view()

class PostUpdateView(UpdateView):
    model=Kirby
    form_class=KirbyForm
kirby_edit=PostUpdateView.as_view()

kirby_delete=DeleteView.as_view(
    model=Kirby,
    success_url=reverse_lazy("star:kirby_list"),
)