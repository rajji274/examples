from django.contrib import admin
from django.urls import path,include
from .views import UserRegisterView,UserFetch,UserLogin
urlpatterns = [
    path('register/',UserRegisterView.as_view()),
    path('get/<int:pk>/',UserFetch.as_view()),
    path('login/',UserLogin.as_view()),
    
]