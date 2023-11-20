from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer): #ModelSerializer is a base class for class DataSerializer
    class Meta:
        model=Product
        fields=('name','description')