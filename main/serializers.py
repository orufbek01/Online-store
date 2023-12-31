from rest_framework import serializers
from .models import *


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = User
        fields = '__all__'


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class Sub_CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Sub_category
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'


class CardSerializers(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'


class SavedSerializers(serializers.ModelSerializer):
    class Meta:
        model = Saved
        fields = '__all__'


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Saved
        fields = '__all__'


class AddressSerializers(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class OficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = '__all__'


