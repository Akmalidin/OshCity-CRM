from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'shop')
admin.site.register(Product, ProductAdmin)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
admin.site.register(Shop, ShopAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(Category, CategoryAdmin)

class Product_brandAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(Product_brand, Product_brandAdmin)