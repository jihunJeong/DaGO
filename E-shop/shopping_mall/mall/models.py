from django.db import models
from django.utils.text import slugify
# Create your models here.

'''
    상품은 Category 있음
    이 Category는 대분류 - 중분류 - 소분류로 이루어져 있음
'''
class CategoryBig(models.Model):
    '''
        Note:
            상품의 대분류
    '''
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
    '''
        Note:
            상품의 중분류
    '''
    cm_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300, blank=True, null=True)
    cb = models.ForeignKey(CategoryBig, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category_mid'

class CategorySm(models.Model):
    '''
        Note:
            상품의 소분류
    '''
    cs_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    cm = models.ForeignKey(CategoryMid, models.DO_NOTHING, blank=True, null=True)
    cb = models.ForeignKey(CategoryBig, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category_sm'

class Brand(models.Model):
    '''
        Note:
            상품을 출시 한 회사
    '''
    brand_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'brand'