from rest_framework import serializers, viewsets
from book.models import Book, Tag
from author.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        exclude = ('created', 'modified')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        exclude = ('created', 'modified')


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    tags = TagSerializer(many=True)
    class Meta:
        model = Book
        depth = 1
        exclude = ('created', 'modified')



class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint for authors
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer