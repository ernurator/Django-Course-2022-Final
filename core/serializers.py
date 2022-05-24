from rest_framework import serializers

from . import models


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        exclude = ['id']
        read_only = ['created_at']


class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Journal
        exclude = ['id']
        read_only = ['created_at']
