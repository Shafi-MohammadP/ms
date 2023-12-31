from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from product.models import Product, Color

# Create your models here.


class Variant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.product.product_name} - {self.color.color_name} "


class VariantImage(models.Model):
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='photos/variant', default='No image available')
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Image for {self.variant.product.product_name} - {self.variant.color.color_name} "
