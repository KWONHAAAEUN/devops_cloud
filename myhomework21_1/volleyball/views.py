from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404

from volleyball.models import Player

def tag_detail(request: HttpRequest, tag_name:str)->HttpResponse:
    qs=Player.objects.all()
    qs=qs.filter(tag_set__name=tag_name)
    return render(request,"volleyball/tag_detail.html",{
        "tag_name": tag_name,
        "player_list":qs,
    })

def player_list(request:HttpRequest)->HttpResponse:
    qs=Player.objects.all()
    query=request.GET.get("query","")
    if query: # 검색어가 있다면
        qs=qs.filter(name__icontains=query)
    return render(request,"volleyball/player_list.html",{
        "player_list":qs,
    })

def player_detail(request:HttpRequest,pk:int)->HttpResponse:
    player=get_object_or_404(Player,pk=pk)
    return render(request,"volleyball/player_detail.html",{
        "player":player,
    })