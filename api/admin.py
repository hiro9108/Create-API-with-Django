from django.contrib import admin
from .models import Product, Feature

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
   pass

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
   pass