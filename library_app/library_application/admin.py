from django.contrib import admin

from .models import Book, Author

# Register your models here.

class BookInline(admin.StackedInline):
    model = Book.author.through
    extra = 0
    
class AuthorInline(admin.TabularInline):
    model = Book.author.through
    extra = 0

class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "published_year"]
    list_filter = ["published_year"]
    ordering = ["title", "published_year"]
    filter_horizontal = ["author"]
    inlines = [AuthorInline]
    

class AuthorAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "birth_date", "birth_place"]
    list_filter = ["nationality"]
    ordering = ["name"]
    inlines = [BookInline]

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)