from django.contrib import admin

# Register your models here.

from application.product.models import Product, Category, Like, Comment

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Like)
admin.site.register(Comment)
