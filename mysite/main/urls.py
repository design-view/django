from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('',index),
    # path('', views.index, name='index'),
    path('notice',notice),
    path('notice/<int:pk>',noticeView, name="noticeView"),
    path('notice/remove/<int:pk>',notice_remove),
    path('notice/add/', notice_add)
]