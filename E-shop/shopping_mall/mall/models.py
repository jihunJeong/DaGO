from django.db import models

# Create your models here.

class Category(models.Model):
    category_id = models.IntegerField(primary_key=True)
    category_name = models.CharField(db_column='category name', max_length=20)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'category'

class Brand(models.Model):
    brand_id = models.IntegerField(primary_key=True)
    brand_name = models.CharField(db_column='brand name', max_length=20)  # Field renamed to remove unsuitable characters.
    nation = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'brand'
        
class Item(models.Model):
    name = models.CharField(max_length=20)
    item_id = models.IntegerField(primary_key=True)
    price = models.FloatField()
    enroll_date = models.DateField(db_column='enroll date')  # Field renamed to remove unsuitable characters.
    category_id = models.ForeignKey(Category, models.DO_NOTHING, db_column='category id')  # Field renamed to remove unsuitable characters.
    image_link = models.CharField(db_column='image link', max_length=50)  # Field renamed to remove unsuitable characters.
    brand = models.ForeignKey(Brand, models.DO_NOTHING, blank=True, null=True)
    nickname = models.CharField(max_length=20, blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'item'

    def get_absolute_url(self):
        return f'/product/{self.name}/'