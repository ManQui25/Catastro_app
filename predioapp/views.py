from django.shortcuts import render
from rest_framework import routers, serializers, viewsets, status, generics
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializer import PredioSerializer, OwnerSerializer, UserSerializer
from .models import Predio, Owner
from rest_framework import filters


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class PredioViewSet(viewsets.ModelViewSet):
    """
    List all workers, or create a new worker.
    """
    queryset = Predio.objects.all()
    serializer_class = PredioSerializer


class OwnerViewSet(viewsets.ModelViewSet):
    """
    List all workkers, or create a new worker.
    """
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['document']

