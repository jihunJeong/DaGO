from re import I
import os
from django.shortcuts import render
from django.views.generic import ListView, FormView, DetailView
from django.utils.decorators import method_decorator
from user.decorator import login_required, admin_required
from rest_framework import generics, mixins
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Item, PreAlso, ContentRecommend, Review, AsinId
from user.models import User
from django.core.exceptions import ObjectDoesNotExist
from recommend import usercontent
import time

# Create your views here.

class ProductList(ListView):
    template_name = "product/list.html"
    model = Item
    context_object_name = "products"

    def get_queryset(self):
        product_all = Item.objects.all().order_by('-enroll_date')
        page = int(self.request.GET.get('p',1))
        paginator = Paginator(product_all, 9)
        queryset = paginator.get_page(page)
        return queryset

def product_detail(request, pk):
    item = Item.objects.get(pk=pk)
    recommends = []
    try:
        user = User.objects.get(email=request.session.get('user'))
        reviewes = Review.objects.filter(reviewerid=user)
        if reviewes:
            recommend = usercontent.load_content(reviewes, AsinId.objects.filter(asin=item.asin).values_list('aid')[0], user, item, num=4)
        else :
            recommend = ContentRecommend.objects.get(asin=item.asin).recommend[1:-1].split(",")
    except ObjectDoesNotExist:
        recommend = ContentRecommend.objects.get(asin=item.asin).recommend[1:-1].split(",")
        pass
    cnt = 0
    for r in recommend:
        if r == item.asin:
            continue
        cnt += 1
        recommends.append(Item.objects.get(asin=r))
        if cnt == 4:
            break
    
    return render(
        request, 'product/detail.html', 
        {
            'p': item,
            'recommends' : recommends,
        }
    )