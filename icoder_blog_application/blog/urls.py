from django.urls import path
from blog import views

urlpatterns = [
    # Api to post comments:
    path('postcomment/', views.Post_comment,name='postcomment'),
    path('', views.blog_home,name='blog_home'),
    path('post/<str:slug>/', views.blog_post,name='blog_post'),
]