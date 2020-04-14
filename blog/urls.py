from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    path('', views.post_list, name = 'post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('login/', views.Account_login.as_view(), name='login'),
    path('create_account/',views.Create_account.as_view(), name='Create_account'),
    
    ]
