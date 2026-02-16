from django.contrib import admin
from .models import Product
# Register your models here.
admin.site.register(Product)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name_product', 'price', 'created_at', 'image')