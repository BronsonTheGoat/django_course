from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
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
    expiry_date = forms.DateField(
    widget=forms.DateInput(attrs={'type': 'date'}),
    required=False
    )
    
    class Meta:
        model = Product
        fields = '__all__'
        
class PurchaseItemForm(forms.Form):
    quantity = forms.IntegerField(min_value=1)
    
class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Email'})
    )
    age = forms.IntegerField(required=True, validators=[MinValueValidator(18), MaxValueValidator(100)])
    phone_number = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "first_name", "last_name")
        # widgets = {
        #     'username': forms.TextInput(attrs={'placeholder': 'Username'}),
        #     'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
        # }
        
    def save(self, commit=True):
        user = super().save(commit=False)

        if commit:
            user.save()

        customer = Customer(
            user=user,
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            email=self.cleaned_data['email'],
            age=self.cleaned_data['age'],
            phone_number=self.cleaned_data.get('phone_number', None)
        )
        if commit:
            customer.save()

        return user