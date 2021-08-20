from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=64, verbose_name ="상품명")
    price = models.IntegerField(verbose_name="가격")
    description = models.TextField(verbose_name="설명")
    stock = models.IntegerField(verbose_name="재고")
    reg_date = models.DateTimeField(auto_now_add=True, verbose_name = "등록시간")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "products"
        verbose_name="상품"
        verbose_name_plural = "상품"

class TestItems(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    test_id = models.AutoField(primary_key=True)
    brand_name = models.CharField(max_length=100, blank=True, null=True)
    categories = models.CharField(max_length=1000, blank=True, null=True)
    image_link = models.CharField(db_column='image link', max_length=2500, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    nickname = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_items'
        verbose_name="테스트상품"
        verbose_name_plural = "테스트상품"
        
    def get_absolute_url(self):
        return f"/product/{self.pk}/"

    def __str__(self):
        return f'{self.brand_name} {self.nickname}'


class CategoryBig(models.Model):
    cb_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'category_big'
        verbose_name_plural = "big_categories"

    def __str__(self):
        return self.name

class CategoryMid(models.Model):
    cm_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300, blank=True, null=True)
    cb = models.ForeignKey(CategoryBig, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category_mid'


class CategorySm(models.Model):
    cs_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    cm = models.ForeignKey(CategoryMid, models.DO_NOTHING, blank=True, null=True)
    cb = models.ForeignKey(CategoryBig, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category_sm'

class Brand(models.Model):
    brand_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'brand'
        
class Item(models.Model):
    asin = models.CharField(primary_key=True, max_length=100)
    price = models.FloatField(blank=True, null=True)
    enroll_date = models.DateField(blank=True, null=True)
    imagelink = models.TextField(db_column='imageLink', blank=True, null=True)  # Field name made lowercase.
    brand = models.ForeignKey(Brand, models.DO_NOTHING, blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    feature = models.TextField(blank=True, null=True)
    imagehighres = models.TextField(db_column='imageHighRes', blank=True, null=True)  # Field name made lowercase.
    cb = models.ForeignKey(CategoryBig, models.DO_NOTHING, blank=True, null=True)
    cm = models.ForeignKey(CategoryMid, models.DO_NOTHING, blank=True, null=True)
    cs = models.ForeignKey(CategorySm, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item'


    def get_absolute_url(self):
        return f'/product/{self.pk}/'

    def get_image_link(self):
        imagelink = None
        if self.imagehighres:
            imagelink = self.imagehighres[1:-1].split(',')[0]
        return imagelink
    
    def __str__(self):
        return self.title

    def get_category(self):
        category = self.cb.name
        if self.cm.name != "None" and self.cm.name != "Extra":
            category += " > " + self.cm.name
        if self.cs.name != "None" and self.cs.name != "Extra":
            category += " > " + self.cs.name
        return category

    def get_brand(self):
        return self.brand.name
    
    def get_feature(self):
        return self.feature[1:-1]

    def get_also_view(self):
        item = Item.objects.get(pk=self.asin)
        also_asin = PreAlso.objects.get(asin=item.asin)
        
        also_view = []
        if also_asin.also_view:
            temp = also_asin.also_view[1:-1].split(",")
            also_view.extend(temp)
        if also_asin.also_buy:
            temp = also_asin.also_buy[1:-1].split(",")
            also_view.extend(temp)
        items = list(Item.objects.filter(asin__in=also_view))[:4]
        return items

    def get_recommend(self):
        item = Item.objects.get(pk=self.asin)
        recommend = ContentRecommend.objects.get(asin=item.asin).recommend[1:-1].split(",")
        recommends = list(Item.objects.filter(asin__in=recommend))[:4]
        return recommends


class PreAlso(models.Model):
    asin = models.ForeignKey(Item, models.DO_NOTHING, db_column='asin')
    also_id = models.AutoField(primary_key=True)
    also_view = models.TextField(blank=True, null=True)
    also_buy = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pre_also'

class ContentRecommend(models.Model):
    recommend_id = models.AutoField(primary_key=True)
    asin = models.ForeignKey('Item', models.DO_NOTHING, db_column='asin')
    recommend = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_recommend'

class Orders(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    asin = models.ForeignKey(Item, models.DO_NOTHING, db_column='asin')
    quantity = models.IntegerField(blank=True, null=True)
    reg_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders'

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
