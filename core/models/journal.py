from django.db import models

from .base import BookJournalBase


class JournalTypeChoices(models.IntegerChoices):
    BULLET = 1
    FOOD = 2
    TRAVEL = 3
    SPORT = 4


class Journal(BookJournalBase):
    type = models.IntegerField(choices=JournalTypeChoices.choices)
    publisher = models.CharField(max_length=150)
