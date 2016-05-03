from __future__ import unicode_literals
from model_utils.models import TimeStampedModel
from django.db import models


class Author(TimeStampedModel):
    name = models.CharField(max_length=1024)
    bio = models.TextField(blank=True)
    image = models.URLField(blank=True)


    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name