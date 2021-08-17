from django.http import request
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.base import TemplateResponseMixin
from django.core.paginator import Paginator

from .models import Item, CategoryBig
# Create your views here.

class MainView(ListView):
    template_name = "mall/home.html"
    model = Item
    ordering = '-enroll_date'
    context_object_name = 'items'
    paginate_by = 8

# class ContactView(TemplateView):
    # template_name = 'mall/contact.html'
    # template_name = 'contact/contact.html'