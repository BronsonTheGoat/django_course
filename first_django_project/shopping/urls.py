from django.urls import path, include
from .views import index, get_customers, get_products, get_product_details, get_customer_details

urlpatterns = [
    path("", index, name="index"),
    path("customers", get_customers, name="customer_list"),
    path("products", get_products, name="product_list"),
    path("products/<product_id>", get_product_details, name="product_details"),
    path("customers/<customer_id>", get_customer_details, name="customer_details"),
]
