from django.http import HttpResponse
from django.shortcuts import render, loader

from .models import Customer, Product

# Create your views here.

def index(request):
    return render(request, 'shopping/index.html')

def get_customers(request):
    customers = Customer.objects.all()
    # customers = Customer.objects.filter(first_name="Gábor")
    # customer_text = '\n'.join([customer.first_name for customer in customers])
    # return HttpResponse(f"Customers: {customer_text}")
    
    context = {
        'customers': customers
    }

    # template = loader.get_template('shopping/customers.html')
    # # context = {}
    # return HttpResponse(template.render(context, request))

    return render(request, 'shopping/customers.html', context)

def get_products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'shopping/products.html', context)
    
def get_product_details(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return HttpResponse("No product found!", status=404)
    context = {'product': product}
    return render(request, 'shopping/product_details.html', context)