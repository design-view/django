from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('main',views.index, name='main'),
    path('blog/',views.blog, name='blog'),
    # URL:80/blog/숫자로 접속하면 게시글-세부페이지(posting)
    path('blog/<int:pk>',views.posting, name="posting"),
    path('blog/new_post/', views.new_post, name='new_post'),
    path('blog/<int:pk>/remove', views.remove_post, name='remove_post')
]
# 이미지 출력을 위한 url설정 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)