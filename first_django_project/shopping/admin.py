from django.contrib import admin

from .models import Customer, Product

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email',  'age']
    list_filter = ['age']
    ordering = ['id']
    
    # readonly_fields = ['age']
    fieldsets = (
        ('Name', {
            'fields': ('first_name', 'last_name')
        }),
        ('Contact information', {
            'fields': ('email', 'phone_number')
        }),
        ('Other', {
            'fields': ('age',)
        })
    )

admin.site.register(Customer, CustomerAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_name', 'price']

admin.site.register(Product, ProductAdmin)