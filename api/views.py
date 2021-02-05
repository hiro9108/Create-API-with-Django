from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer

def Top(request):
  return HttpResponse("<h1>Hello Django</h1>")

@api_view(['GET'])
def apiOverviews(request):
  api_urls = {
    'List': 'products/'
  }
  return Response(api_urls)

# For product model
@api_view(['GET'])
def getAllProducts(request):
  products = Product.objects.all()
  serializer = ProductSerializer(products, many=True)
  return Response(serializer.data)