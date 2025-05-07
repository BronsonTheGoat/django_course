from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product
from .serializers import ProductSerializer


@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    # if request.method == 'POST':
    #     serializer = ProductCreateSerializer(request.data)
    #     product = Product.objects.create(**serializer.data)
    #     serializer_2 = ProductSerializer(product)
    #     return Response(serializer_2.data)