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
    path("products/<int:product_id>/buy", views.buy_product, name="product_buy"),
    path("products/<int:product_id>/add_to_cart", views.add_product_to_cart, name="add_to_cart"),
    path("cart/", views.cart_details, name="cart_details"),
    path("cart/delete/<int:cart_item_id>", views.remove_product_from_cart, name="remove_from_cart"),
    path("cart/update/<int:cart_item_id>", views.update_product_in_cart, name="update_cart"),
    path("cart/checkout/", views.create_purchase, name="create_purchase"),
    path("register/", views.register, name="register"),
    path("page1/", views.page1, name="page1"),
    path("page2/", views.page2, name="page2"),
]
