from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from shop.forms import ReviewForm
from shop.mixins import ReviewUserCheckMixin
from shop.models import Shop, Category, Review


class ShopListView(ListView):
    model = Shop
    paginate_by = 2


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
    # 위 코드를 주석처리 한 이유는
    # 아래 valid에서 super로 부모 호출을 사용하지 않고
    # absolute url 설정해 준 것으로 return redirect(shop)를 받기 때문

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

class ReviewUdateView(LoginRequiredMixin, ReviewUserCheckMixin, UpdateView): # 다중 상속
    model=Review
    form_class=ReviewForm
    # success_url = reverse_lazy("shop:shop_list")

    # UserPassesTestMixin 부모 때문에 호출 가능
    # 참이면 UserPassesTestMixin 거짓 UpdateView
    # 유저가 같은지 테스트
    # def test_func(self):
    #     review=self.get_object()
    #     return self.request.user==review.user

    def get_success_url(self) -> str:
        review=self.object
        return resolve_url(review.shop)
    # resolve_url의 리턴 값을 문자열이고 HttpResponse를 요구하면 redirect

review_edit=ReviewUdateView.as_view()
