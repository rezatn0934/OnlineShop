from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from model_bakery import baker
from store.models import Product, Category
from store.serializers import ProductSerializer


class TestProductViewCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.product = baker.make(Product, price=10.0, is_active=True, quantity=100)
        self.url = reverse('store:product_details', args=(self.product.slug,))

    def test_retrieve_product(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_serializer_data(self):
        response = self.client.get(self.url)
        self.assertEqual(response.data, ProductSerializer(self.product).data)

    def test_invalid_product(self):
        invalid_prod_url = reverse('store:product_details', args=('rdtcfvgbhjnkm',))
        response = self.client.get(invalid_prod_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
