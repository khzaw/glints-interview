from django.conf.urls import url, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'tags', TagViewSet)


urlpatterns = [
    url(r'^', include(router.urls), name="index"),
]