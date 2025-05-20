from .models import*
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        table=Users_tb
        fields="__all__"


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        table=Task_tb
        fields="__all__"