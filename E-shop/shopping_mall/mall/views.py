from django.http import request
from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Item
# Create your views here.

class MainView(TemplateView):
    template_name = "mall/home.html"
    model = Item
    ordering = '-pk'

class ProductDetail(TemplateView):
    template_name = 'mall/product_detail.html'
    model = Item
    
class ProductList(TemplateView):
    model = Item
    template_name = 'mall/product.html'

class ContactView(TemplateView):
    template_name = 'mall/contact.html'