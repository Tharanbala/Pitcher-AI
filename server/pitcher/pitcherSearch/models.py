from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=80)
    price = models.CharField(max_length=100)
    dimensions = models.CharField(max_length=50)
    pros = models.CharField(max_length=500)
    cons = models.CharField(max_length=500)
    reviews = models.CharField(max_length=500)
    stars = models.IntegerField()