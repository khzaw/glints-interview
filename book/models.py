from __future__ import unicode_literals

from django.db import models
from author.models import Author


class Book(models.Model):
    title = models.CharField(max_length=1024)
    description = models.TextField()
    author = models.ForeignKey(Author)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    url = models.URLField()


    @property
    def price(self):
        return "S$%s" % self.price