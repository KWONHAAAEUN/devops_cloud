from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from bread.models import Shop

def shop_list(request: HttpRequest) -> HttpResponse:
    qs=Shop.objects.all()
    context_data={
        "shop_list":qs,
        }
    return  render(request,"bread/shop_list.html",context_data)

def shop_detail(request: HttpRequest, pk:int) -> HttpResponse:
    shop=Shop.objects.get(pk=pk)
    context_data={
        "shop":shop,
    }
    return render(request,"bread/shop_detail.html",context_data)
