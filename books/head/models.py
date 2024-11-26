from django.db import models


STATUS = [('в наличии', 'в наличии'),
          ('выдана', 'выдана')]

class Book(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    author = models.CharField(max_length=255, null=True, blank=True)
    year = models.PositiveIntegerField(null=True, blank=True)
    status = models.CharField(max_length=255, choices=STATUS, blank=True)