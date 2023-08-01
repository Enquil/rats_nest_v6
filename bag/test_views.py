from django.test import TestCase


class TestBagViews(TestCase):

    def test_bag_template_used(self):

        response = self.client.get('/bag/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html', 'base.html')
