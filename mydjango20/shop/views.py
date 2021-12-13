from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect, get_object_or_404

# /shop/new/
from shop.forms import ShopForm
from shop.models import Shop, Category


def shop_list(request: HttpRequest)->HttpResponse: # 장고가 뷰 함수에게 요구하는 형태
    category_qs=Category.objects.all() # 전체 조회
    qs=Shop.objects.all()# .order_by("-id") # -id 역순 정렬

    # category별로 검색하는 방법
    category_id:str=request.GET.get("category_id","")
    if category_id:
        qs=qs.filter(category__pk=category_id)

    query=request.GET.get("query","") # query값을 가져오고 없으면 빈문자열
    if query:
        qs=qs.filter(name__icontains=query)

    return render(request,"shop/shop_list.html",{
        "category_list":category_qs,
        "shop_list":qs, # qs를 shop_list안에 있는 것으로 사용
    })


def shop_new(request: HttpRequest)->HttpResponse:
    # raise NotImplementedError("곧 구현 예정")

    if request.method == "POST":
        form=ShopForm(request.POST,request.FILES)
        if form.is_valid():
            saved_post=form.save()
            # shop_detail 뷰를 구현했을 경우
            return redirect("shop:shop_detail", saved_post.pk)
    else:
        form=ShopForm()
    return render(request,"shop/shop_form.html",{
        "form":form,
    })

# /shop/100/
def shop_detail(request:HttpRequest,pk:int)->HttpResponse:
    shop=get_object_or_404(Shop,pk=pk)
    return  render(request,"shop/shop_detail.html",{
        "shop":shop,
    })
