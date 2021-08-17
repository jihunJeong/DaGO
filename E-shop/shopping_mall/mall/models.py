from django.db import models
# Create your models here.

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
    brand_name = models.CharField(db_column='brand name', max_length=20)  # Field renamed to remove unsuitable characters.
    nation = models.CharField(max_length=20)

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
            imagelink = imagelink[1:-1]
            print(imagelink)     
        return imagelink
    
    def __str__(self):
        return self.title

    def get_category(self):
        return self.cb.name


class TestItems(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    test_id = models.AutoField(primary_key=True)
    brand_name = models.CharField(max_length=100, blank=True, null=True)
    categories = models.CharField(max_length=1000, blank=True, null=True)
    image_link = models.CharField(db_column='image link', max_length=2500, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    nickname = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        db_table = 'test_items'
    
    def get_absolute_url(self):
        return f"/product/{self.pk}/"

    def __str__(self):
        return f'{self.brand_name} {self.nickname}'
    