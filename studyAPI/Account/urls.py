from django.urls import path, include
from .views import UserCreateAPIView, UserLoginAPIView
from rest_framework import routers

urlpatterns = [
    path('register', UserCreateAPIView.as_view()),
    path('login', UserLoginAPIView.as_view())
]
