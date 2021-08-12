from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField(verbose_name="이메일")
    password = models.CharField(max_length=128, verbose_name="비밀번호")
    nickname = models.CharField(max_length=20, verbose_name="닉네임")
    contact = models.IntegerField(verbose_name="전화번호")
    address = models.CharField(max_length=50, verbose_name="주소")
    level = models.CharField(max_length=8, verbose_name="등급",
        choices={
            ('admin', 'admin'),
            ('user', 'user')
        })

    def __str__(self):
        return self.email
    class Meta:
        db_table = 'users'
        verbose_name = "사용자"
        verbose_name_plural = "사용자"

class Email(models.Model):
    email_id = models.IntegerField(primary_key=True)
    email = models.CharField(db_column='email', max_length=20)  # Field renamed to remove unsuitable characters.
    password = models.CharField(max_length=20)
    contact = models.IntegerField()
    enroll_date = models.DateField(db_column='enroll date')  # Field renamed to remove unsuitable characters.
    address = models.CharField(max_length=50)
    nickname = models.CharField(max_length=20, blank=True, null=True)
    rule_id = models.IntegerField()
    #credit = models.ForeignKey('Credit', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email'


class Credit(models.Model):
    credit_id = models.IntegerField(primary_key=True)
    account = models.CharField(max_length=20)
    bank = models.CharField(max_length=20)
    email = models.ForeignKey('Email', models.DO_NOTHING)
    card = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'credit'


#
# class Brand(models.Model):
#     brand_id = models.IntegerField(primary_key=True)
#     brand_name = models.CharField(db_column='brand name', max_length=20)  # Field renamed to remove unsuitable characters.
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
#     category_name = models.CharField(db_column='category name', max_length=20)  # Field renamed to remove unsuitable characters.
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
#     category_id = models.ForeignKey(Category, models.DO_NOTHING, db_column='category id')  # Field renamed to remove unsuitable characters.
#     image_link = models.CharField(db_column='image link', max_length=50)  # Field renamed to remove unsuitable characters.
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
