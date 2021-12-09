from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from dancer.models import Post


def post_list(request: HttpRequest)->HttpResponse:
    qs=Post.objects.all()
    query = request.GET.get("query", "")
    if query:  # 검색어가 있다면
        qs = qs.filter(team_name__icontains=query)
    return render(request,'dancer/post_list.html',{
        "post_list":qs,
    })

def post_detail(request: HttpRequest, pk:int)->HttpResponse:
    post=Post.objects.get(pk=pk)
    return render(request,"dancer/post_detail.html",{
        "post":post,
    })
