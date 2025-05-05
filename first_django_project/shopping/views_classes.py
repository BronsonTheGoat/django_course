from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.urls import reverse

from .forms import CustomerForm, CustomerAddForm2
from .models import Customer

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
    
    
class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerAddForm2
    template_name = 'shopping/customer_add.html'
    success_url = '/shopping/customers'

    def form_valid(self, form):
        # print('This form is valid: ')
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('customer_details', kwargs={'customer_id': self.object.pk})