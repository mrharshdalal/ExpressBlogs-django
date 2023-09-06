from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('home', views.home, name="home"),
    path('login', views.loginUser, name="login"),
    path('logout', views.logoutUser, name="logout"),
    path('create/', views.create_blog_post, name='create'),
    path('blogs/', views.blog_list, name='blog_list'),

]