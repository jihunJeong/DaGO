from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('add/<product_id>/', views.add_cart, name='add_cart'),
    path('', views.cart_detail, name='cart_detail'),
    path('remove/<product_id>/', views.cart_remove, name='cart_remove'),
    path('delete/<product_id>/', views.cart_delete, name='cart_delete'),
]