from django import forms

from .models import Product, Customer

class CustomerForm(forms.Form):
    first_name = forms.CharField(max_length=10, required=True)
    last_name = forms.CharField(max_length=20, required=False)
    email = forms.EmailField(max_length=200, required=False)
    # phone_number = forms.CharField(max_length=15, required=False)
    # email = forms.CharField(max_length=200, required=False)
    
class ProductForm(forms.Form):
    product_name = forms.CharField(max_length=30, required=True)
    # price = forms.CharField(max_length=20, required=False)
    
class ProductForm2(forms.ModelForm):
    class Meta:
        model = Product
        # fields = ['name', 'price']
        fields = '__all__'
        # exclude = ['expiry_date']
        
class CustomerAddForm(forms.Form):
    first_name = forms.CharField(max_length=10, required=True)
    last_name = forms.CharField(max_length=20, required=True)
    email = forms.EmailField(max_length=200, required=True)
    age = forms.IntegerField(required=True)
    phone_number = forms.CharField(max_length=15, required=False)
    
class CustomerAddForm2(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        
class ProductAddForm2(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'