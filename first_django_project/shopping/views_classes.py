from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.db.models import ProtectedError
from django.shortcuts import render
from django.urls import reverse

from .forms import CustomerForm, CustomerAddForm2, ProductForm, ProductForm2, ProductAddForm2, PurchaseItemForm
from .models import Customer, Product

class MyView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, this is a GET request!')

    def post(self, request, *args, **kwargs):
        return HttpResponse('Hello, this is a POST request!')
    
    
class MyTemplateView(TemplateView):
    template_name = 'shopping/index2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['greeting'] = 'Hello!'
        return context
    

class CustomerListView(ListView):
    model = Customer
    template_name = 'shopping/customers.html'
    context_object_name = 'customers'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # print(context)
        context['form'] = CustomerForm
        # print(context)
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        form = CustomerForm(self.request.GET or None)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            queryset = queryset.filter(
                    first_name__icontains=first_name,
                    last_name__icontains=last_name,
            )
            if email:
                queryset = queryset.filter(email=email)
        return queryset
    
    
class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'shopping/customer_details.html'
    context_object_name = 'customer'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PurchaseItemForm
        return context
    
    
class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerAddForm2
    template_name = 'shopping/customer_add.html'
    success_url = '/shopping/customers'

    def form_valid(self, form):
        # print('This form is valid: ')
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('customer_details2', kwargs={'pk': self.object.pk})
    
    
class ProductListView(ListView):
    model = Product
    template_name = 'shopping/products.html'
    context_object_name = 'products'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ProductForm
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        form = ProductForm(self.request.GET or None)
        if form.is_valid():
            product_name = form.cleaned_data.get('product_name')
            # price_lower = form.cleaned_data.get('price_limit_lower')
            # price_higher = form.cleaned_data.get('price_limit_higher')
            queryset = queryset.filter(
                name__contains=product_name,
                # price__gte=price_lower,
                # price__lte=price_higher
            )
        return queryset
    
    
class ProductDetailView(DetailView):
    model = Product
    template_name = 'shopping/product_details.html'
    context_object_name = 'product'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PurchaseItemForm
        return context
    
    
class ProductCreateView(CreateView):
    model = Product
    form_class = ProductAddForm2
    template_name = 'shopping/product_add.html'
    success_url = '/shopping/products'

    # def form_valid(self, form):
        # print('This form is valid: ')
        # return super().form_valid(form)
    
    # Optional
    def get_success_url(self):
        return reverse('product_details', kwargs={'pk': self.object.pk})
    
    
class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductAddForm2
    template_name = 'shopping/product_update.html'
    success_url = '/shopping/products'
    
    def get_success_url(self):
        return reverse('product_details', kwargs={'pk': self.object.pk})
    
    
class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'shopping/product_delete_success.html'
    success_url = '/shopping/products'
    # context_object_name = 'product2'
    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except ProtectedError:
            print("Can't be deleted")
            context = {
                "product": self.object,
                "error_message": "Can't be deleted",
            }
            return render(request, "shopping/product_details.html", context)