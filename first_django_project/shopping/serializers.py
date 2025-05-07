from rest_framework import serializers
    
class ProductSerializer(serializers.Serializer):
    # id = serializers.IntegerField()
    product_name = serializers.CharField(max_length=200)
    price = serializers.IntegerField()