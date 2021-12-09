from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from diary.forms import PostForm
from diary.models import Post

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
    post=Post.objects.get(pk=pk)
    comment_list=post.comment_set.all()
    tag_list=post.tag_set.all()
    return render(request,"diary/post_detail.html",{
        "post":post,
        "comment_list":comment_list,
        "tag_list":tag_list,
    })

def post_new(request: HttpRequest) -> HttpResponse:
    #    print("request.method:", request.method)
    #    print("request.GET:", request.GET)
    #    print("request.POST:", request.POST)
    #    print("request.FILES:", request.FILES)

    # 입력 서식을 보여주겠다.
    if request.method == "GET":
        form = PostForm()
    # 서식 입력값을 전달받아서, 유효성 검사를 하겠다.
    # -> 에러상황 : 에러 메시지를 보여주겠다.
    # -> 유효성 검사에 통과하면, 입력값을 보여주고, post_list로 이동
    else:
        form = PostForm(request.POST, request.FILES)  # request.POST에 넘기기
        if form.is_valid():  # 통과를 한다면?
            print("유효성 검사에 통과했습니다. :", form.cleaned_data)
            form.save() # ModelForm에서만 지원
            return redirect("diary:post_list")
            # 통과하면 출력하고 이동하는 것.
        else:  # 통과하지 않으면 ?
            pass  # 아무것도 안하고 pass!!!


    return render(request, "diary/post_form.html", {
        "form": form,  # form을 넘기기
    })  # _form.html도 하나의 약속!
