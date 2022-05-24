from django.shortcuts import render

from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action

from . import serializers


class AuthenticationViewSet(ViewSet):
    @action(detail=False, methods=['POST'])
    def register(self, request):
        serializer = serializers.UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(user.password)
            user.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
