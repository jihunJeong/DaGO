from django.db import models
from django.utils.text import slugify
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

    def get_absolute_url(self):
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