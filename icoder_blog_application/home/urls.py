'''
        Home.urls
'''
from django.urls import path
from home import views

urlpatterns = [
    path('', views.home_page,name='home'),
    path('about/', views.about_page,name='about'),
    path('contact/', views.contact_page,name='contact'),
    path('search/', views.search,name='search'),
    path('signup/', views.signup_form,name='signup'),
    path('login/', views.login_form,name='login'),
    path('logout/', views.logout_user,name='logout'),
]