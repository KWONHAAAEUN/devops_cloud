from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from blog.forms import PostForm
from blog.models import Post


def post_list(request: HttpRequest)->HttpResponse:
    post_qs=Post.objects.all()
    return render(request,"blog/post_list.html",{
        'post_list':post_qs,
    })

def post_detail(request:HttpRequest,pk:int)->HttpResponse:
    post=get_object_or_404(Post, pk=pk) # post에 pk에 맞는 값이 있으면 가져오고 아니면 404오류
    return render(request,"blog/post_detail.html",{
        "post":post,
    })

def post_new(request:HttpRequest)->HttpResponse:
    # request.method # "GET", "POST"
    if request.method=="POST": # POST의 로직이 많으니까 GET이 먼저 수행되기는 하지만 POST를 먼저 적어준다
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            saved_post=form.save()
            messages.success(request,"새로운 포스팅을 저장했씁니다")
            return redirect("blog:post_detail", saved_post.pk) # 저장된 saved_post는 pk값이 있으니 이동가능
    else:
        form=PostForm()
    return render(request,"blog/post_form.html",{
        "form":form,
    })

def post_edit(request:HttpRequest,pk:int)->HttpResponse:
    post = get_object_or_404(Post, pk=pk)
    if request.method=="POST":
        form = PostForm(request.POST, request.FILES,instance=post)
        if form.is_valid():
            saved_post=form.save()
            messages.success(request,f"#{pk}포스팅을 저장했습니다")
            return redirect("blog:post_detail", saved_post.pk)
    else:
        form=PostForm(instance=post)
    return render(request,"blog/post_form.html",{
        "form":form,
    })


def post_delete(request:HttpRequest,pk:int)->HttpResponse:
    post=get_object_or_404(Post, pk=pk)
    # GET 요청: 정말 삭제를 할 것인지, 한 번 더 물어봅니다
    # POST 요청: 삭제를 하고, 다른 주소로 이동을 시킵니다

    if request.method=="POST":
        post.delete() # 실제로 DB에 delete 쿼리를 실행
        messages.success(request,f"#{pk} 포스팅을 삭제했습니다")
        return redirect("blog:post_list")
    return render(request,"blog/post_confirm_delete.html",{
        "post":post,
    })