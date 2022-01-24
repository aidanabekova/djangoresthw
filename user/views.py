from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.authtoken.admin import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

from user.serializer import UserRegisterValidateSerializer


@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        serializer = UserRegisterValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
                            data={'errors': serializer.errors})
        User.objects.create_user(**request.data)
        return Response(data={'user created'}, status=201)


@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        user = authenticate(**request.data)
        if user:
            try:
                token = Token.objects.get(user=user)
            except Token.DoesNotExist:
                token = Token.objects.create(user=user)
            return Response(data={'token': token.key})
        return Response(data={'user not found'}, status=404)

