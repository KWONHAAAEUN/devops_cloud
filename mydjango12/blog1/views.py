from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from blog1.models import Post

def index(request):
    return render(request,"blog1/index.html")

def post_list(request: HttpRequest) -> HttpResponse:
    request.GET #QueryString Values
    request.POST #Post 요청 Values
    request.FILES #Post 요청에서 파일 Values

    qs=Post.objects.all() #QuerySet Type
    #return render(request,"blog1/post_list.html",{})
    # blog1/templates/blog1/post_list.html
    qs = qs.order_by("-pk")

    q = request.GET.get("q", "")
    if q:
        qs = qs.filter(title__icontains=q)

    return render(request,"blog1/post_list.html",{
                  "post_list":qs,})


def post_detail(request: HttpRequest, pk: int) -> HttpResponse:

    # pk=1
    post=Post.objects.get(pk=pk)
    return render(request,"blog1/post_detail.html",{
        "post":post,
    })
