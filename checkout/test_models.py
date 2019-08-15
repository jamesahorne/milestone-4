from django.test import TestCase
from .models import Order, OrderLineItem
from products.models import Product

class TestOrderModel(TestCase):
    def test_can_create_order(self):
        order = Order(full_name='Mark', phone_number='01234567890', 
                      country='United Kingdom', postcode='GU5 9JZ',
                      town_or_city='Guildford', 
                      street_address1='10 Street Name',
                      street_address2='Somewhere', county='Surrey')
        order.save()
        self.assertEqual(order.full_name, 'Mark')
        self.assertEqual(order.phone_number, '01234567890')
        self.assertEqual(order.country, 'United Kingdom')
        self.assertEqual(order.postcode, 'GU5 9JZ')
        self.assertEqual(order.town_or_city, 'Guildford')
        self.assertEqual(order.street_address1, '10 Street Name')
        self.assertEqual(order.street_address2, 'Somewhere')
        self.assertEqual(order.county, 'Surrey')

class TestOrderLineItemModel(TestCase):
    def test_order_not_Null(self):
        order = Order(full_name='Mark', phone_number='01234567890', 
                      country='United Kingdom', postcode='GU5 9JZ',
                      town_or_city='Guildford', 
                      street_address1='10 Street Name',
                      street_address2='Somewhere', county='Surrey')
        order.save()
        self.assertIsNotNone(order)

    def test_product_model(self):
        product = Product(name='Bug', description='Bug description', 
                          price=10.00)
        self.assertIsNotNone(product)
