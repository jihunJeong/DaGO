from django.shortcuts import render
from django.views.generic import ListView, FormView, DetailView
from django.utils.decorators import method_decorator
from user.decorator import login_required, admin_required
from .forms import RegisterForm
from order.forms import OrderForm
from .models import Product, TestItems
from .Serializers import ProductSerializer
from rest_framework import generics, mixins
from django.core.paginator import Paginator

# Create your views here.

class ProductList(ListView):
    template_name = "product/list.html"
    model = TestItems
    context_object_name = "products"

    def get_queryset(self):
        product_all = TestItems.objects.all()
        page = int(self.request.GET.get('p',1))
        paginator = Paginator(product_all, 9)
        queryset = paginator.get_page(page)
        return queryset

class ProductListAPI(generics.ListAPIView, mixins.ListModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    #ListModelMixin을 사용하면 get을 손쉽게 구현 가능.
    #CreateModelMixin을 사용하면 post를 손쉽게 구현 가능.
    #RetrieveModelMixin을 사용하면 상세보기를 손쉽게 구현 가능
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class ProductDetailAPI(generics.ListAPIView, mixins.RetrieveModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


@method_decorator(admin_required, name='dispatch')
class ProductRegister(FormView):
    template_name = "product/register.html"
    form_class = RegisterForm
    success_url = '/product/'

    def form_valid(self,form):
        product = Product(
            name=form.data.get('name'),
            price=form.data.get('price'),
            description=form.data.get('description'),
            stock = form.data.get('stock')
        )
        product.save()
        return super().form_valid(form)

class ProductDetail(DetailView):
    template_name = "product/detail.html"
    #queryset = Product.objects.all()
    model = Product
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        #생성된 context는 Template으로 전달됨.
        context = super().get_context_data(**kwargs)
        context['form']=OrderForm()
        return context