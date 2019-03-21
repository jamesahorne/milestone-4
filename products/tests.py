from django.test import TestCase
from .models import Product

class ProductTests(TestCase):
    ''' Product model tests '''

    def test_str(self):
        test_name = Product(name='Product name')
        self.assertEqual(str(test_name), 'Product name')
