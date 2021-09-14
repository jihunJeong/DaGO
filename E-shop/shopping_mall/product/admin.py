from django.contrib import admin
from .models import Item
# Register your models here.

class productAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

admin.site.register(Item)
