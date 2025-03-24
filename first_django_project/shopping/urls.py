from django.urls import path, include
from .views import index, get_customers, get_products, get_product_details

urlpatterns = [
    path("", index, name="index"),
    path("customers", get_customers, name="customer_list"),
    path("products", get_products, name="product_list"),
    path("products/<product_id>", get_product_details, name="product_details"),
]
