from django.contrib import admin
from .models import Product, Category


@admin.register(Product)
class ProductsAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class ProductsAdmin(admin.ModelAdmin):
    pass
