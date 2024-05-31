from rest_framework import serializers

from .models import Review, Product, Category
from rest_framework import generics

class ProductSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=150)
    price = serializers.IntegerField()
    category_id = serializers.IntegerField()
    review_id = serializers.IntegerField()

class ReviewSerializers(serializers.Serializer):
    content = serializers.CharField(max_length=680)


class CategorySerializers(serializers.Serializer):
    category_name = serializers.CharField(max_length=150)