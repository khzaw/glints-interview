from __future__ import unicode_literals
from model_utils.models import TimeStampedModel
from django.db import models
from author.models import Author


class Book(TimeStampedModel):
    title = models.CharField(max_length=1024)
    description = models.TextField(blank=True)
    author = models.ForeignKey(Author, blank=True, null=True, related_name='books')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)
    image = models.TextField(blank=True)
    tags = models.ManyToManyField('Tag', related_name='books', blank=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_books(self, tag):
        return Book.objects.filter(tags__name=tag)



class Tag(TimeStampedModel):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name