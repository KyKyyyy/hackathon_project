
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from application.product.views import CategoryView, ProductView, CommentView

router = DefaultRouter()
router.register('category', CategoryView)
router.register('review', CommentView)
router.register('', ProductView)

urlpatterns = [
    path('', include(router.urls)),

]
