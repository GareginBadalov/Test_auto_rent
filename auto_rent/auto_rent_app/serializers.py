from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.relations import StringRelatedField
from rest_framework.serializers import ModelSerializer

from .models import *


class BrandsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBrands
        fields = ['label']


class CarSerializer(serializers.ModelSerializer):
    brand = BrandsSerializer(source='brand_id', read_only=True)


    class Meta:
        model = Cars
        fields = '__all__'




