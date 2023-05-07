from django.urls import path
from . import views
from .views import BookListCreate, BookRetrieveUpdateDestroy, AuthorListCreate, AuthorRetrieveUpdateDestroy

urlpatterns = [
    path('search/', views.search, name='search'),
    path('', views.get_all_books, name='get_all_books'),
    path('create/', views.create_book, name='create_book'),
    path('books/', BookListCreate.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroy.as_view(), name='book-retrieve-update-destroy'),
    path('authors/', AuthorListCreate.as_view(), name='author-list-create'),
    path('authors/<int:pk>/', AuthorRetrieveUpdateDestroy.as_view(), name='author-retrieve-update-destroy'),
]