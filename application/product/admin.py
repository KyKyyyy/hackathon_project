from django.contrib import admin

# Register your models here.

from application.product.models import Product, Category, Image, Review

# admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Image)
admin.site.register(Review)


class ImageInAdmin(admin.TabularInline):
    model = Image
    fields = ['image']
    max_num = 3


class ReviewInAdmin(admin.TabularInline):
    model = Review
    fields = ['comment']


class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInAdmin, ReviewInAdmin]


admin.site.register(Product, ProductAdmin)
