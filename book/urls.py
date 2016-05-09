from django.conf.urls import url, include
from .views import BookListView, BookDetailView


urlpatterns = [
    url(r'^$', BookListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', BookDetailView.as_view(), name='detail'),
]