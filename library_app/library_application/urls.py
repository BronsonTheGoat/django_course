from django.urls import path, include
from .views import index, get_books, get_book_details, get_authors, get_author_details

urlpatterns = [
    path("", index, name="index"),
    path("books", get_books, name="book_list"),
    path("books/<book_id>", get_book_details, name="book_details"),
    path("authors", get_authors, name="author_list"),
    path("auhtors/<author_id>", get_author_details, name="author_details"),
]
