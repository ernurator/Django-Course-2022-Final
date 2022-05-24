from django.db import models

from .base import BookJournalBase


class Book(BookJournalBase):
    num_pages = models.IntegerField()
    genre = models.CharField(max_length=50)
