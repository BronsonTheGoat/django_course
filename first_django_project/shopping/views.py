from django.http import HttpResponse
from django.shortcuts import render

from .models import Customer

# Create your views here.

def index(request):
    return HttpResponse("Welcome to the shopping page!")

def get_customers(request):
    customers = Customer.objects.all()
    customer_text = '\n'.join([customer.first_name for customer in customers])
    return HttpResponse(f"Customers: {customer_text}")