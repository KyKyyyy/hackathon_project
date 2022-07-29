from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

from application.product.models import Product

User = get_user_model()


class Order(models.Model):
    item = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
    amount = models.PositiveIntegerField()
    # cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    total_price = models.PositiveIntegerField(blank=True)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')

    def save(self, *args, **kwargs):
        self.total_price = self.item.price * self.amount
        super().save(*args, **kwargs)
