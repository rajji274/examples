from django.contrib import admin
from django.urls import path
from application.views import index,view_data,login

urlpatterns = [
    # path('register/',register, name="register"),
    path('search/',index,name="search"),
    path('get_data/',view_data),
    # path('adduser/',adduser,name='adduser'),
    path('login/',login,name="login"),
    # path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',activate,name="activate"),
]
