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
    '''
        Note: 처음으로 쇼핑몰 접근 시 볼 수 있는 대문페이지
            사용자에게 모든 상품을 등록 최신 순으로 노출
    '''
    template_name = "mall/home.html"
    paginate_by = 8
    context_object_name = 'items'

    def get_queryset(self) :
        return Item.objects.order_by('-enroll_date')[:64] # Filtering by Enroll date

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context['categories'] = CategoryBig.objects.all()[1:]
        return context

def category_page(request, name):
    '''
        Note: 메인에 있는 Category NavBar에서 대분류 Category 선택시
            Category에 해당하는 상품만 등록 최신 순으로 노출
    '''
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
    '''
        Note: 제품을 검색할 시 Search
    '''
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

