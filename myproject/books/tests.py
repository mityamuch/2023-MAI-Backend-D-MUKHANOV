from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import patch, MagicMock

from .models import Author, Book
from .views import search, get_all_books, create_book
from .factories import AuthorFactory, BookFactory


class BookViewTests(TestCase):

    def setUp(self):
        self.client = Client()

    @patch('books.views.Book.objects.filter')
    def test_search(self, mock_filter):
        mock_book = BookFactory.build()
        mock_filter.return_value = [mock_book]
        response = self.client.get(reverse('search'), {'q': 'test'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),
                         {'data': [{'id': mock_book.id, 'title': mock_book.title, 'author': mock_book.author.name}]})

    @patch('books.views.Book.objects.all')
    def test_get_all_books(self, mock_all):
        mock_book = BookFactory.build()
        mock_all.return_value = [mock_book]
        response = self.client.get(reverse('get_all_books'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),
                         {'data': [{'id': mock_book.id, 'title': mock_book.title, 'author': mock_book.author.name}]})

    @patch('books.views.Author.objects.get_or_create')
    @patch('books.views.Book.objects.create')
    def test_create_book(self, mock_create, mock_get_or_create):
        mock_author = AuthorFactory.build()  # Build but do not save the object in the database
        mock_book = BookFactory.build(author=mock_author)  # Build but do not save the object in the database
        mock_get_or_create.return_value = (mock_author, True)
        mock_create.return_value = mock_book
        mock_book.id = 1
        mock_book.save = MagicMock()  # Mock the save() method
        response = self.client.post(reverse('create_book'), {'title': 'test', 'author': 'test'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'message': 'Book created successfully', 'id': mock_book.id})
