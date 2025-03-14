#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.test import TestCase

from order.factories import OrderFactory, ProductFactory
from order.serializers import OrderSerializer


class TestOrderSerializer(TestCase):
    def setUp(self):
        self.product_test_1 = ProductFactory()
        self.product_test_2 = ProductFactory()

        self.order = OrderFactory(product=(self.product_test_1, self.product_test_2))
        self.order_serializer = OrderSerializer(self.order)

    def test_order_serializer(self):
        serializer_data = self.order_serializer.data
        self.assertEqual(
            serializer_data["product"][0]["title"], self.product_test_1.title)
        self.assertEqual(
            serializer_data["product"][1]["title"], self.product_test_2.title)
