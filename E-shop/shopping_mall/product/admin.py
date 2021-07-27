from django.contrib import admin
from .models import Product, TestItems
# Register your models here.

class productAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

admin.site.register(Product)
admin.site.register(TestItems)
