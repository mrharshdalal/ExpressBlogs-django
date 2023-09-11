from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name="blog_list"),
    path('home', views.home, name="home"),
    path('login', views.loginUser, name="login"),
    path('logout', views.logoutUser, name="logout"),
    path('create/', views.create_blog_post, name='create'),
    path('blogs/', views.blog_list, name='blog_list'),
    path('search/', views.search_results, name='search_results'),
    path('like/<int:blog_post_id>/', views.like_blog_post, name='like_blog_post'),
    path('trending/', views.trending_blogs, name='trending_blogs'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),



]