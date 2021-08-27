from django.core import paginator
from django.http import request
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.base import TemplateResponseMixin
from django.core.paginator import Paginator

from .models import CategoryBig, CategoryMid
from product.models import Item

from .forms import PostSearchForm
from django.db.models import Q
from django.views.generic import FormView

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
    
def category_page(request, name):
    category = CategoryBig.objects.get(name=name)
    items = Item.objects.filter(cb = category.cb_id).order_by('-enroll_date')[:64]
    paginator = Paginator(items, 8)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(
        request, 'mall/home.html',
        {
            'items' : posts,
            'categories' : CategoryBig.objects.all()[1:],
            'category' : category,
            'page_obj' : posts,
        }
    )
class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = 'mall/post_search.html'


    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']
        post_list = Item.objects.filter(Q(title__icontains=searchWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = post_list

        return render(self.request, self.template_name, context)

