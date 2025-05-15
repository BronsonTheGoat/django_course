from rest_framework import serializers
from .models import Customer, Product, HomeAddress, CustomerAddress, Purchase, PurchaseItem
    
class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    product_name = serializers.CharField(max_length=200)
    # price = serializers.IntegerField()
    
# class ProductCreateSerializer(serializers.Serializer):
#     product_name = serializers.CharField(max_length=200)
#     price = serializers.IntegerField()
    
class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
    
class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
    
# class CustomerSerializer(serializers.Serializer):
#     # first_name = serializers.CharField(max_length=200)
#     # last_name = serializers.CharField(max_length=200)
#     name = serializers.CharField(max_length=200)
#     # email = serializers.CharField(max_length=200)
    
# class CustomerCreateSerializer(serializers.Serializer):
#     first_name = serializers.CharField(max_length=200)
#     last_name = serializers.CharField(max_length=200)
#     email = serializers.CharField(max_length=200)
#     age = serializers.IntegerField()
#     phone_number = serializers.CharField(required=False)

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeAddress
        fields = '__all__'

class CustomerAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerAddress
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'product_name']

class PurchaseItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    # product = serializers.StringRelatedField(many=True)
    class Meta:
        model = PurchaseItem
        fields = ['quantity', 'product']
        
class PurchaseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = ['id', 'purchase_date', 'customer_id']
        
# class PurchaseSerializer(serializers.ModelSerializer):
#     # products = serializers.StringRelatedField(many=True)
#     class Meta:
#         model = Purchase
#         fields = ['purchase_date','products']
        
class PurchaseSerializer(serializers.ModelSerializer):
    items = PurchaseItemSerializer(many=True)

    class Meta:
        model = Purchase
        fields = ['id', 'purchase_date', 'items'] 
           
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id','name']
        # fields = '__all__'
        # exclude = ['phone_number']
        
class CustomerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        exclude = ['phone_number', "user"]
        
class CustomerDetailSerializer(serializers.ModelSerializer):
    customer_addresses = CustomerAddressSerializer(many=True)
    home_address = AddressSerializer(source='address')
    number_of_purchases = serializers.SerializerMethodField()    
    purchases = PurchaseSerializer(many=True)
    # purchase_item = PurchaseItemSerializer(source='items')
    rank = serializers.SerializerMethodField()
    
    class Meta:
        model = Customer
        fields = '__all__'
    
    def get_number_of_purchases(self, obj):
        return obj.purchases.count()
    
    def get_rank(self, obj):
        if obj.purchases.count() == 0:
            return "guest"
        elif obj.purchases.count() < 5:
            return "bronze"
        elif 10 > obj.purchases.count() > 5:
            return "silver"
        else:
            return "gold"