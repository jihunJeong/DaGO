from django.http import request
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.base import TemplateResponseMixin
from django.core.paginator import Paginator

from .models import Item, TestItems
# Create your views here.

class MainView(ListView):
    template_name = "mall/home.html"
    model = TestItems
    context_object_name = 'items'

    def get_queryset(self):
        product_all = TestItems.objects.all()
        page = int(self.request.GET.get('p',1))
        paginator = Paginator(product_all, 8)
        queryset = paginator.get_page(page)
        return queryset
    
class ContactView(TemplateView):
    template_name = 'mall/contact.html'