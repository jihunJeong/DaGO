from django.db import models
from django.template.defaultfilters import slugify
from user.models import User
from mall.models import CategoryBig, CategoryMid, CategorySm, Brand

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

    def get_rating_count(self):
        ratings = PreReview.objects.filter(asin=self.asin)
        return ratings.count()

    def get_rating_average(self):
        sum = 0
        ratings = PreReview.objects.filter(asin=self.asin)
        for i in ratings:
            sum += i.overall
        avg = sum / ratings.count()

        return avg

class PreReview(models.Model):
    review_id = models.AutoField(primary_key=True)
    overall = models.IntegerField()
    reviewtime = models.CharField(db_column='reviewTime', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reviewerid = models.CharField(db_column='reviewerID', max_length=50)  # Field name made lowercase.
    asin = models.ForeignKey(Item, models.DO_NOTHING, db_column='asin')
    reviewtext = models.TextField(db_column='reviewText', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pre_review'

class Review(models.Model):
    review_id = models.IntegerField(primary_key=True)
    reviewerid = models.ForeignKey(User, models.DO_NOTHING, db_column='reviewerID')  # Field name made lowercase.
    overall = models.IntegerField()
    reviewtext = models.TextField(db_column='reviewText', blank=True, null=True)  # Field name made lowercase.
    asin = models.ForeignKey(Item, models.DO_NOTHING, db_column='asin')
    reviewtime = models.CharField(db_column='reviewTime', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'review'


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

class AsinId(models.Model):
    aid = models.IntegerField(primary_key=True)
    asin = models.ForeignKey('Item', models.DO_NOTHING, db_column='asin', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asin_id'

