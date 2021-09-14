from django.urls import path
from . import views

from django.conf.urls import url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.MainView.as_view()), # 대문 페이지
    path('category/<str:name>/', views.category_page) # Home Page에서 Category 클릭시
]