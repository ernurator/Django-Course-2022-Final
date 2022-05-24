from rest_framework import serializers

from . import models


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}
