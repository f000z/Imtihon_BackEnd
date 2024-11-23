from rest_framework import serializers
from shop.models import Category, Furniture, ShopMainView


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']  # You can add other fields if necessary.


class FurnitureSerializer(serializers.ModelSerializer):
    category = CategorySerializer()  # Nested serializer for the category

    class Meta:
        model = Furniture
        fields = ['id', 'name', 'image', 'price', 'category']  # Add more fields as needed


class ShopMainViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopMainView
        fields = ['id', 'title', 'body', 'image']  # Add more fields as needed
