from django.test import TestCase
from .forms import TicketForm


class TestTicketForm(TestCase):

    def test_fill_out_valid_form(self):
        form = TicketForm({'type': 'Bug', 'issue_name': 'Test Issue Name', 
                           'description': 'Test description'})
        self.assertTrue(form.is_valid())

    def test_correct_error_message_empty_field(self):
        form = TicketForm({'issue_name': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['issue_name'], [u'This field is required.'])
