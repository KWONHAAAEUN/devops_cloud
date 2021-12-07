from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from diary.models import Post

def post_list(request: HttpRequest)->HttpResponse:
    qs=Post.objects.all() # 전체 포스팅 목록을 얻어올 준!비!
    query=request.GET.get("query","")
    if query: # 검색어가 있다면
        qs=qs.filter(title__icontains=query)

    return render(request,"diary/post_list.html",{
        "post_list":qs,
    })

def post_detail(request:HttpRequest, pk:int) -> HttpResponse:
    post=Post.objects.get(pk=pk)
    comment_list=post.comment_set.all()
    tag_list=post.tag_set.all()
    return render(request,"diary/post_detail.html",{
        "post":post,
        "comment_list":comment_list,
        "tag_list":tag_list,
    })