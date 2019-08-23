from django.test import TestCase
from .forms import UserLoginForm, UserRegistrationForm


class TestUserLoginForm(TestCase):

    def test_fill_out_valid_form(self):
        form = UserLoginForm({'username': 'username', 'password': 'password'})
        self.assertTrue(form.is_valid())

    def test_correct_error_message_empty_field(self):
        form = UserLoginForm({'username': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], [u'This field is required.'])


class TestUserRegistrationForm(TestCase):

    def test_fill_out_valid_form(self):
        form = UserRegistrationForm({'username': 'username', 'email':
                                     'email@email.com', 'password1': 'abc',
                                     'password2': 'abc'})
        self.assertTrue(form.is_valid())

    def test_correct_error_message_empty_field(self):
        form = UserRegistrationForm({'username': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], [u'This field is required.'])

    def test_correct_error_message_different_passwords(self):
        form = UserRegistrationForm({'username': 'username', 'email':
                                     'email@email.com', 'password1': 'abc',
                                     'password2': 'def'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password2'], [u'Passwords must match'])
