from django.db import models

# Create your models here.
class Product(models.Model):
  name = models.CharField(max_length=100)
  description = models.CharField(max_length=255)
  price = models.DecimalField(max_digits=6, decimal_places=2)
  image_url = models.CharField(max_length=255)
  
  def __str__(self):
      return self.name

class Feature(models.Model):
  name = models.CharField(max_length=100)
  description = models.CharField(max_length=255)
  image_url = models.CharField(max_length=255)
  
  def __str__(self):
      return self.name
  