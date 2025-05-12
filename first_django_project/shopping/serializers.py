from rest_framework import serializers
from .models import Customer, Product
    
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
    
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        # fields = ['name']
        fields = '__all__'
        # exclude = ['phone_number']
        
class CustomerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        exclude = ['phone_number', "user"]
        
class CustomerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'