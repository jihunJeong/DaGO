from django.shortcuts import render
from django.views.generic import ListView, FormView, DetailView
from django.utils.decorators import method_decorator
from user.decorator import login_required, admin_required
# from .forms import RegisterForm
from order.forms import OrderForm
# from .Serializers import ProductSerializer
from rest_framework import generics, mixins
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Item, PreAlso, ContentRecommend, Review
from user.models import User
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

class ProductList(ListView):
    template_name = "product/list.html"
    model = Item
    context_object_name = "products"

    def get_queryset(self):
        product_all = Item.objects.all()
        page = int(self.request.GET.get('p',1))
        paginator = Paginator(product_all, 9)
        queryset = paginator.get_page(page)
        return queryset

def product_detail(request, pk):
    item = Item.objects.get(pk=pk)
    try:
        user = User.objects.get(email=request.session.get('user'))
        reviewes = Review.objects.filter(reviewerid=user)
        if reviewes:
            print("Yes")
            recommend = ContentRecommend.objects.get(asin=item.asin).recommend[1:-1].split(",")
            recommends = list(Item.objects.filter(asin__in=recommend))[:4]
        else :
            recommend = ContentRecommend.objects.get(asin=item.asin).recommend[1:-1].split(",")
            recommends = list(Item.objects.filter(asin__in=recommend))[:4]
    except ObjectDoesNotExist:
        recommend = ContentRecommend.objects.get(asin=item.asin).recommend[1:-1].split(",")
        recommends = list(Item.objects.filter(asin__in=recommend))[:4]
        pass

    return render(
        request, 'product/detail.html', 
        {
            'p': item,
            'recommends' : recommends,
        }
    )
'''
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
'''