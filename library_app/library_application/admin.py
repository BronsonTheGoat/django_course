from django.contrib import admin

from .models import Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'published_year']
    list_filter = ['published_year', 'author']
    ordering = ['title', 'published_year']
    

admin.site.register(Book, BookAdmin)

# class AuthorAdmin(admin.ModelAdmin):
#     list_display = ['id', 'name', 'birth_date']

# admin.site.register(Author, AuthorAdmin)