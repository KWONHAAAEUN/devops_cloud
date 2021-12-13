from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404

from volleyball.models import Player


def player_list(request:HttpRequest)->HttpResponse:
    qs=Player.objects.all()
    return render(request,"volleyball/player_list.html",{
        "player_list":qs,
    })

def player_detail(request:HttpRequest,pk:int)->HttpResponse:
    player=get_object_or_404(Player,pk=pk)
    return render(request,"volleyball/player_detail.html",{
        "player":player,
    })