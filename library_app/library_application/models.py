from django.contrib.auth.models import User
from django.db import models

# Create your models here.
    
class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    birth_place = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)
    decease_date = models.DateField(blank=True, null=True)
    decease_place = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
        return f"{self.name}"

class Book(models.Model):
    isbn = models.CharField(max_length=13, unique=True)
    title = models.CharField(max_length=200)
    author = models.ManyToManyField(Author, related_name="books")
    published_year = models.IntegerField()
    pages = models.IntegerField()    
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True)
    available = models.BooleanField()
    
    def __str__(self):
        authors = ", ".join([str(author) for author in self.author.all()])
        return f"{self.title} - {authors}"
    
class Borrow(models.Model):
    borrow_date = models.DateField()
    return_date = models.DateField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='borrows')
    book = models.ForeignKey(Book, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.user} ({self.borrow_date})'
    
    class Meta:
        ordering = ["borrow_date"]