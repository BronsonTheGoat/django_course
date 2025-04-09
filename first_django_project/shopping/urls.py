from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("customers", views.get_customers, name="customer_list"),
    path("customers/add", views.add_customer, name="add_customer"),
    path("customers/<int:customer_id>", views.get_customer_details, name="customer_details"),
    path("customers/<int:customer_id>/update", views.update_customer, name="customer_update"),
    path("products", views.get_products, name="product_list"),
    path("products/<int:product_id>", views.get_product_details, name="product_details"),
    path("products/add", views.add_product, name="product_add"),
    path("products/<int:product_id>/update", views.update_product, name="product_update"),
    path("products/<int:product_id>/delete", views.delete_product, name="product_delete"),
]
