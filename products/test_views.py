from django.test import TestCase


class TestProductsViews(TestCase):

    def test_products_template_used(self):

        response = self.client.get('/products/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'products/products.html', 'base.html'
        )
