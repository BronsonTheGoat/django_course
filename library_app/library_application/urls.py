from django.urls import path, include
from . import views 

urlpatterns = [
    path("", views.index, name="index"),
    path("books", views.get_books, name="book_list"),
    path("books/add", views.add_book, name="book_add"),
    path("books/<book_id>", views.get_book_details, name="book_details"),
    path("books/<book_id>/update", views.update_book, name="book_update"),
    path("authors", views.get_authors, name="author_list"),
    path("auhtors/<author_id>", views.get_author_details, name="author_details"),
    path("books/<int:book_id>/borrow", views.borrow_book, name="borrow_book"),
    path("books/<int:book_id>/return", views.return_book, name="return_book"),
]
