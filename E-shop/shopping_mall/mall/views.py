from django.http import request
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.base import TemplateResponseMixin

from .models import Item, TestItems
# Create your views here.

class MainView(ListView):
    template_name = "mall/home.html"
    model = TestItems
    context_object_name = 'items'
    
class ContactView(TemplateView):
    template_name = 'mall/contact.html'