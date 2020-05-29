from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.mypage, name = 'mypage'),
    path('blog/detail/<int:pk>', views.guide_detail, name="guide_detail"),
    path('blog/new', views.guide_new, name='guide_new'),
    path('blog/create', views.create, name='create'),
    path('blog/edit/<int:pk>', views.guide_edit, name='guide_edit'),
    path('blog/update/<int:pk>', views.guide_update, name='guide_update'),
    path('blog/delete/<int:pk>', views.guide_delete, name="guide_delete"),
    path('blog/search', views.search, name='search'),
    path('blog/result', views.result, name='result'),
] 
