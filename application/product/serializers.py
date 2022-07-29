from django.db.models import Avg
from rest_framework import serializers

from . import models
from .models import Product, Category, Image


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['image']


class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        requests = self.context.get('request')
        images = requests.FILES

        product = Product.objects.create(**validated_data)
        print(images)
        for image in images.getlist('images'):
            Image.objects.create(product=product, image=image)
        return  product

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['likes'] = instance.likes.filter(like=True).count()
        return representation
