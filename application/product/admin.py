from django.contrib import admin

# Register your models here.

from application.product.models import Product, Category, Image

# admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Image)


class ImageInAdmin(admin.TabularInline):
    model = Image
    fields = ['image']
    max_num = 3

class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInAdmin]

admin.site.register(Product, ProductAdmin)
