from rest_framework import serializers

from django.contrib.auth.models import User
from .models import Owner, Predio


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')


class PredioSerializer(serializers.ModelSerializer):

    class Meta:
        ordering = ['-document']
        model = Predio
        fields = ("document", "matricula", "category", "Location", "owner")
        extra_kwargs = {'books': {'required': False}}

class OwnerSerializer(serializers.ModelSerializer):
    predios = PredioSerializer(many=True, read_only=True)

    class Meta:
        ordering = ['-document']
        model = Owner
        fields = ("document", "name", "phone", "email", "type_p", "predios")
        extra_kwargs = {'authors': {'required': False}}