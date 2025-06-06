from django import forms

from .models import Book, Author

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        exclude = ['cover_image']
        
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
        
class BookAddForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'