# Class Based View(CBV)
# -뷰 함수를 만들어주는 클래스
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.forms import PostForm
from blog.models import Post

post_list=ListView.as_view(
    model=Post,
)
post_detail=DetailView.as_view(
    model=Post,
)

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    # success_url = reverse_lazy("blog:post_list")

    # 가변적인 상황을 가능하게 함
    def get_success_url(self):
        # self.object # 저장된 모델 인스턴스
        post_pk=self.object.pk

        # URL Reverse 지원하는 함수 in django
        # 리턴값 문자열
        return reverse("blog:post_detail",args=[post_pk])
        # return resolve_url("blog:post_detail",post_pk)
        # 리턴값 HttpResponse
        # return redirect("blog:post_detail",post_pk)
        # 리턴값 문자열
        # {% url "blo:post_detail" post_pk %}

post_new=PostCreateView.as_view()

class PostUpdateView(UpdateView):
    model=Post
    form_class=PostForm

    # def get_success_url(self):
    #     post_pk=self.object.pk
    #     return reverse("blog:post_detail",args=[post_pk])
post_edit=PostUpdateView.as_view(
    # model=Post,
    # form_class=PostForm,
    # TODO: 가변적으로 URL을 지정할 수 없다.
    # TODO: URL Reverse가 미적용
    # success_url="/blog/",
    # success_url="blog:post_list", # URL Reverse 미지원

    # 완성된 URL Reverse를 지정해줘야한다
    # url reverse를 하려면 프로젝트 로딩 이후에 할 수 있다
    # 근데 이것은 로딩 전에 부른느 것이기 때문에 작동되지 않는 것이고
    # success_url=reverse("blog:post_list")
    # lazy는 url이 필요할 때 가져와서 사용한다
    # success_url=reverse_lazy("blog:post_list"),
)

post_delete=DeleteView.as_view(
    model=Post,
    success_url=reverse_lazy("blog:post_list"),
)