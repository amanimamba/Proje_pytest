# myapp/serializers.py

from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'description']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=user
        fields=['id','nom','age']