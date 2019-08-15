from django.test import TestCase
from django.contrib.auth.models import User

class TestViews(TestCase):
    def test_get_checkout_page(self):
        user = User.objects.create_user(
            username='username',
            email='username@example.com',
            password='password')
        self.client.login(username='username', password='password')
        page = self.client.get('/checkout/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "checkout.html")
