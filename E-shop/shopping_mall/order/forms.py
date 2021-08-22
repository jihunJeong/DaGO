from django import forms
from user.models import User
from product.models import Item
from .models import Order

class OrderForm(forms.Form):
    quantity = forms.IntegerField(
        error_messages={
            'required':'수량을 입력해주세요.'
        }, label="수량")
    product = forms.CharField(
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
            #product = Item.objects.get(pk=product)
            product = Item.objects.get(asin=self.asin)
            if quantity < 0:
                self.add_error('quantity', '0개 이하는 주문할 수 없습니다.')
        else:
            self.add_error('quantity', '주문 수량을 확인해주세요.')