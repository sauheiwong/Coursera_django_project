from django.test import TestCase

from restaurant.models import *

class MenuViewTest(TestCase):
    def setUp(self):
        self.item_1 = Menu.objects.create(
            title = 'test01',
            price = 80,
            inventory = 100
        )
        self.item_2 = Menu.objects.create(
            title = 'test02',
            price = 160,
            inventory = 200
        )

    def test_getall(self):
        self.assertEqual(self.item_1.title, 'test01')
        self.assertNotEqual(self.item_1.price, 80)