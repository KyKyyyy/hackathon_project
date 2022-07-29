from django.contrib import admin

# Register your models here.
from application.cart.models import Order

# admin.site.register(Cart)
admin.site.register(Order)
