from django.db.models import Q
from django.http import JsonResponse
from rest_framework import generics
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer


class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorListCreate(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer











def search(request):
    if request.method == 'GET':
        query = request.GET.get('q', '')

        if query:
            results = Book.objects.filter(Q(title__icontains=query) | Q(author__name__icontains=query))
        else:
            results = []

        response_data = [{'id': book.id, 'title': book.title, 'author': book.author.name} for book in results]
        return JsonResponse({'data': response_data})
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)


def get_all_books(request):
    if request.method == 'GET':
        books = Book.objects.all()
        response_data = [{'id': book.id, 'title': book.title, 'author': book.author.name} for book in books]
        return JsonResponse({'data': response_data})
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)


def create_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author_name = request.POST.get('author')
        author, _ = Author.objects.get_or_create(name=author_name)
        book = Book.objects.create(title=title, author=author)
        book.save()

        return JsonResponse({'message': 'Book created successfully', 'id': book.id})
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
