from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from diary.models import Post

def post_list(request: HttpRequest)->HttpResponse:
    qs=Post.objects.all() # 전체 포스팅 목록을 얻어올 준!비!
    return render(request,"diary/post_list.html",{
        "post_list":qs,
    })