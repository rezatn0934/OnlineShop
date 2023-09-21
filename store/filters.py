from django_filters.rest_framework import FilterSet
from .models import Product


class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = {
            'category__name': ['in', 'startswith'],
            'price': ['gt', 'lt'],
            'product_year': ['gt', 'lt'],
        }
