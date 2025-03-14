from django.test import TestCase

from product.factories import CategoryFactory, ProductFactory
from product.serializers import CategorySerializer


class TestCategorySerializer(TestCase):
    def setUp(self):
        self.category = CategoryFactory(title="sports")
        self.category_serializer = CategorySerializer(self.category)

    def test_order_serializer(self):
        serializer_data = self.category_serializer.data

        self.assertEqual(serializer_data["title"], "sports")
