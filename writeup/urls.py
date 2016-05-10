from django.conf.urls import url
from .views import WriteUpTemplateView

urlpatterns = [
    url(r'^$', WriteUpTemplateView.as_view(), name='index'),
]