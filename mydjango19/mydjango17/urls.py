from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include

# TODO: 편의상 여기에 root를 구현하지만,
# 차후 RedirectView CBV를 써서 이 구현을 제거할 예정
# 최상위 페이지로 가면 바로 post_list로 이동하도록 설정
def root(request):
    return redirect("diary:post_list")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('diary/',include('diary.urls')),
    path('',root,name="root"),
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)

# 디버그 툴바의 urls
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path("__debug__/",include(debug_toolbar.urls)),
    ]