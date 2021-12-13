from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from volleyball.forms import PlayerForm
from volleyball.models import Player, Category

def player_list(request:HttpRequest)->HttpResponse:
    category_qs = Category.objects.all()
    qs=Player.objects.all()
    query=request.GET.get("query","")
    category_id: str = request.GET.get("category_id", "")
    if category_id:
        qs = qs.filter(category__pk=category_id)

    if query: # 검색어가 있다면
        qs=qs.filter(name__icontains=query)
    return render(request,"volleyball/player_list.html",{
        "category_list": category_qs,
        "player_list":qs,
    })

def player_detail(request:HttpRequest,pk:int)->HttpResponse:
    player=get_object_or_404(Player,pk=pk)
    return render(request,"volleyball/player_detail.html",{
        "player":player,
    })

def player_new(request:HttpRequest)->HttpResponse:
    if request.method=="POST":
        form=PlayerForm(request.POST,request.FILES)
        if form.is_valid():
            saved_post=form.save()
        return redirect("volleyball:player_detail",saved_post.pk)
    else:
        form=PlayerForm()
    return render(request,"volleyball/player_form.html",{
        "form":form,
    })

def player_edit(request: HttpRequest, pk:int)->HttpResponse:
    player=get_object_or_404(Player,pk=pk)

    if request.method=="POST":
        form=PlayerForm(request.POST, request.FILES, instance=player)
        if form.is_valid():
            saved_player = form.save()
            return redirect("volleyball:player_detail",saved_player.pk)
    else:
        form=PlayerForm(instance=player)
    return render(request,"volleyball/player_form.html",{
        "form":form,
    })