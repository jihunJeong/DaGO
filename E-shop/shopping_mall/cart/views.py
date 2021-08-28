from django.shortcuts import render, redirect, get_object_or_404
from product.models import Item
from user.models import User
from .models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
# def _cart_id(request):
#     #cart = request.session.session_key
#     user = User.objects.get(email=request.session.get('user'))
#     cart = Cart.objects.get(user=user)
#     if not cart:
#         cart = request.session.create()
#     return cart

def add_cart(request, product_id):
    product = Item.objects.get(asin=product_id)
    try:
        user = User.objects.get(email=request.session.get('user'))
        #cart = Cart.objects.get(cart_id=_cart_id(request), user=user)
        cart = Cart.objects.get(user=user)
    except Cart.DoesNotExist:
        user = User.objects.get(email=request.session.get('user'))
        cart = Cart.objects.create(
            user = user,
            # cart_id = _cart_id(request)
        )
        cart.save()

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product = product,
            quantity = 1,
            cart = cart
        )
        cart_item.save()
    #return render(request, 'product/list.html')
    return redirect('cart:cart_detail')

def cart_detail(request, total=0, counter=0, cart_items=None):
    try:
        user = User.objects.get(email=request.session.get('user'))
        # cart = Cart.objects.get(cart_id=_cart_id(request), user=user)
        cart = Cart.objects.get(user=user)
        cart_items = CartItem.objects.filter(cart=cart, active=True)
        for cart_item in cart_items:
            total += (float(cart_item.product.price) * cart_item.quantity)
            counter += cart_item.quantity
    except ObjectDoesNotExist:
        pass

    if counter > 0:
        total += 5

    try:
        return render(request, 'cart/cart.html', dict(cart_items = cart_items, total=round(total,2), counter=counter, cart=cart))
    except:
        return render(request, 'cart/cart.html', dict(cart_items = cart_items, total=round(total,2), counter=counter))

def cart_remove(request, product_id):
    user = User.objects.get(email=request.session.get('user'))
    # cart = Cart.objects.get(cart_id = _cart_id(request), user=user)
    cart = Cart.objects.get(user=user)
    product = get_object_or_404(Item, asin=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart:cart_detail')

def cart_delete(request, product_id):
    user = User.objects.get(email=request.session.get('user'))
    cart = Cart.objects.get(user=user)
    product = get_object_or_404(Item, asin=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if cart_item.quantity:
        cart_item.delete()

    return redirect('cart:cart_detail')