from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import *
# Create your views here.


class CarsViewSet(viewsets.ModelViewSet):
    queryset = Cars.objects.all()
    serializer_class = CarSerializer


# class CarsAPIList(generics.ListAPIView):
#     queryset = Cars.objects.all()
#     serializer_class = CarDetailSerializer
