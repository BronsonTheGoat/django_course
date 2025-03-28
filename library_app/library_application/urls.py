from django.urls import path, include
from .views import index, get_books, get_book_details

urlpatterns = [
    path("", index, name="index"),
    path("books", get_books, name="book_list"),
    path("books/<book_id>", get_book_details, name="book_details"),
]
