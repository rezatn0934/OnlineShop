from django.db import models
from django.core.validators import MinValueValidator
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name='categories')

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(verbose_name=_("Product Image"), upload_to='images/category/')
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(1)])
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT)
    color = models.ForeignKey(Color, on_delete=models.PROTECT)
    product_year = models.DateField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    is_active = models.BooleanField(default=True)

    def img_preview(self):
        if self.image:
            return mark_safe(f'<img src = "{self.image.url}" width = "150" height="150"/> ')

    class Meta:
        ordering = ['name']

    def __str__(self) -> str:
        return self.name