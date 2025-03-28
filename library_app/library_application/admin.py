from django.contrib import admin

from .models import Book, Author

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'isbn', 'title', 'author', 'published_year', 'pages']
    

admin.site.register(Book, BookAdmin)

# class AuthorAdmin(admin.ModelAdmin):
#     list_display = ['id', 'name', 'birth_date']

# admin.site.register(Author, AuthorAdmin)