from django.test import TestCase
from .models import Ticket
from django.contrib.auth.models import User


class TestViews(TestCase):
    def test_get_all_tickets_page(self):
        page = self.client.get('/tickets/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "all_tickets.html")

    def test_get_buy_tickets_page(self):
        user = User.objects.create_user(
            username='username',
            email='username@example.com',
            password='password')
        self.client.login(username='username', password='password')
        page = self.client.get('/tickets/buy-tickets/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "buy_tickets.html")

    def test_get_bug_page(self):
        user = User.objects.create_user(
            username='username',
            email='username@example.com',
            password='password')
        self.client.login(username='username', password='password')
        page = self.client.get('/tickets/bug/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bug.html")

    def test_get_edit_ticket_page(self):
        user = User.objects.create_user(
            username='username',
            email='username@example.com',
            password='password')
        self.client.login(username='username', password='password')
        ticket = Ticket(type='Bug', issue_name='Test Issue Name',
                        description='Test description', urgent='True')
        ticket.save()
        page = self.client.get('/tickets/edit-ticket/{0}'.format(ticket.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "edit_ticket.html")

    def test_get_feature_page(self):
        user = User.objects.create_user(
            username='username',
            email='username@example.com',
            password='password')
        self.client.login(username='username', password='password')
        page = self.client.get('/tickets/feature/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "feature.html")

    def test_get_full_detail_page(self):
        ticket = Ticket(type='Bug', issue_name='Test Issue Name',
                        description='Test description', urgent='True')
        ticket.save()
        page = self.client.get('/tickets/full-detail/{0}'.format(ticket.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "full_details.html")

    def test_get_full_detail_404(self):
        ticket = Ticket(type='Bug', issue_name='Test Issue Name',
                        description='Test description', urgent='True')
        ticket.save()
        page = self.client.get('/tickets/full-detail/100')
        self.assertEqual(page.status_code, 404)

    def test_get_feature_or_upvote_page(self):
        user = User.objects.create_user(
            username='username',
            email='username@example.com',
            password='password')
        self.client.login(username='username', password='password')
        page = self.client.get('/tickets/feature-or-upvote/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "feature_or_upvote.html")

    def test_get_upvote_page(self):
        user = User.objects.create_user(
            username='username',
            email='username@example.com',
            password='password')
        self.client.login(username='username', password='password')
        page = self.client.get('/tickets/upvote/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "upvote.html")
