from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('add/<product_id>/', views.add_cart, name='add_cart'),
    path('', views.cart_detail, name='cart_detail')
]