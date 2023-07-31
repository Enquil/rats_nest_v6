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
