from django.contrib import admin
from django.db.models import F
from rangefilter.filters import DateRangeFilter, DateRangeFilterBuilder, DateTimeRangeFilter, \
    DateTimeRangeFilterBuilder, NumericRangeFilter, NumericRangeFilterBuilder
from django_object_actions import DjangoObjectActions
# from .filters import PriceRangeFilter, AgeRangeFilter, AgeRangeFilter2
from .filters2 import AgeRangeFilter, PriceRangeFilter
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
    # list_filter = ['age']
    list_filter = [AgeRangeFilter]
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


class ProductAdmin(DjangoObjectActions, admin.ModelAdmin):
    list_display = ["id", "product_name", "price", "is_discounted", "storage_quantity"]
    readonly_fields = ["created", "last_modified"]
    # list_filter = [PriceRangeFilter]
    list_filter = [
    ('expiry_date', DateRangeFilter),
    ('expiry_date', DateRangeFilterBuilder(title='Expiry date:', default_start='2024-07-01',
                                           default_end='2024-08-01')),
    ('last_modified', DateTimeRangeFilter),
    ('last_modified', DateTimeRangeFilterBuilder(title='Last modified at:')),
    ('storage_quantity', NumericRangeFilter),
    ('price', NumericRangeFilterBuilder(title='Quantity:', default_start=100, default_end=300)),
]
    actions = ['set_discounted', 'set_full_price']

    # @admin.action(description="Set products as discounted2")
    def set_discounted(modeladmin, request, queryset): # modeladmin is replacement of self
        # print(modeladmin)
        # print(request)
        # print(queryset)
        count = queryset.update(is_discounted=True, price=F("price")-100)
        modeladmin.message_user(request, f'Updated products: {count}')

    set_discounted.short_description = 'Set products as discounted'
    
    @admin.action(description="Set products to full price")
    def set_full_price(modeladmin, request, queryset): # modeladmin is replacement of self
        # print(modeladmin)
        # print(request)
        # print(queryset)
        count = queryset.update(is_discounted=False, price=F("price")+100)
        modeladmin.message_user(request, f'Updated products: {count}')
        
    change_actions = ['set_product_discounted', 'set_product_full_price', "buy_product"]
    
    def set_product_discounted(self, request, obj):
        # print(request)
        # print(obj)
        if not obj.is_discounted:
            obj.is_discounted = True
            obj.price -= 100
            obj.save()
            self.message_user(request, f'{obj} has been discounted.')
        else:
            self.message_user(request, f'{obj} is already discounted!')
            
    set_product_discounted.label = "Discount"
    set_product_discounted.short_description = "Discount"
            
    def set_product_full_price(self, request, obj):
        # print(request)
        # print(obj)
        if obj.is_discounted:
            obj.is_discounted = False
            obj.price += 100
            obj.save()
            self.message_user(request, f'{obj} has been set to full price.')
        else:
            self.message_user(request, f'{obj} is already at full price!')
            
    def buy_product(self, request, obj):
        if obj.storage_quantity > 0:
            obj.storage_quantity -= 1
            obj.save()
            self.message_user(request, f'{obj} has been bought.')
        else:
            self.message_user(request, f'{obj} is out of stock!')
            
    def get_change_actions(self, request, object_id, form_url):
        actions = super().get_change_actions(request, object_id, form_url)
        actions = list(actions)
        # print(actions)
        # print(type(actions))
        # print(object_id)
        product = self.model.objects.get(pk=object_id)
        print(product)
        if product.is_discounted:
            actions.remove('set_product_discounted')
        if not product.is_discounted:
            actions.remove('set_product_full_price')
        if product.storage_quantity <= 0:
            actions.remove('buy_product')

        # print(actions)

        return actions
    
    
class PurchaseAdmin(admin.ModelAdmin):
    inlines = [PurchaseInline]


admin.site.register(Customer, CustomerAdmin)
# admin.site.register(HomeAddress, HomeAddressAdmin)
# admin.site.register(CustomerAddress)
admin.site.register(Product, ProductAdmin)
admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(PurchaseItem)