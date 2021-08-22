from django.shortcuts import render,redirect
from django.utils.decorators import method_decorator
from user.decorator import login_required
from django.views.generic import FormView,ListView
from django.db import transaction
from .forms import OrderForm
from product.models import Product
from product.models import Item
from .models import Order
from user.models import User
from django.core.paginator import Paginator

# Create your views here.
@method_decorator(login_required, name='dispatch')
class OrderCreate(FormView):
    form_class = OrderForm
    success_url = "/product/"

    def form_valid(self,form):
        with transaction.atomic():
            #product = Product.objects.get(pk=form.data.get("product"))
            #product = Item.objects.get(pk=form.data.get("product"))
            product = Item.objects.filter(asin=self.asin)
            print(product)
            user = User.objects.get(email=self.request.session.get('user'))
            order = Order(
                user=user,
                product=product.asin,
                quantity=int(form.data.get('quantity'))
            )
            order.save()
            product.save()
        return super().form_valid(form)

    #실패 했을 때, 어디로 redirect할 지 결정을 안했기 때문에 에러 발생.
    def form_invalid(self, form):
        #실패 했을 때의 작업.
        #form : <tr><th><label> .... </td></tr> 형태의 html코드를 가지고 있는 객체.
        #redirect하면 ProductDetail에서 OrderForm을 새로 생성하기 때문에 에러 메시지가 전달되지 않음.
        #return redirect('/product/'+ str(form.product))

        #product = Item.objects.get(pk=form.data.get('product'))
        product = Item.objects.filter(asin=self.asin)
        print(product)
        return render(self.request, 'product/detail.html', {'form': form, 'product':product})

@method_decorator(login_required, name='dispatch')
class OrderList(ListView):
    template_name = "order/list.html"
    context_object_name = "orders"
    def get_queryset(self, **kwargs):
        #user는 객체이므로, user 밑에 email과 비교를 원한다면 user__email 사용
        queryset = Order.objects.filter(user__email=self.request.session.get('user')).order_by('-id')
        page = int(self.request.GET.get('p',1))
        paginator = Paginator(queryset, 5)
        queryset = paginator.get_page(page)
        return queryset

# def order_detail(request, total = 0, counter = 0, order_items = None):
#     try:
#         order = Order.objects.get(order_id = OrderCreate(request))
#         order_items = OrderList.object.filter(order=order, active=True)
#         for order_item in order_items:
#             total += (order_item.product.price * order.quantity)
#             counter += order.quantity
#     except ObjectDoesNotExist:
#         pass
#
#     return render(request, 'order.html', dict(cart_items))

# def add_cart(request, product_pk):
#     product = Product.objects.get(pk=test_id)
#
#     try:
#         cart = CartItem.objects.get(product__id=product.pk, user__id=request.user.pk)
#         if cart:
#             if cart.product.name == product.name:
#                 cart.quantity += 1
#                 cart.save()
#     except CartItem.DoesNotExist:
#         user = User.objects.get(pk=request.user.pk)
#         cart = CartItem(
#             user=user,
#             product=product,
#             # 장바구니에 해당 상품이 없을 경우 int 1을 선언
#             quantity=1,
#         )
#         cart.save()
#     return redirect('product:my-cart')
#
# def minus_cart_item(request, product_pk):
#     cart_item = CartItem.objects.filter(product__id=product_pk)
#     product = Product.objects.get(pk=product_pk)
#     try:
#         for item in cart_item:
#             if item.product.name == product.name:
#                 if item.quantity > 1:
#                     item.quantity -= 1
#                     item.save()
#                 return redirect('product:my-cart')
#             else:
#                 return redirect('product:my-cart')
#     except CartItem.DoesNotExist:
#         raise Http404