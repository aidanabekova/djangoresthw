from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import User


class UserRegisterValidateSerializer(serializers.Serializer):
    username = serializers.CharField(min_length=5, max_length=15)
    password = serializers.CharField(min_length=5, max_length=15)

    def validate_username(self, username):
        users = User.objects.filter(username=username)
        if users.count():
            raise ValidationError("Such user already exists. Please,change your name!")
        return username

    # def validate_username(self, username):
    #     for i in username:
    #         if ord(i) >= 1040 and ord(i) <= 1103:  # проверка на русский язык
    #             raise ValidationError('Please use english only!')
    #     return username

