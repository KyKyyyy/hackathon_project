
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from application.product.views import CategoryView, ProductView

router = DefaultRouter()
router.register('', ProductView)
router.register('category', CategoryView)

urlpatterns = [
    path('', include(router.urls)),
]
