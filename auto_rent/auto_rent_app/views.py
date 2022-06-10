from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
# Create your views here.


class CarsViewSet(viewsets.ModelViewSet):
    queryset = Cars.objects.all()
    serializer_class = CarSerializer