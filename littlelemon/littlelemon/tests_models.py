from django.test import TestCase

from restaurant.models import *

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(
            title = 'test01',
            price = 80,
            inventory = 100
        )
        self.assertEqual(item.title, 'test01')