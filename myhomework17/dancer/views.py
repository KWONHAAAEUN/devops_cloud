from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from dancer.models import Post


def post_list(request:HttpRequest) -> HttpResponse:
    qs=Post.objects.all()
    query=request.GET.get("query","")
    if query:
        qs=qs.filter(team_name__icontains=query)
    return render(request,'dancer/post_list.html',{
        "post_list":qs,
    })
def post_detail(request:HttpRequest, pk:int)->HttpResponse:
    post=Post.objects.get(pk=pk)
    tag_list=post.tag_set.all()
    comment_list=post.comment_set.all()
    return render(request,"dancer/post_detail.html",{
        "post":post,
        "tag_list":tag_list,
        "comment_list":comment_list,
    })

def tag_detail(request:HttpRequest,tag_name:str)->HttpResponse:
    qs=Post.objects.all()
    qs=qs.filter(tag_set__name=tag_name)
    return render(request,'dancer/tag_detail.html',{
        "tag_name":tag_name,
        "post_list":qs,
    })