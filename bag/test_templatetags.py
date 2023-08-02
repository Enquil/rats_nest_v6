from django.test import TestCase
from .templatetags.bag_tools import calc_subtotal


class TestBagTools(TestCase):

    def test_calc_sub(self):

        price = 10.99
        quantity = 2

        self.assertEqual(calc_subtotal(price, quantity), 21.98)
