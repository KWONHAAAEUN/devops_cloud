from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404

from car.models import Shop

def shop_list(request:HttpRequest)->HttpResponse:
    qs=Shop.objects.all()
    query = request.GET.get("query", "")
    if query:  # 검색어가 있다면
        qs = qs.filter(name__icontains=query)
    return render(request,"car/shop_list.html",{
        "shop_list":qs,
    })

def shop_detail(request:HttpRequest,pk:int)->HttpResponse:
    shop=get_object_or_404(Shop,pk=pk)
    tag_list=shop.tag_set.all()
    review_list = shop.review_set.all()
    return render(request,"car/shop_detail.html",{
        "shop":shop,
        "tag_list":tag_list,
        "review_list": review_list,
    })

def tag_detail(request:HttpRequest,tag_name:str)->HttpResponse:
    qs=Shop.objects.all()
    qs=qs.filter(tag_set__name=tag_name)
    return render(request,"car/tag_detail.html",{
        "tag_name": tag_name,
        "post_list":qs,
    })

