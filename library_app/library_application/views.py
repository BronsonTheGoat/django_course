from django.http import HttpResponse
from django.shortcuts import render, loader, redirect
from django.contrib.auth.decorators import permission_required
import datetime
from .forms import BookForm, BookAddForm, AuthorForm
from .models import Book, Author, Borrow

from django.utils.translation import gettext as _
from django.utils import translation

# Create your views here.

def index(request):
    translation.activate("hu")
    return render(request, 'index.html')

def get_books(request):
    translation.activate("hu")
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
    translation.activate("hu")
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return HttpResponse("No book found!", status=404)
    borrows = Borrow.objects.filter(book=book).order_by('-borrow_date')
    context = {
        'book': book,
        'borrows': borrows,
        }
    return render(request, 'book_details.html', context)

def get_authors(request):
    translation.activate("hu")
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
    translation.activate("hu")
    try:
        author = Author.objects.get(id=author_id)
    except Author.DoesNotExist:
        return HttpResponse("No author found!", status=404)
    context = {'author': author}
    return render(request, 'author_details.html', context)

@permission_required('book_add', raise_exception=True)
def add_book(request):
    translation.activate("hu")
    form = BookAddForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect("book_list")
        
    context = {"form":BookAddForm()}
    return render(request, "book_add.html", context)

def update_book(request, book_id):
    translation.activate("hu")
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

def borrow_book(request, book_id):
    translation.activate("hu")
    if request.user.is_authenticated:
        user = request.user
        print(user)
    else:
        return HttpResponse('Not allowed', status=403)
    
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return HttpResponse('Book not found', status=404)

    if request.method == "POST":
        if book.available == True:
            book.available = False
            book.save()
            
            Borrow.objects.create(borrow_date=datetime.date.today(), book=book, user=user)
    
        return redirect('book_details', book_id=book.id)
    
def return_book(request, book_id):
    translation.activate("hu")
    if not request.user.is_authenticated:
        return HttpResponse('Not allowed', status=403)

    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return HttpResponse('Book not found', status=404)

    borrow = Borrow.objects.filter(book=book, user=request.user, return_date__isnull=True).last()

    if not borrow:
        return HttpResponse("No active borrowing found.", status=404)

    if request.method == 'POST':
        book.available = True
        book.save()

        borrow.return_date = datetime.date.today()
        borrow.save()

        return redirect('book_details', book_id=book.id)

    return HttpResponse("Invalid request", status=400)

def profile(request):
    translation.activate("hu")
    if not request.user.is_authenticated:
        return HttpResponse('Not allowed', status=403)
    else:
        user = request.user
        borrow = Borrow.objects.filter(user=user, return_date__isnull=True)
        
    context = {
        'user': user,
        "borrow": borrow
    }
    return render(request, 'profile.html', context)