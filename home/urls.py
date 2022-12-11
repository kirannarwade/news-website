from django.contrib import admin
from django.urls import path
from home import views

from django.contrib.auth import views as auth_views
from home.forms import LoginForm

urlpatterns = [
    path('', views.home, name="home"),
    # path('login/', views.loginUser, name="loginuser"),
    path('register', views.CustomerRegistrationView.as_view(), name="registeruser"),
    path('contact/', views.contact, name="contact"),
    path('logout/', views.logoutUser, name="logout"),
    # path('login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name='loginUser'),
    path('login_user2/', auth_views.LoginView.as_view(template_name='login_user2.html', authentication_form=LoginForm), name='login_user2'),
    # path('login-user/', views.loginUser2, name="login-user")
 
]
