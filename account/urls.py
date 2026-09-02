from django.urls import path
from . import views as v

urlpatterns = [
    path('',v.home),
    path('signup',v.signup),
    path('login',v.login),
    path('logout',v.logout_user),
    path('adduser',v.CreateUser.as_view(),name='adduser'),
    path('loginuser',v.LoginUser.as_view(),name='loginuser'),
]
