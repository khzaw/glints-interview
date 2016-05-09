from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, generics
from rest_framework.response import Response
from .serializers import BookSerializer
from .models import Book


class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'author_id'

