from django.test import TestCase

class TestViews(TestCase):
    def test_get_index_page(self):
        page = self.client.get('/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")

    def test_get_about_page(self):
        page = self.client.get('/about/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "about.html")

    def test_get_data_page(self):
        page = self.client.get('/data/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "data.html")
