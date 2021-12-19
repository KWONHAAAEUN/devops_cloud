from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from ani.forms import CommentForm
from ani.mixins import CommentUserCheckMixin
from ani.models import Ani, Category, Comment


class AniListView(ListView):
    model=Ani
    paginate_by=5
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