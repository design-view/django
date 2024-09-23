from django.contrib import admin
from django.urls import path
from .views import *
# from . import views

urlpatterns = [
    path('', index),
    # path('', views.index, name='index'),
    path('notice/',notice),
    path('notice/<int:pk>',notice_view),
    path('notice/add/',notice_add),
    path('notice/remove/<int:pk>', notice_remove),
]