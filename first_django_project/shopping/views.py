from django.http import HttpResponse
from django.db.models import ProtectedError
from django.shortcuts import render, loader, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from .decorators import superuser_required, custom_permission_required
import datetime
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .forms import CustomerForm, CustomerAddForm2, ProductForm2, ProductAddForm2, PurchaseItemForm, CustomUserCreationForm
from .models import Customer, Product, Purchase, PurchaseItem, ShopingCart, CartItem

from django.utils.translation import gettext as _
from django.utils import translation

from django.conf import settings

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

def page1(request):
    # translation.activate("hu")
    return HttpResponse(_("Welcome!"))

def page2(request):
    # translation.activate("hu")
    # return HttpResponse(_("Hi my friend!"))
    # context = {
    #     "title": _("Welcome on the page!"),
    # }
    return render(request, "shopping/page2.html")


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
    context = {'product': product, 'form': PurchaseItemForm}
    return render(request, 'shopping/product_details.html', context)

def get_customer_details(request, customer_id):
    try:
        customer = Customer.objects.get(id=customer_id)
    except Customer.DoesNotExist:
        return HttpResponse("No customer found!", status=404)
    context = {'customer': customer}
    return render(request, 'shopping/customer_details.html', context)

def add_customer(request):
    print(request.GET)
    print(request.POST)
    form = CustomerAddForm2(request.POST)
    if form.is_valid():
        
        form.save() # Works only with ModelForm
        return redirect("customer_list")
                
        # first_name = form.cleaned_data.post('first_name')
        # last_name = form.cleaned_data.post('last_name')
        # email = form.cleaned_data.post('email')
        # age = form.cleaned_data.post('age')
        # phone_number = form.cleaned_data.post('phone_number')
        # customers = customers.filter(
        #     first_name__contains=first_name,
        #     last_name__contains=last_name,
        #     email__contains=email
        # )
        # Customer.objects.create(**form.cleaned_data)
        
    context = {"form":CustomerAddForm2()}
    return render(request, 'shopping/customer_add.html', context)

def add_product(request):
    form = ProductAddForm2(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect("product_list")
        
    context = {"form":ProductAddForm2()}
    return render(request, "shopping/product_add.html", context)

def is_superuser(user):
    print(user)
    print(user.is_superuser)
    from django.contrib.auth.models import Permission
    permissions = Permission.objects.filter(user=user)
    print(permissions)
    return user.is_superuser

# @login_required
# @user_passes_test(is_superuser)
# @permission_required('shopping.product_update', raise_exception=True)
# @superuser_required
@custom_permission_required('shopping.product_update', raise_exception=True)
def update_product(request, product_id):
    # print(request)
    # print('GET', request.GET)
    # print('POST', request.POST)

    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return HttpResponse('Product not found', status=404)

    if request.POST:
        form = ProductForm2(request.POST, request.FILES, instance=product)
        if form.is_valid():
            print('DATA:')
            print(form.data)
            print(form.cleaned_data)
            print('____________')
            form.save()
            return redirect('product_details', product_id=product_id)

    form = ProductForm2(instance=product)
    context = {
        'form': form,
        'product': product
    }
    return render(request, 'shopping/product_update.html', context)

def update_customer(request, customer_id):
    # print(request)
    # print('GET', request.GET)
    # print('POST', request.POST)

    try:
        customer = Customer.objects.get(id=customer_id)
    except Customer.DoesNotExist:
        return HttpResponse('Customer not found', status=404)

    if request.POST:
        form = CustomerAddForm2(request.POST, instance=customer)
        if form.is_valid():
            print('DATA:')
            print(form.data)
            print(form.cleaned_data)
            print('____________')
            form.save()
            return redirect('customer_details', customer_id=customer_id)

    form = CustomerAddForm2(instance=customer)
    context = {
        'form': form,
        'customer': customer
    }
    return render(request, 'shopping/customer_update.html', context)

def delete_product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return HttpResponse('Product not found', status=404)

    print(product)
    try:
        product.delete()
        return render(request, 'shopping/product_delete_success.html', {})
        # return redirect('product_list')
    except ProtectedError:
        context = {
            'product': product,
            'error_message': 'This product cannot be deleted'
        }
        # return render(request, 'shopping/product_details.html', context)
        return render(request, 'shopping/product_delete_failed.html', context)
        # return HttpResponse('This product cannot be deleted')
        
def buy_product(request, product_id):
    if hasattr(request.user, 'customer') and request.user.customer:
        customer = request.user.customer
    else:
        return HttpResponse('Not allowed', status=403)
    
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return HttpResponse('Product not found', status=404)
    
    # customer = get_object_or_404(Customer, user=request.user)
    # product = get_object_or_404(Product, id=product.id)

    if request.POST:
        form = PurchaseItemForm(request.POST)
        if form.is_valid():
            # print(form.data)
            # print(form.cleaned_data)
            quantity = form.cleaned_data.get("quantity", 1)
            
            if product.storage_quantity >= quantity > 0:
                product.storage_quantity -= quantity
                product.save()
                
                purchase = Purchase.objects.create(purchase_date=datetime.date.today(), customer=customer)
                PurchaseItem.objects.create(purchase=purchase, product=product, quantity=quantity)
    
        return redirect('product_details', product_id=product.id)
    
    
def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Customer.objects.create(
            #     first_name = form.cleaned_data.get("first_name"),
            #     last_name = form.cleaned_data.get("last_name"),
            #     email = form.cleaned_data.get("email"),
            #     age = form.cleaned_data.get("age"),
            #     user = user
            # )
            login(request, user)
            return redirect('/')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


# def cart_details(request):
#     # customer = get_object_or_404(Customer, user=request.user)
#     if hasattr(request.user, 'customer') and request.user.customer:
#         customer = request.user.customer
#         print(customer)
#     else:
#         return HttpResponse('Not allowed', status=403)

#     # try:
#     #     cart = Cart.objects.get(customer=customer)
#     # except Cart.DoesNotExist:
#     #     return HttpResponse('No cart', status=404)

#     cart, created = Cart.objects.get_or_create(customer=customer)
#     return render(request, 'shopping/cart_details.html', {'cart': cart})

def cart_details(request):
    if hasattr(request.user, 'customer') and request.user.customer:
        customer = request.user.customer
    else:
        return HttpResponse('Not allowed', status=403)
    
    # try:
    #     cart = ShopingCart.objects.get(id=cart_id)
    # except ShopingCart.DoesNotExist:
    #     return HttpResponse("No cart found!", status=404)
    # context = {'cart': cart}
    # return render(request, 'shopping/cart_details.html', context)


    cart, created = ShopingCart.objects.get_or_create(customer=customer)
    context = {'cart': cart,
               'form':PurchaseItemForm}
    return render(request, 'shopping/cart_details.html', context)


def add_product_to_cart(request, product_id):
    if hasattr(request.user, 'customer') and request.user.customer:
        customer = request.user.customer
    else:
        return HttpResponse('Not allowed', status=403)
    
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return HttpResponse('Product not found', status=404)
    
    # customer = get_object_or_404(Customer, user=request.user)
    # product = get_object_or_404(Product, id=product.id)

    if request.POST:
        form = PurchaseItemForm(request.POST)
        if form.is_valid():
            # print(form.data)
            # print(form.cleaned_data)
            quantity = form.cleaned_data.get("quantity", 1)
            
            if product.storage_quantity >= quantity > 0:
                product.storage_quantity -= quantity
                product.save()
                
                shopping_cart, created = ShopingCart.objects.get_or_create(customer=customer)
                cart_item, created = CartItem.objects.get_or_create(shopping_cart=shopping_cart, product=product)
                if created:
                    cart_item.quantity = quantity
                else:
                    cart_item.quantity += quantity
                    
                cart_item.save()
    
        return redirect('product_details', product_id=product.id)
    
    
def remove_product_from_cart(request, cart_item_id):
    try:
        cart_item = CartItem.objects.get(id=cart_item_id)
    except CartItem.DoesNotExist:
        return HttpResponse('Product not found', status=404)
    print(cart_item.product.id)
    try:
        product = Product.objects.get(id=cart_item.product.id)
    except Product.DoesNotExist:
        return HttpResponse('Product not found', status=404)
    
    product.storage_quantity += cart_item.quantity
    product.save()
    cart_item.delete()
    return redirect('cart_details')

def update_product_in_cart(request, cart_item_id):
    # print(cart_item_id)
    # print("update")
    # try:
    #     cart_item = CartItem.objects.get(id=cart_item_id)
    # except CartItem.DoesNotExist:
    #     return HttpResponse('Product not found', status=404)
    
    cart_item = get_object_or_404(CartItem, id=cart_item.id, cart__customer__user=request.user)
    
    if request.POST:
        form = PurchaseItemForm(request.POST)
        if form.is_valid():
            # print(form.data)
            # print(form.cleaned_data)
            quantity = form.cleaned_data.get("quantity", 1)
            
            if cart_item.product.storage_quantity >= quantity > 0:
                cart_item.quantity += quantity
                cart_item.save()
                cart_item.product.storage_quantity -= quantity
                cart_item.product.save()
                messages.success(request, f"Update was successful.")
    return redirect('cart_details')

def create_purchase(request):
    if hasattr(request.user, 'customer') and request.user.customer:
        customer = request.user.customer
    else:
        return HttpResponse('Not allowed', status=403)

    cart = ShopingCart.objects.get(customer=customer)
    
    purchase = Purchase.objects.create(purchase_date=datetime.date.today(), customer=customer)
    for item in cart.items.all():
        PurchaseItem.objects.create(purchase=purchase, product=item.product, quantity=item.quantity)
    cart.delete()  #.items.all().delete()
    # return redirect('cart_details')
    context = {"purchase":purchase}
    return render(request, 'shopping/purchase_successful.html', context)

# path('cart/checkout/', views.checkout_cart, name='checkout_cart'),
# path('cart/checkout/success', views.checkout_cart_success, name='checkout_cart_success'),

# def checkout_cart(request):
#     customer = get_object_or_404(Customer, user=request.user)
#     cart = get_object_or_404(Cart, customer=customer)

#     purchase = Purchase.objects.create(purchase_date=datetime.date.today(), customer=customer)
#     for item in cart.items.all():
#         PurchaseItem.objects.create(purchase=purchase, product=item.product, quantity=item.quantity)
#         item.product.storage_quantity -= item.quantity
#         item.product.save()

#     cart.items.all().delete()

#     return redirect('checkout_cart_success')


# def checkout_cart_success(request):
#     return render(request, 'shopping/checkout_success.html')

# path('cart/checkout/', views.checkout_cart, name='checkout_cart'),
# path('cart/checkout/success', views.checkout_cart_success, name='checkout_cart_success'),

# def checkout_cart(request):
#     customer = get_object_or_404(Customer, user=request.user)
#     cart = get_object_or_404(Cart, customer=customer)

#     purchase = Purchase.objects.create(purchase_date=datetime.date.today(), customer=customer)
#     for item in cart.items.all():
#         PurchaseItem.objects.create(purchase=purchase, product=item.product, quantity=item.quantity)
#         item.product.storage_quantity -= item.quantity
#         item.product.save()

#     cart.items.all().delete()

#     request.session['last_purchase_id'] = purchase.id

#     return redirect('checkout_cart_success')


# def checkout_cart_success(request):
#     purchase_id = request.session.pop('last_purchase_id', None)
#     purchase = None
#     items = []

#     if purchase_id:
#         purchase = get_object_or_404(Purchase, id=purchase_id)
#         items = purchase.items.select_related('product')

#     return render(request, 'shopping/checkout_success.html', {
#         'purchase': purchase,
#         'items': items
#     })

# path('cart/checkout/', views.checkout_cart, name='checkout_cart'),
# path('cart/checkout/success/<int:purchase_id>/', views.checkout_cart_success, name='checkout_cart_success'),

# def checkout_cart(request):
#     customer = get_object_or_404(Customer, user=request.user)
#     cart = get_object_or_404(Cart, customer=customer)

#     purchase = Purchase.objects.create(purchase_date=datetime.date.today(), customer=customer)
#     for item in cart.items.all():
#         PurchaseItem.objects.create(purchase=purchase, product=item.product, quantity=item.quantity)
#         item.product.storage_quantity -= item.quantity
#         item.product.save()

#     cart.items.all().delete()

#     return redirect('checkout_cart_success', purchase_id=purchase.id)


# def checkout_cart_success(request, purchase_id):
#     purchase = get_object_or_404(Purchase, id=purchase_id, customer__user=request.user)
#     items = purchase.items.select_related('product')

#     return render(request, 'shopping/checkout_success.html', {
#         'purchase': purchase,
#         'items': items
#     })

# path('cart/checkout/', views.checkout_cart, name='checkout_cart'),

# def checkout_cart(request):
#     customer = get_object_or_404(Customer, user=request.user)
#     cart = get_object_or_404(Cart, customer=customer)

#     purchase = Purchase.objects.create(purchase_date=datetime.date.today(), customer=customer)
#     for item in cart.items.all():
#         PurchaseItem.objects.create(purchase=purchase, product=item.product, quantity=item.quantity)
#         item.product.storage_quantity -= item.quantity
#         item.product.save()

#     cart.items.all().delete()

#     items = purchase.items.select_related('product')

#     return render(request, 'shopping/checkout_success.html', {
#         'purchase': purchase,
#         'items': items
#     })

# def set_language_hu(request):
#     translation.activate('hu')
#     response = redirect('page2')
#     response.set_cookie(settings.LANGUAGE_COOKIE_NAME, 'hu')
#     return response

# def set_language_en(request):
#     translation.activate('en')
#     response = redirect('page2')
#     response.set_cookie(settings.LANGUAGE_COOKIE_NAME, 'en')
#     return response

# def set_language_de(request):
#     translation.activate('de')
#     response = redirect('page2')
#     response.set_cookie(settings.LANGUAGE_COOKIE_NAME, 'de')
#     return response

# def set_language(request, language_code):
#     translation.activate(language_code)
#     response = redirect('page2')
#     response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language_code)
#     return response

def set_language2(request):
    # print(request.GET)
    # print(request.POST)
    # print(request.META)
    language_code = request.POST.get('language')
    print('CODE', language_code)
    translation.activate(language_code)
    response = redirect(request.META.get('HTTP_REFERER', '/'))
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language_code)
    return response