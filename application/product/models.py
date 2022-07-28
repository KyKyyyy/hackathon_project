from django.db import models

# Create your models here.

from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(primary_key=True, unique=True, blank=True)
    pre_category = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,
                                     related_name='post_categories')

    def save(self, *args, **kwargs):
        self.slug = ''
        for i in self.name.lower():
            if i == ' ':
                i = '_'
            self.slug += i
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        if self.pre_category:
            return f'{self.pre_category} --> {self.slug}'
        else:
            return f'{self.slug}'

    class Meta:
        ordering = ['slug']
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    quantity = models.PositiveIntegerField(default=1)
    # media = models.ImageField(upload_to='products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return f'{self.category} --> {self.name}'

    class Meta:
        ordering = ['id']


class Image(models.Model):
    image = models.ImageField(upload_to='products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='images')


class Like(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='likes')
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='likes')
    like = models.BooleanField('like', default=False)

    def __str__(self):
        return f'{self.like}'


class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE,
                              related_name='comments')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='comments')
    text = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
