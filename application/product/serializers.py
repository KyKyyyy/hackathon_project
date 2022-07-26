
from rest_framework import serializers

from application.product.models import Category, Product, Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['image']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        requests = self.context.get('request')
        images = requests.FILES
        for i in range(10):
            product = Product.objects.create(**validated_data)
        print(images)
        for image in images.getlist('images'):
            Image.objects.create(product=product, image=image)

        return product
