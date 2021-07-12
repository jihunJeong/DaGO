from django import forms
from user.models import User
from product.models import Product
from .models import Order


class OrderForm(forms.Form):
    quantity = forms.IntegerField(
        error_messages={
            'required':'수량을 입력해주세요.'
        }, label="수량")
    product = forms.IntegerField(
        error_messages={
            'required':'상품을 선택해주세요.'
        },
    label="상품", widget=forms.HiddenInput
    )

    def clean(self):

        cleaned_data = super().clean()
        quantity = cleaned_data.get('quantity')
        product = cleaned_data.get('product')

        if quantity and product:
            product = Product.objects.get(pk=product)
            if product.stock < quantity:
                self.add_error('quantity', '재고보다 많은 주문은 할 수 없습니다.')
                return
            if quantity < 0:
                self.add_error('quantity', '0개 이하는 주문할 수 없습니다.')
        else:
            self.add_error('quantity', '주문 수량을 확인해주세요.')