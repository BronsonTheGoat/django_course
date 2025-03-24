from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Product(models.Model):
    product_name = models.CharField(max_length=200)
    price = models.IntegerField()
    expiry_dte = models.DateField(blank=True, null=True)
    is_discounted = models.BooleanField(default=False)
    storage_quantity = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.product_name}: {self.price}"