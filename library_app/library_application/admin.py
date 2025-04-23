from django.contrib import admin
from rangefilter.filters import DateRangeFilter
from django_object_actions import DjangoObjectActions
from .filters import PublishedYearFilter
from .models import Book, Author

# Register your models here.

class BookInline(admin.StackedInline):
    model = Author.books.through
    extra = 0
    
class AuthorInline(admin.TabularInline):
    model = Book.author.through
    extra = 0

class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "published_year"]
    ordering = ["title", "published_year"]
    filter_horizontal = ["author"]
    inlines = [AuthorInline]
    list_filter = [PublishedYearFilter]
    

class AuthorAdmin(DjangoObjectActions, admin.ModelAdmin):
    list_display = ["id", "name", "birth_date", "birth_place"]
    list_filter = ["nationality", ("birth_date", DateRangeFilter)]
    ordering = ["name"]
    inlines = [BookInline]

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)