from django.http import HttpResponse
from django.shortcuts import render, loader

from .forms import BookForm
from .models import Book

# Create your views here.

def index(request):
    return render(request, 'index.html')

def get_books(request):
    books = Book.objects.all()
    form = BookForm(request.GET or None)
    if request.GET and form.is_valid():
        title = form.cleaned_data.get('title')
        author = form.cleaned_data.get('author')
        books = books.filter(
            title__contains=title,
            author__contains=author
        )

    context = {
        'form': form,
        'books': books
    }
    return render(request, 'books.html', context)

def get_book_details(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return HttpResponse("No book found!", status=404)
    context = {'book': book}
    return render(request, 'book_details.html', context)