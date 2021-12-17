from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from shop.forms import ReviewForm
from shop.models import Shop, Category, Review


class ShopListView(ListView):
    model = Shop

    # 부모의 get context date를 불러와서 저장
    def get_context_data(self, **kwargs):
        context_date = super().get_context_data(**kwargs)
        context_date["category_list"] = Category.objects.all()
        return context_date


shop_list = ShopListView.as_view()

shop_detail = DetailView.as_view(
    model=Shop,
)


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    # success_url = reverse_lazy("shop:shop_list")

    # 유효성 검사에 통과한다면 ..
    def form_valid(self, form) -> HttpResponse:
        # self.kwargs:URL Captured 값들이 사전으로 저장
        shop_pk = self.kwargs["shop_pk"]
        shop = get_object_or_404(Shop, pk=shop_pk)

        review = form.save(commit=False)
        review.shop = shop
        review.user = self.request.user
        review.save()
        # return redirect("shop:shop_detail",shop.pk)
        return redirect(shop)

review_new = ReviewCreateView.as_view()

review_edit=UpdateView.as_view(
    model=Review,
    form_class=ReviewForm,
    success_url = reverse_lazy("shop:shop_list")
)
