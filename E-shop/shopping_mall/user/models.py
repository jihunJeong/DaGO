from django.db import models

# Create your models here.
class User(models.Model):
    email_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=128)
    password = models.CharField(max_length=20)
    contact = models.CharField(max_length=50)
    enroll_date = models.DateField(db_column='enroll_date')  # Field renamed to remove unsuitable characters.
    address = models.CharField(max_length=50)
    nickname = models.CharField(max_length=20)
    rule_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email'
