from django.urls import path, include


from .views_rest import product_list, product_details, customer_list, customer_details,\
    ProductList, ProductDetail, ProductList2, ProductCreate2, ProductRetrieve, ProductUpdate,\
    ProductDestroy, ProductListCreate, ProductRetrieveUpdateDestroy, ProductViewSet, CustomerViewSet,\
    PurchaseViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'products5', ProductViewSet)
router.register(r'customers2', CustomerViewSet)
router.register(r'purchases2', PurchaseViewSet)

urlpatterns = [
    path('products1/', product_list, name='product_list1'),
    path('products1/<int:pk>/', product_details, name='product_details1'),
    path('products2/', ProductList.as_view(), name='product_list2'),
    path('products2/<int:pk>/', ProductDetail.as_view(), name='product_details2'),
    path('products3/', ProductList2.as_view(), name='product_list3'),
    path('products3/create', ProductCreate2.as_view(), name='product_create3'),
    path('products3/<int:pk>/', ProductRetrieve.as_view(), name='product_details3'),
    path('products3/<int:pk>/update', ProductUpdate.as_view(), name='product_details3'),
    path('products3/<int:pk>/delete', ProductDestroy.as_view(), name='product_details3'),
    path('products4/', ProductListCreate.as_view(), name='product-list4'),
    path('products4/<int:pk>/', ProductRetrieveUpdateDestroy.as_view(), name='product-retrieve-update-destroy4'),
    path('customers1/', customer_list, name='customer_list1'),
    path('customers1/<int:pk>/', customer_details, name='customer_details1'),
    path('', include(router.urls)),
]