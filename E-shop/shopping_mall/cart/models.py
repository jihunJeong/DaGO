from django.db import models
from user.models import User
from product.models import Item
from user.models import User
import random
# Create your models here.
class MfRecommend(models.Model):
    recommend_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    recommend = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mf_recommend'

class Cart(models.Model):
    # cart_id = models.CharField(max_length=250, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'Cart'
        ordering = ['date_added']

    def __str__(self):
        #return self.cart_id
        return (str(self.user) + ' ' + str(self.cart_id))

    def get_mf_recommend(self):
        user = User.objects.get(email_id=self.user.email_id)
        recommend = MfRecommend.objects.get(user_id=user).recommend[1:-1].split(",")
        recommends = []
        cnt = 0
        for r in recommend:
            cnt += 1
            recommends.append(Item.objects.get(asin=r))
            if cnt == 5:
                break

        return recommends

class CartItem(models.Model):
    product = models.ForeignKey(Item, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    # 수량은 -1 과 같은 수량이 없기 때문에 아래의 필드로 선언하여 최소값을 1 로 설정
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'CartItem'

    def sub_total(self):
        return round(float(self.product.price) * self.quantity, 2)

    def __str__(self):
        return self.product
