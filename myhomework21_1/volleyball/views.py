from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from volleyball.forms import PlayerForm, CommentForm
from volleyball.models import Player, Category, Comment


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
    comment_list = player.comment_set.all()
    return render(request,"volleyball/player_detail.html",{
        "player":player,
        "comment_list": comment_list,
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

def comment_new(request,player_pk:int)->HttpResponse:
    player=Player.objects.get(pk=player_pk)
    if request.method=="POST":
        form=CommentForm(request.POST,request.FILES)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.player=player
            comment.save()
            return redirect("volleyball:player_detail",player_pk)
    else:
        form=CommentForm()
    return render(request,"volleyball/comment_form.html",{
        "form":form,
    })

def comment_edit(request,player_pk:int, pk:int)->HttpResponse:
    comment=get_object_or_404(Comment,pk=pk)
    if request.method=="POST":
        form=CommentForm(request.POST,request.FILES,instance=comment)
        if form.is_valid():
            form.save()
            return redirect("volleyball:player_detail",player_pk)
    else:
        form=CommentForm(instance=comment)
    return render(request,"volleyball/comment_form.html",{
        "form":form,
    })