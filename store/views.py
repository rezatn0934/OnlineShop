from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView

# Create your views here.

from .models import Product
from .serializers import ProductSerializer
from .filters import ProductFilter


class ProductListView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'description']

    def get_serializer_context(self):
        return {'request': self.request}


class ProductDetail(RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
