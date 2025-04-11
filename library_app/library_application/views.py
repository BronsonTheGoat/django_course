from django.http import HttpResponse
from django.shortcuts import render, loader, redirect

from .forms import BookForm, BookAddForm, AuthorForm
from .models import Book, Author

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

def get_authors(request):
    authors = Author.objects.all()
    form = AuthorForm(request.GET or None)
    if request.GET and form.is_valid():
        name = form.cleaned_data.get('name')
        birth_date = form.cleaned_data.get('birth_date')
        birth_place = form.cleaned_data.get('birth_place')
        authors = authors.filter(
            name__contains=name,
            birth_date__contains=birth_date,
            birth_place__contains=birth_place
        )

    context = {
        'form': form,
        'authors': authors
    }
    return render(request, 'authors.html', context)

def get_author_details(request, author_id):
    try:
        author = Author.objects.get(id=author_id)
    except Author.DoesNotExist:
        return HttpResponse("No author found!", status=404)
    context = {'author': author}
    return render(request, 'author_details.html', context)

def add_book(request):
    form = BookAddForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect("book_list")
        
    context = {"form":BookAddForm()}
    return render(request, "book_add.html", context)

def update_book(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return HttpResponse('Product not found', status=404)

    if request.POST:
        form = BookAddForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            print('DATA:')
            print(form.data)
            print(form.cleaned_data)
            print('____________')
            form.save()
            return redirect('book_details', book_id=book_id)

    form = BookAddForm(instance=book)
    context = {
        'form': form,
        'book': book
    }
    return render(request, 'book_update.html', context)