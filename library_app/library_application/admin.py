from django.contrib import admin
from rangefilter.filters import DateRangeFilter
from .filters import PublishedYearFilter
from django_object_actions import DjangoObjectActions
from .models import Book, Author

# Register your models here.

class BookInline(admin.StackedInline):
    model = Author.books.through
    extra = 0
    
class AuthorInline(admin.TabularInline):
    model = Book.author.through
    extra = 0

class BookAdmin(DjangoObjectActions, admin.ModelAdmin):
    list_display = ["title", "published_year", "available"]
    ordering = ["title", "published_year"]
    filter_horizontal = ["author"]
    inlines = [AuthorInline]
    list_filter = [PublishedYearFilter]
    
    actions = ['set_borrowed', 'set_available']

    @admin.action(description="Set book borrowed")
    def set_borrowed(modeladmin, request, queryset): # modeladmin is replacement of self
        count = queryset.update(available=False)
        modeladmin.message_user(request, f'Updated products: {count}')
    
    @admin.action(description="Set book available")
    def set_available(modeladmin, request, queryset): # modeladmin is replacement of self
        count = queryset.update(available=True)
        modeladmin.message_user(request, f'Updated products: {count}')
    
    change_actions = ['borrow_book', 'return_book']
    
    def borrow_book(self, request, obj):
        if obj.available:
            obj.available = False
            obj.save()
            self.message_user(request, f'{obj} has been borrowed.')
        else:
            self.message_user(request, f'{obj} is already borrowed!')
            
    borrow_book.label = "Borrow"
    borrow_book.short_description = "Borrow"
           
    def return_book(self, request, obj):
        if not obj.available:
            obj.available = True
            obj.save()
            self.message_user(request, f'{obj} has been returned.')
        else:
            self.message_user(request, f'{obj} is already returned!')
            
    return_book.label = "Return"
    return_book.short_description = "Return"
            
    def get_change_actions(self, request, object_id, form_url):
        actions = super().get_change_actions(request, object_id, form_url)
        actions = list(actions)
        product = self.model.objects.get(pk=object_id)
        print(product)
        if product.available:
            actions.remove('return_book')
        if not product.available:
            actions.remove('borrow_book')

        return actions
    

class AuthorAdmin(DjangoObjectActions, admin.ModelAdmin):
    list_display = ["id", "name", "birth_date", "birth_place"]
    list_filter = ["nationality", ("birth_date", DateRangeFilter)]
    ordering = ["name"]
    inlines = [BookInline]

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)