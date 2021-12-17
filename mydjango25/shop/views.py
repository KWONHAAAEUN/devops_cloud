from django.shortcuts import render
from django.views.generic import ListView

from shop.models import Shop, Category


class ShopListView(ListView):
    model = Shop

    # 부모의 get context date를 불러와서 저장
    def get_context_data(self, **kwargs):
        context_date=super().get_context_data(**kwargs)
        context_date["category_list"]=Category.objects.all()
        return context_date

shop_list=ShopListView.as_view()