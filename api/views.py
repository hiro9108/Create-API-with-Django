from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product, Feature
from .serializers import ProductSerializer, FeatureSerializer

def Top(request):
  return HttpResponse("<h1>Hello Django</h1>")

@api_view(['GET'])
def apiOverviews(request):
  api_urls = {
    'List-products': 'products/',
    'List-features': 'features/',
  }
  return Response(api_urls)

# For product model
@api_view(['GET'])
def getAllProducts(request):
  products = Product.objects.all()
  serializer = ProductSerializer(products, many=True)
  return Response(serializer.data)

# For feature model
@api_view(['GET'])
def getAllFeatures(request):
  features = Feature.objects.all()
  serializer = ProductSerializer(features, many=True)
  return Response(serializer.data)