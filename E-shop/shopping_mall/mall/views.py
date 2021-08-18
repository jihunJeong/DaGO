from django.http import request
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.base import TemplateResponseMixin
from django.core.paginator import Paginator

from .models import Item, CategoryBig
# Create your views here.

class MainView(ListView):
    template_name = "mall/home.html"
    paginate_by = 8
    context_object_name = 'items'

    def get_queryset(self) :
        return Item.objects.order_by('-enroll_date')[:64]

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context['categories'] = CategoryBig.objects.all()[1:]
        return context

def CategoryView(request, cats):
    return render(request, '')

# class ContactView(TemplateView):
    # template_name = 'mall/contact.html'
    # template_name = 'contact/contact.html'