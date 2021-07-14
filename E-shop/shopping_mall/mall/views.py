from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class MainView(TemplateView):
    template_name = "mall/home.html"

class ProductView(TemplateView):
    template_name = 'mall/product.html'

class ContactView(TemplateView):
    template_name = 'mall/contact.html'