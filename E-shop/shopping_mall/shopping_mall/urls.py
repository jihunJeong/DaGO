"""shopping_mall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from user.views import index, logout, RegisterView,LoginView
from product.views import(
    ProductList,ProductRegister, ProductDetail,
    ProductListAPI, ProductDetailAPI
)

from order.views import OrderCreate,OrderList
from mall.views import MainView

from contact import views as contact_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mall.urls')),
    path('product/', include('product.urls')),
    path('logout/', logout),
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('order/', OrderList.as_view()),
    path('order/create/', OrderCreate.as_view()),

    path('api/product', ProductListAPI.as_view()),
    path('api/product/<int:pk>', ProductDetailAPI.as_view()),

    path('contact/', contact_views.contact_view, name='contact'),

    path('cart/', include('cart.urls')),
]
    
