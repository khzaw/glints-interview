from django.views.generic.detail import DetailView
from django.shortcuts import render
from rest_framework import viewsets
from .models import Author
from .serializers import AuthorSerializer


class AuthorDetailView(DetailView):
    model = Author


class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint for authors
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer