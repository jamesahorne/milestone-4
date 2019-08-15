from django.test import TestCase
from .models import Product, Ticket

class TestProductModel(TestCase):
    def test_product_model(self):
        product = Product(name='Bug', description='Bug description', 
                          price=10.00)
        self.assertEqual(product.name, 'Bug')
        self.assertEqual(product.description, 'Bug description')
        self.assertEqual(product.price, 10.00)

class TestTicketModel(TestCase):
    def test_can_create_ticket(self):
        ticket = Ticket(type='Bug', issue_name='Test Issue Name', 
                        description='Test description', urgent='True')
        ticket.save()
        self.assertEqual(ticket.type, 'Bug')
        self.assertEqual(ticket.issue_name, 'Test Issue Name')
        self.assertEqual(ticket.description, 'Test description')
        self.assertTrue(ticket.urgent)

    def test_status_defaults_to_ToDo(self):
        ticket = Ticket(type='Bug', issue_name='Test Issue Name', 
                        description='Test description', urgent='True')
        ticket.save()
        self.assertEqual(ticket.issue_name, 'Test Issue Name')
        self.assertEqual(ticket.status, 'ToDo')
