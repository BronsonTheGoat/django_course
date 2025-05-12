from django.urls import path

from .views_rest import product_list, product_details, customer_list, customer_details,\
    ProductList, ProductDetail, ProductList2, ProductCreate2, ProductRetrieve, ProductUpdate, ProductDestroy, ProductListCreate, ProductRetrieveUpdateDestroy

urlpatterns = [
    path('products/', product_list, name='product_list'),
    path('products/<int:pk>/', product_details, name='product_details'),
    path('products2/', ProductList.as_view(), name='product_list2'),
    path('products2/<int:pk>/', ProductDetail.as_view(), name='product_details2'),
    path('products3/', ProductList2.as_view(), name='product_list3'),
    path('products3/create', ProductCreate2.as_view(), name='product_create3'),
    path('products3/<int:pk>/', ProductRetrieve.as_view(), name='product_details3'),
    path('products3/<int:pk>/update', ProductUpdate.as_view(), name='product_details3'),
    path('products3/<int:pk>/delete', ProductDestroy.as_view(), name='product_details3'),
    path('products4/', ProductListCreate.as_view(), name='product-list'),
    path('products4/<int:pk>/', ProductRetrieveUpdateDestroy.as_view(), name='product-retrieve-update-destroy'),
    path('customers/', customer_list, name='customer_list'),
    path('customers/<int:pk>/', customer_details, name='customer_details'),
]