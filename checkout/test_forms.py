from django.test import TestCase
from .forms import MakePaymentForm, OrderForm


class TestMakePaymentForm(TestCase):

    def test_fill_out_valid_form(self):
        form = MakePaymentForm({'credit_card_number': '4242424242424242', 'cvv':
                                '111', 'expiry_month': '12', 'expiry_year': 
                                '2019', 'stripe_id': 
                                'ch_1F7iRT2eZvKYlo2CuFhkV03z'})
        self.assertTrue(form.is_valid())

    def test_correct_error_message(self):
        form = MakePaymentForm({'credit_card_number': ''})
        self.assertFalse(form.is_valid())

class TestOrderForm(TestCase):

    def test_fill_out_valid_form(self):
        form = OrderForm({'full_name': 'string', 'phone_number': '01234567890', 
                          'country': 'string', 'postcode': 'string',
                          'town_or_city': 'string', 'street_address1': 'string',
                          'street_address2': 'string', 'county': 'string'})
        self.assertTrue(form.is_valid())

    def test_correct_error_message_empty_field(self):
        form = OrderForm({'full_name': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['full_name'], [u'This field is required.'])
