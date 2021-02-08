from django.urls import path
from .views import Top, apiOverviews, getAllProducts, getAllFeatures

urlpatterns = [
    path('', Top),                         # http://localhost:8000
    path('api/', apiOverviews),            # http://localhost:8000/api/
    path('api/products/', getAllProducts), # http://localhost:8000/api/products
    path('api/features/', getAllFeatures), # http://localhost:8000/api/features
]
