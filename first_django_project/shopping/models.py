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