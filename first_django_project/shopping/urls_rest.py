from django.urls import path

from .views_rest import product_list

urlpatterns = [
    path('products/', product_list, name='product_list'),
]