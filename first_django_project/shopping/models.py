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
    
# invoice address and delivery address
class HomeAddress(models.Model):
    city = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    street = models.CharField(max_length=50)
    house_number = models.CharField(max_length=4)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, related_name="address")
    
    def __str__(self):
        return f"{self.zip_code}, {self.city} {self.street} {self.house_number}"
    
    class Meta:
        verbose_name = "Home address"
        verbose_name_plural = "Home addresses"
        
        
class CustomerAddress(models.Model):
    COUNTRY_CHOICES = [
        (1, 'Magyarország'),
        (2, 'Ausztria'),
        (3, "U.S.A"),
    ]

    customer = models.ForeignKey(Customer, related_name='customer_addresses', on_delete=models.CASCADE)
    country = models.IntegerField(choices=COUNTRY_CHOICES, default=1)
    zip_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=200)
    house_number = models.CharField(max_length=4)

    def __str__(self):
        return f"{self.get_country_display()}, {self.zip_code} {self.city}, {self.street} {self.house_number}"
        # return f"{self.country}, {self.zip_code} {self.city}, {self.street} {self.house_number}"

    class Meta:
        verbose_name = 'Customer address'
        verbose_name_plural = 'Customer addresses' 
        
    
class Product(models.Model):
    product_name = models.CharField(max_length=200)
    price = models.IntegerField()
    expiry_dte = models.DateField(blank=True, null=True)
    is_discounted = models.BooleanField(default=False)
    storage_quantity = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.product_name}: {self.price}"

# orders