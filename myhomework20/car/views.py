from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from car.forms import ReviewForm, ShopForm
from car.models import Shop, Review


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
        "shop_list":qs,
    })

def review_new(request, shop_pk:int)->HttpResponse:
    shop=Shop.objects.get(pk=shop_pk)
    if request.method=="POST":
        form=ReviewForm(request.POST,request.FILES)
        if form.is_valid():
            review=form.save(commit=False)
            review.shop=shop
            review.save()
            return redirect("car:shop_detail",shop_pk)
    else:
        form=ReviewForm()
    return render(request,"car/review_form.html",{
        "form":form,
    })

def review_edit(request, shop_pk:int, pk:int)->HttpResponse:
    review=get_object_or_404(Review,pk=pk)
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save()
            return redirect("car:shop_detail", shop_pk)
    else:
        form = ReviewForm(instance=review)
    return render(request,"car/review_form.html",{
        "form":form,
    })

def shop_new(request:HttpRequest)->HttpResponse:
    if request.method=="POST":
        form=ShopForm(request.POST,request.FILES)
        if form.is_valid():
            shop=form.save(commit=False)
            shop.save()
            messages.success(request,"성공적으로 저장했습니다")
            return redirect("car:shop_list")
    else:
        form=ShopForm()

    return render(request,"car/shop_form.html",{
        "form":form,
        })

def shop_edit(request:HttpRequest,pk:int)->HttpResponse:
    shop=get_object_or_404(Shop,pk=pk)
    if request.method=="POST":
        form=ShopForm(request.POST,request.FILES,instance=shop)
        if form.is_valid():
            form.save()
            messages.success(request,"성공적으로 수정했습니다")
            return redirect("car:shop_list")
    else:
        form=ShopForm(instance=shop)

    return render(request,"car/shop_form.html",{
        "form":form,
    })



