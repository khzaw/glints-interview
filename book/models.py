from __future__ import unicode_literals

from django.db import models
from author.models import Author


class Book(models.Model):
    title = models.CharField(max_length=1024)
    description = models.TextField(blank=True)
    author = models.ForeignKey(Author)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)
    url = models.URLField(blank=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title