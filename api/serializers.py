from rest_framework import serializers
from .models import Product, Feature

class ProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = Product
    fields = '__all__'

class FeatureSerializer(serializers.ModelSerializer):
  class Meta:
    model = Feature
    fields = '__all__'