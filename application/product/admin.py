from django.contrib import admin

# Register your models here.

from application.product.models import Product, Category, Image, Comment, Like

# admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Image)
admin.site.register(Like)
admin.site.register(Comment)


class ImageInAdmin(admin.TabularInline):
    model = Image
    fields = ['image']
    max_num = 3


class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInAdmin]


admin.site.register(Product, ProductAdmin)
