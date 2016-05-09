from django.conf.urls import url, include
from rest_framework import routers
from book.views import *
from author.views import *

router = routers.DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'authors', AuthorViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]