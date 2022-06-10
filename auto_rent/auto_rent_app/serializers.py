from rest_framework import serializers
from .models import *


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = '__all__'


class BrandsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBrands
        fields = '__all__'


class CarDetailSerializer(serializers.ModelSerializer):
    brands = BrandsSerializer(required=True)

    class Meta:
        model = Cars
        fields = '__all__'
