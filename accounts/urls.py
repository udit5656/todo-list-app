from django.urls import path, include, reverse
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('index/', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
]

