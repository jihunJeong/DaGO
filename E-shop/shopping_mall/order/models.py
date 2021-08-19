from django.db import models

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name="구매자")
    product = models.ForeignKey('product.Item', on_delete=models.CASCADE, verbose_name="상품")
    quantity = models.IntegerField(verbose_name = "수량")
    reg_date = models.DateTimeField(auto_now_add=True, verbose_name="구매일자")
    def __str__(self):
        return (str(self.user) + ' ' + str(self.product))

    class Meta:
        db_table = 'orders'
        verbose_name = "주문"
        verbose_name_plural = "주문"


    # def total(self):
    #     #return sum([item.product.price for item in self.orders.all()])
    #     return sum([item.product.test_id for item in self.product.all()])
# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     product = models.ForeignKey('product.TestItems', on_delete=models.CASCADE, verbose_name="상품")
#     quantity = models.IntegerField(verbose_name = "수량")
#
#     def __str__(self):
#         return '{}'.format(self.id)
#
#     def get_cost(self):
#         return self.price * self.quantity

# class Brand(models.Model):
#     brand_id = models.IntegerField(primary_key=True)
#     brand_name = models.CharField(db_column='brand name',
#                                   max_length=20)  # Field renamed to remove unsuitable characters.
#     nation = models.CharField(max_length=20)
#
#     class Meta:
#         managed = False
#         db_table = 'brand'
#
#
# class Bucket(models.Model):
#     bucket_id = models.IntegerField(primary_key=True)
#     buy = models.ForeignKey('Buy', models.DO_NOTHING)
#     eamil = models.ForeignKey('Email', models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'bucket'
#
#
# class Buy(models.Model):
#     buy_id = models.IntegerField(primary_key=True)
#     item = models.ForeignKey('Item', models.DO_NOTHING)
#     account = models.IntegerField()
#     email = models.ForeignKey('Email', models.DO_NOTHING)
#     price = models.FloatField()
#
#     class Meta:
#         managed = False
#         db_table = 'buy'
#
#
# class Category(models.Model):
#     category_id = models.IntegerField(primary_key=True)
#     category_name = models.CharField(db_column='category name',
#                                      max_length=20)  # Field renamed to remove unsuitable characters.
#
#     class Meta:
#         managed = False
#         db_table = 'category'
#
#
# class Credit(models.Model):
#     credit_id = models.IntegerField(primary_key=True)
#     account = models.CharField(max_length=20)
#     bank = models.CharField(max_length=20)
#     email = models.ForeignKey('Email', models.DO_NOTHING)
#     card = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'credit'
#
#
# class Email(models.Model):
#     email_id = models.IntegerField(primary_key=True)
#     e_mail = models.CharField(db_column='e-mail', max_length=20)  # Field renamed to remove unsuitable characters.
#     password = models.CharField(max_length=20)
#     contact = models.IntegerField()
#     enroll_date = models.DateField(db_column='enroll date')  # Field renamed to remove unsuitable characters.
#     address = models.CharField(max_length=50)
#     nickname = models.CharField(max_length=20, blank=True, null=True)
#     rule_id = models.IntegerField()
#     credit = models.ForeignKey(Credit, models.DO_NOTHING, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'email'
#
#
# class Item(models.Model):
#     name = models.CharField(max_length=20)
#     item_id = models.IntegerField(primary_key=True)
#     price = models.FloatField()
#     enroll_date = models.DateField(db_column='enroll date')  # Field renamed to remove unsuitable characters.
#     category_id = models.ForeignKey(Category, models.DO_NOTHING,
#                                     db_column='category id')  # Field renamed to remove unsuitable characters.
#     image_link = models.CharField(db_column='image link',
#                                   max_length=50)  # Field renamed to remove unsuitable characters.
#     brand = models.ForeignKey(Brand, models.DO_NOTHING, blank=True, null=True)
#     nickname = models.CharField(max_length=20, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'item'
#
#
# class Review(models.Model):
#     review_id = models.IntegerField(primary_key=True)
#     item = models.ForeignKey(Item, models.DO_NOTHING)
#     email = models.ForeignKey(Email, models.DO_NOTHING)
#     score = models.IntegerField()
#     text = models.CharField(max_length=500)
#
#     class Meta:
#         managed = False
#         db_table = 'review'
#
# 
# class Transaction(models.Model):
#     transaction_id = models.IntegerField(primary_key=True)
#     also_buy = models.CharField(db_column='also buy', max_length=50)  # Field renamed to remove unsuitable characters.
#     also_view = models.CharField(db_column='also view', max_length=50)  # Field renamed to remove unsuitable characters.
#     email = models.ForeignKey(Email, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'transaction'
