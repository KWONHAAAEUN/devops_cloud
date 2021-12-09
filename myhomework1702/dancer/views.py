from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from dancer.models import Post

def post_list(request: HttpRequest)->HttpResponse:
    qs=Post.objects.all() # 전체 포스팅 목록을 얻어올 준!비!
    query = request.GET.get("query", "")
    if query:  # 검색어가 있다면
        qs = qs.filter(team_name__icontains=query)
    return render(request,'dancer/post_list.html',{
        "post_list":qs,
    })

def post_detail(request: HttpRequest, pk:int)->HttpResponse:
    post=Post.objects.get(pk=pk)
    comment_list=post.comment_set.all()
    tag_list=post.tag_set.all()

    return render(request,"dancer/post_detail.html",{
        "post":post,
        "comment_list": comment_list,
        "tag_list": tag_list,
    })

def tag_detail(request: HttpRequest, tag_name:str)->HttpResponse:
    qs=Post.objects.all()
    qs=qs.filter(tag_set__name=tag_name)
    return render(request,"dancer/tag_detail.html",{
        "tag_name": tag_name,
        "post_list":qs,
    })