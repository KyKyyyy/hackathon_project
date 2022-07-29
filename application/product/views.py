

# Create your views here.

from rest_framework.permissions import IsAdminUser, AllowAny

from rest_framework.viewsets import ModelViewSet

from application.product.models import Category, Product
from application.product.serializers import CategorySerializer, ProductSerializer


class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # pagination_class = ...
    permission_classes = [AllowAny]


class ProductView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # pagination_class = ...
    permission_classes = [AllowAny]
