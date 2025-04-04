from django.contrib import admin

from .models import Book, Author

# Register your models here.

class BookInline(admin.StackedInline):
    model = Book
    extra = 0

class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "published_year"]
    list_filter = ["published_year", "author"]
    ordering = ["title", "published_year"]
    

admin.site.register(Book, BookAdmin)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "birth_date", "birth_place"]
    list_filter = ["nationality"]
    ordering = ["name"]
    inlines = [BookInline]

admin.site.register(Author, AuthorAdmin)