from django.urls import path, include
from django.contrib import admin
from .views import ProductAPI, UserAPI, OrdersAPI, myAPI


urlpatterns = [
    path('products/', ProductAPI.as_view()),
    path('users/', UserAPI.as_view()),
    path('orders/', OrdersAPI.as_view()),
    path('my/', myAPI.as_view()),
]