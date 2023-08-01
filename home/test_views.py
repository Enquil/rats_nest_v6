from django.test import TestCase


class TestHomeViews(TestCase):

    def test_home_template_used(self):

        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html', 'base.html')
