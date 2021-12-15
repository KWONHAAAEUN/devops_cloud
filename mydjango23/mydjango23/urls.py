from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    # FIXME: 아래의 url 설정은 blog 기능 구현 후에 pattern_name으로 변경 예정
    path('', RedirectView.as_view(url='/blog/'), name='root'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]