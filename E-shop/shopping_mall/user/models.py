from django.db import models

# Create your models here.
# class User(models.Model):
#     email = models.EmailField(verbose_name="이메일")
#     password = models.CharField(max_length=128, verbose_name="비밀번호")
#     nickname = models.CharField(max_length=20, verbose_name="닉네임")
#     contact = models.IntegerField(verbose_name="전화번호")
#     address = models.CharField(max_length=50, verbose_name="주소")
#     level = models.CharField(max_length=8, verbose_name="등급",
#         choices={
#             ('admin', 'admin'),
#             ('user', 'user')
#         })
#
#     def __str__(self):
#         return self.email
#     class Meta:
#         db_table = 'users'
#         verbose_name = "사용자"
#         verbose_name_plural = "사용자"

class User(models.Model):
    email_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=128)
    password = models.CharField(max_length=20)
    contact = models.IntegerField()
    enroll_date = models.DateField(db_column='enroll_date')  # Field renamed to remove unsuitable characters.
    address = models.CharField(max_length=50)
    nickname = models.CharField(max_length=20)
    rule_id = models.IntegerField(blank=True, null=True)
    # credit = models.ForeignKey('Credit', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email'

class Credit(models.Model):
    credit_id = models.IntegerField(primary_key=True)
    account = models.CharField(max_length=20)
    bank = models.CharField(max_length=20)
    email = models.ForeignKey('User', models.DO_NOTHING)
    card = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'credit'

# class AuthGroup(models.Model):
#     name = models.CharField(unique=True, max_length=150)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_group'
#
#
# class AuthGroupPermissions(models.Model):
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#     permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_group_permissions'
#         unique_together = (('group', 'permission'),)
#
#
# class AuthPermission(models.Model):
#     name = models.CharField(max_length=255)
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
#     codename = models.CharField(max_length=100, db_collation='latin1_swedish_ci')
#
#     class Meta:
#         managed = False
#         db_table = 'auth_permission'
#         unique_together = (('content_type', 'codename'),)
#
#
# class AuthUser(models.Model):
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.IntegerField()
#     username = models.CharField(unique=True, max_length=150)
#     first_name = models.CharField(max_length=150)
#     last_name = models.CharField(max_length=150)
#     email = models.CharField(max_length=254)
#     is_staff = models.IntegerField()
#     is_active = models.IntegerField()
#     date_joined = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'auth_user'
#
#
# class AuthUserGroups(models.Model):
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_user_groups'
#         unique_together = (('user', 'group'),)
#
#
# class AuthUserUserPermissions(models.Model):
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_user_user_permissions'
#         unique_together = (('user', 'permission'),)
#
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
#     email = models.ForeignKey('Email', models.DO_NOTHING)
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
#
# class DjangoAdminLog(models.Model):
#     action_time = models.DateTimeField()
#     object_id = models.TextField(blank=True, null=True)
#     object_repr = models.CharField(max_length=200)
#     action_flag = models.PositiveSmallIntegerField()
#     change_message = models.TextField()
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'django_admin_log'
#
#
# class DjangoContentType(models.Model):
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)
#
#     class Meta:
#         managed = False
#         db_table = 'django_content_type'
#         unique_together = (('app_label', 'model'),)
#
#
# class DjangoMigrations(models.Model):
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'django_migrations'
#
#
# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'django_session'
#
#
# class Email(models.Model):
#     email_id = models.AutoField(primary_key=True)
#     email = models.CharField(max_length=20)
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
# class Orders(models.Model):
#     quantity = models.IntegerField()
#     reg_date = models.DateTimeField()
#     product = models.ForeignKey('Products', models.DO_NOTHING)
#     user = models.ForeignKey('Users', models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'orders'
#
#
# class Products(models.Model):
#     name = models.CharField(max_length=64)
#     price = models.IntegerField()
#     description = models.TextField()
#     stock = models.IntegerField()
#     reg_date = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'products'
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
# class TestItems(models.Model):
#     name = models.CharField(max_length=100, blank=True, null=True)
#     brand_name = models.CharField(max_length=100, blank=True, null=True)
#     categories = models.CharField(max_length=1000, blank=True, null=True)
#     image_link = models.CharField(db_column='image link', max_length=2500, blank=True, null=True)  # Field renamed to remove unsuitable characters.
#     nickname = models.CharField(max_length=1000, blank=True, null=True)
#     test_id = models.AutoField(primary_key=True)
#
#     class Meta:
#         managed = False
#         db_table = 'test_items'
#
#
# class TestReviews(models.Model):
#     reviewtime = models.DateField(blank=True, null=True)
#     vote = models.CharField(max_length=1000, blank=True, null=True)
#     score = models.CharField(max_length=1000, blank=True, null=True)
#     text = models.CharField(max_length=1000, blank=True, null=True)
#     review_name = models.CharField(max_length=1000, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'test_reviews'
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
#
#
# class Users(models.Model):
#     email = models.CharField(max_length=254, db_collation='utf8_general_ci')
#     password = models.CharField(max_length=128, db_collation='utf8_general_ci')
#     nickname = models.CharField(max_length=20, db_collation='utf8_general_ci')
#     contact = models.IntegerField()
#     address = models.CharField(max_length=50, db_collation='utf8_general_ci')
#     level = models.CharField(max_length=8, db_collation='utf8_general_ci')
#
#     class Meta:
#         managed = False
#         db_table = 'users'