from django.conf.urls import url, include
from rest_framework import routers
from book.views import BookViewSet

router = routers.DefaultRouter()
router.register(r'books', BookViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]