from django.db import models

# Create your models here.

class Book(models.Model):
    isbn = models.CharField(max_length=13, unique=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    published_year = models.IntegerField()
    pages = models.IntegerField()
    
    def __str__(self):
        return f"{self.title} - {self.author}"