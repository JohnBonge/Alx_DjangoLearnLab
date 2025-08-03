from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

# List-only view (keep for filtered view if needed)
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Full CRUD viewset
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
