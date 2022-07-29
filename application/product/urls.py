
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from application.product.views import CategoryView, ProductView, CommentView

router = DefaultRouter()
router.register('all', ProductView)
router.register('review', CommentView)
router.register('', CategoryView)

urlpatterns = [
    path('', include(router.urls)),

]
