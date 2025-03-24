from django.urls import path, include
from .views import index, get_customers

urlpatterns = [
    path("", index, name="index"),
    path("customers", get_customers, name="customer_list"),
]
