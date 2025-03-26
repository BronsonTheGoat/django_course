from django.http import HttpResponse
from django.shortcuts import render, loader

from .forms import CustomerForm, ProductForm, ProductForm2
from .models import Customer, Product

# Create your views here.

def index(request):
    return render(request, 'shopping/index.html')

# def get_customers(request):
#     customers = Customer.objects.all()
#     # customers = Customer.objects.filter(first_name="Gábor")
#     # customer_text = '\n'.join([customer.first_name for customer in customers])
#     # return HttpResponse(f"Customers: {customer_text}")
    
#     context = {
#         'customers': customers
#     }

#     # template = loader.get_template('shopping/customers.html')
#     # # context = {}
#     # return HttpResponse(template.render(context, request))

#     return render(request, 'shopping/customers.html', context)

# Gréta version
# def get_customers(request):
#     print(request.GET)
#     print(request.POST)
#     customers = Customer.objects.all()
#     print(customers)
#     first_name = request.GET.get('first_name')
#     last_name = request.GET.get('last_name')
#     email = request.GET.get('email')
#     print(first_name)
#     print(last_name)
#     print(email)
#     if first_name:
#         customers = customers.filter(first_name=first_name)
#         print(customers)
#     if last_name:
#         customers = customers.filter(last_name=last_name)
#         print(customers)
#     if email:
#         customers = customers.filter(email=email)
#         print(customers)

#         # customers = Customer.objects.filter(
#         #     first_name=first_name,
#         #     # last_name=request.GET.get('last_name'),
#         #     # email=request.GET.get('email'),
#         # )
#     print(customers)

#     context = {
#         'customers': customers
#     }
#     return render(request, 'shopping/customers.html', context)

# def get_customers(request):
#     print(request.GET)
#     print(request.POST)
#     customers = Customer.objects.all()
#     form = CustomerForm(request.GET)
#     print(form.is_valid())
#     print(form.data)
#     if form.is_valid():
#         print(form.cleaned_data)
#     # if first_name:
#     #     customers = customers.filter(first_name=first_name)
#     # if last_name:
#     #     customers = customers.filter(last_name=last_name)
#     # if email:
#     #     customers = customers.filter(email__contains=email)
#     if request.GET:
#         first_name = request.GET.get("first_name")
#         last_name = request.GET.get("last_name")
#         email = request.GET.get("email")
#         customers = customers.filter(first_name__contains=first_name,
#                                      last_name__contains=last_name,
#                                      email__contains=email,
#                                      )
            
#     context = {
#         "form": form,
#         'customers': customers
#     }

#     return render(request, 'shopping/customers2.html', context)

def get_customers(request):
    customers = Customer.objects.all()
    form = CustomerForm(request.GET or None)
    if request.GET and form.is_valid():
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        email = form.cleaned_data.get('email')
        customers = customers.filter(
            first_name__contains=first_name,
            last_name__contains=last_name,
            email__contains=email
        )

    context = {
        'form': form,
        'customers': customers
    }
    return render(request, 'shopping/customers.html', context)

def get_products(request):
    products = Product.objects.all()
    form = ProductForm2(request.GET or None)
    if request.GET and form.is_valid():
        product_name = form.cleaned_data.get('product_name')
        products = products.filter(
            product_name__contains=product_name,
        )

    context = {
        'form': form,
        'products': products
    }
    return render(request, 'shopping/products.html', context)
    
def get_product_details(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return HttpResponse("No product found!", status=404)
    context = {'product': product}
    return render(request, 'shopping/product_details.html', context)

def get_customer_details(request, customer_id):
    try:
        customer = Customer.objects.get(id=customer_id)
    except Customer.DoesNotExist:
        return HttpResponse("No customer found!", status=404)
    context = {'customer': customer}
    return render(request, 'shopping/customer_details.html', context)