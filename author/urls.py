from django.conf.urls import url, include
from .views import AuthorDetailView

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', AuthorDetailView.as_view(), name='detail'),
]