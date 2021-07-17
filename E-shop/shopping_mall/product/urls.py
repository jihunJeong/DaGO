from django.urls import path
from . import views

from django.conf.urls import url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.ProductList.as_view()),
    path('<str:name>/', views.ProductDetail.as_view()),
]