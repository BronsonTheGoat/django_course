from django.contrib import admin

from .models import Customer, Product, HomeAddress, CustomerAddress, Purchase, PurchaseItem

# Register your models here.

class AddressInline(admin.StackedInline):
    model = HomeAddress
    # extra = 0
    
class CustomerAddressInline(admin.StackedInline):
    model = CustomerAddress
    extra = 0
    
class PurchaseInline(admin.TabularInline):
    model = PurchaseItem
    extra = 0

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email',  'age']
    list_filter = ['age']
    ordering = ['id']
    inlines = [AddressInline,  CustomerAddressInline]
    
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

@admin.register(HomeAddress)
class HomeAddressAdmin(admin.ModelAdmin):
    list_display = ["zip_code", "city", "street", "house_number", "customer"]
    list_filter = ["city"]
    ordering = ["city", "street"]
    # readonly_fields = ["customer"]
    # fields = ["city", "customer"]
    raw_id_fields = ["customer"]

#   In csae of remove it can be only accessed from the linked admin site 
@admin.register(CustomerAddress)
class CustomerAddressAdmin(admin.ModelAdmin):
    list_display = ["id", "country", "zip_code", "city", "street", "house_number", "customer"]
    list_filter = ["city"]
    ordering = ["city", "street"]
    # readonly_fields = ["customer"]
    # fields = ["city", "customer"]
    raw_id_fields = ["customer"]   


class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "product_name", "price"]
    readonly_fields = ["created", "last_modified"]
    
class PurchaseAdmin(admin.ModelAdmin):
    inlines = [PurchaseInline]


admin.site.register(Customer, CustomerAdmin)
# admin.site.register(HomeAddress, HomeAddressAdmin)
# admin.site.register(CustomerAddress)
admin.site.register(Product, ProductAdmin)
admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(PurchaseItem)