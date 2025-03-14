from django.test import TestCase

from product.factories import CategoryFactory, ProductFactory
from product.serializers import ProductSerializer


class TestProductSerializer(TestCase):
    def setUp(self):
        self.category = CategoryFactory(title="sports")
        self.product_1 = ProductFactory(
            title="soccer ball", price=100, category=[self.category]
        )
        self.product_serializer = ProductSerializer(self.product_1)

    def test_product_serializer(self):
        serializer_data = self.product_serializer.data
        self.assertEqual(serializer_data["price"], 100)
        self.assertEqual(serializer_data["title"], "soccer ball")
        self.assertEqual(
            serializer_data["category"][0]["title"], "sports")
