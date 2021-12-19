
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from ani.forms import CommentForm, AniForm
from ani.mixins import CommentUserCheckMixin
from ani.models import Ani, Category, Comment


class AniListView(ListView):
    model=Ani
    paginate_by=5

    def get_queryset(self):
        qs=super().get_queryset()

        query=self.request.GET.get("query","")
        if query:
            qs=qs.filter(name__icontains=query)

        return qs

    def get_context_data(self,**kwargs):
        context_date=super().get_context_data(**kwargs)
        context_date["category_list"]=Category.objects.all()
        return context_date

ani_list=AniListView.as_view()

ani_detail=DetailView.as_view(
    model=Ani,
)

class CommentCreateView(LoginRequiredMixin,CreateView):
    model=Comment
    form_class=CommentForm

    def form_valid(self, form)->HttpResponse:
        ani_pk=self.kwargs["ani_pk"]
        ani=get_object_or_404(Ani,pk=ani_pk)

        comment=form.save(commit=False)
        comment.ani=ani
        comment.user=self.request.user
        comment.save()

        return redirect(ani)

comment_new=CommentCreateView.as_view()



class CommentUdateView(LoginRequiredMixin, CommentUserCheckMixin, UpdateView): # 다중 상속
    model=Comment
    form_class=CommentForm
    # success_url = reverse_lazy("ani:ani_list")
    #
    # def test_func(self):
    #     commnet=self.get_object()
    #     return self.request.user==comment.user

    def get_success_url(self)->str:
        comment=self.object
        return resolve_url(comment.ani)

comment_edit=CommentUdateView.as_view()

comment_delete=DeleteView.as_view(
    model=Ani,
    success_url=reverse_lazy("ani:ani_list")
)

class AniCreateView(CreateView):
    model = Ani
    form_class=AniForm

    def get_success_url(self):
        ani_pk=self.object.pk
        return reverse("ani:ani_detail",args=[ani_pk])

ani_new=AniCreateView.as_view()


class AniUpdateView(UpdateView):
    model=Ani
    form_class=AniForm
ani_edit=AniUpdateView.as_view()

ani_delete=DeleteView.as_view(
    model=Ani,
    success_url=reverse_lazy("ani:ani_list"),
)