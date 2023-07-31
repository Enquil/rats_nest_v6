from django.test import TestCase
from .models import *


class TestCommonAbstractModel(TestCase):
    '''
    Tests for the Common Model (abstract)
    '''

    def setUp(self):

        test_domain = Domain.objects.create(
            name='test_domain',
            friendly_name='Test Domain',
        )
        test_domain.save()

    def test_str_method(self):
        '''
        Tests the str_method defined in the Common model
        '''

        test_domain = Domain.objects.get(id=1)

        self.assertEqual(
            str(test_domain), 'test_domain'
        )


class TestCategoryModel(TestCase):

    def setUp(self):

        test_domain = Domain.objects.create(
            name='test_domain',
            friendly_name='Test Domain',
        )
        test_domain.save()

        test_category = Category.objects.create(
            name='test_category',
            friendly_name='Test Category',
            domain=test_domain,
        )
        test_category.save()

    def test_category_get_friendly_name(self):

        test_category = Category.objects.get(id=1)

        self.assertEqual(
            Category.get_friendly_name(test_category), 'Test Category'
        )


class TestProductModel(TestCase):

    def setUp(self):

        test_domain = Domain.objects.create(
            name='test_domain',
            friendly_name='Test Domain',
        )
        test_domain.save()

        test_brand = Brand.objects.create(
            name='test_brand',
            friendly_name='Test Brand'
        )

        test_category = Category.objects.create(
            name='test_category',
            friendly_name='Test Category',
            domain=test_domain,
        )
        test_category.save()

    def test_product_save_method(self):

        test_brand = Brand.objects.get(id=1)
        test_category = Category.objects.get(id=1)

        test_product = Product.objects.create(
            name='test product',
            brand=test_brand,
            category=test_category,
            description='test description',
            has_sizes=False,
            price=99.99,
            rating=4,
            m_or_f='U',
        )
        test_product.save()

        # assert domain got auto-filled
        self.assertEqual(
            test_product.domain, 1
        )

        # Store last 5 digits of product.sku since they are random
        sku_rand_int = (
            test_product.sku[-5:-1] + test_product.sku[-1]
        )

        # assert test_product.sku returns 111 + sku_rand_int val
        self.assertEqual(
            test_product.sku,
            f'{test_product.domain}' +
            f'{test_product.brand.id}' +
            f'{test_product.category.id}' +
            sku_rand_int
        )
