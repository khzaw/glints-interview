from __future__ import unicode_literals

from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=1024)
    bio = models.TextField()