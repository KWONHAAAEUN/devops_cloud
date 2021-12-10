from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404

from diary.forms import PostForm, CommentForm
from diary.models import Post, Comment

from django.contrib import messages

def tag_detail(request: HttpRequest, tag_name:str)->HttpResponse:
    qs=Post.objects.all()
    qs=qs.filter(tag_set__name=tag_name)
    return render(request,"diary/tag_detail.html",{
        "tag_name": tag_name,
        "post_list":qs,
    })

def post_list(request: HttpRequest)->HttpResponse:
    qs=Post.objects.all() # 전체 포스팅 목록을 얻어올 준!비!
    query=request.GET.get("query","")
    if query: # 검색어가 있다면
        qs=qs.filter(title__icontains=query)

    return render(request,"diary/post_list.html",{
        "post_list":qs,
    })

def post_detail(request:HttpRequest, pk:int) -> HttpResponse:
    post=get_object_or_404(Post, pk=pk)
    # try:
    #     post=Post.objects.get(pk=pk)
    # except Post.DoesNotExist:
    #     raise Http404 # 예외는 return이 아니라 raise로 해야함

    comment_list=post.comment_set.all()
    tag_list=post.tag_set.all()
    return render(request,"diary/post_detail.html",{
        "post":post,
        "comment_list":comment_list,
        "tag_list":tag_list,
    })

def post_new(request: HttpRequest) -> HttpResponse:
    # if request.method == "GET" # 빈서식
    #     form=PostForm()
    # else: # 입력 값을 전달받아 유효성 검사->저장
    #     form = PostForm(request.POST,request.FILES)

    # form.save(!!!2 전체 작성 후 commit=False)
    # !!!2 post.ip=request.META["REMOTE_ADDR"]
    if request.method=="POST":
        form=PostForm(request.POST,request.FILES)
        if form.is_valid(): # 관심있어하는 모든 것의 유효성을 검사하는데 하나라도 실패시 실패
            # form.cleaned.data
            post=form.save(commit=False)
            post.ip=request.META["REMOTE_ADDR"]
            post.save()
            messages.success(request,"성공적으로 저장했습니다.")
            return redirect("diary:post_list")
    else:
        form=PostForm()

    return render(request, "diary/post_form.html", {
        "form": form,
    })

def post_edit(request: HttpRequest, pk:int) -> HttpResponse:
    # 아래 코드는 ModelForm에 한해서 동작하는 코드
    post=Post.objects.get(pk=pk)
    if request.method=="POST":
        form=PostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            form.save()
            messages.success(request,"성공적으로 수정했습니다")
            return redirect("diary:post_list")
    else:
        form=PostForm(instance=post)

    return render(request, "diary/post_form.html", {
        "form": form,
    })

# /diary/100/comments/new/
def comment_new(request, post_pk:int)->HttpResponse:
    post=Post.objects.get(pk=post_pk)
    if request.method == "POST":
        form=CommentForm(request.POST, request.FILES)
        if form.is_valid():
            # form.cleaned_data # 유효성 검사에 통과한 값을 dict
            comment=form.save(commit=False)
            # comment.post_id=post_pk #FK를 직접 채우진 않는다
            comment.post=post
            comment.save()
            return redirect("diary:post_detail",post_pk)
    else:
        form=CommentForm()
    return render(request,"diary/comment_form.html",{
        "form":form,
    })
# /diary/100/comments/20/edit/
# pk는 수정할 인자=2번째 인자
def comment_edit(request, post_pk:int, pk:int)->HttpResponse:
    comment=get_object_or_404(Comment,pk=pk)
    form=CommentForm(instance=comment)
    return render(request,"diary/comment_form.html",{
        "form":form,
    })