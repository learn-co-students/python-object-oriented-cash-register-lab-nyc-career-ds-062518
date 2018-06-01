import unittest2 as unittest
from ipynb.fs.full.index import *

class TestObjectAttributes(unittest.TestCase):

    def test_shopping_cart_class(self):
        example_shc = ShoppingCart()
        self.assertEqual(type(example_shc), type(ShoppingCart()))

    def test_shopping_cart_initial_values(self):
        example_shc = ShoppingCart()
        self.assertEqual(example_shc._total, 0)
        self.assertItemsEqual(example_shc._items, [])

    def test_cash_register_initial_values_with_discount(self):
        example_shc = ShoppingCart(50)
        self.assertEqual(example_shc._total, 0)
        self.assertItemsEqual(example_shc._items, [])
        self.assertEqual(example_shc._employee_discount, 50)

    def test_cash_register_decorator_methods(self):
        example_shc = ShoppingCart(50)
        self.assertItemsEqual(example_shc.items, [])
        self.assertEqual(example_shc.employee_discount, 50)
        example_shc.total = 40
        example_shc.items = [{"name": "ice cream", "price": 5.00}]
        example_shc.employee_discount = 10
        self.assertEqual(example_shc.total, 40)
        self.assertItemsEqual(example_shc.items, [{"name": "ice cream", "price": 5.00}])
        self.assertEqual(example_shc._employee_discount, 10)

    def test_add_item_method(self):
        example_shc = ShoppingCart()
        self.assertEqual(example_shc.add_item("ice cream", 5.00), 5.00)
        self.assertItemsEqual(example_shc.items, [{"name": "ice cream", "price": 5.00}])

    def test_mean_item_price_method(self):
        example_shc = ShoppingCart()
        example_shc.add_item("ice cream", 5.00)
        example_shc.add_item("cereal", 10.00)
        example_shc.add_item("OJ", 4.00, 3)
        self.assertEqual(example_shc.mean_item_price(), 5.40)

    def test_median_item_price_odd_count_method(self):
        example_shc = ShoppingCart()
        example_shc.add_item("ice cream", 5.00)
        example_shc.add_item("cereal", 10.00)
        example_shc.add_item("OJ", 4.00, 3)
        self.assertEqual(example_shc.median_item_price(), 4.00)

    def test_median_item_price_even_count_method(self):
        example_shc_even_item_count = ShoppingCart()
        example_shc_even_item_count.add_item("ice cream", 5.00)
        example_shc_even_item_count.add_item("cereal", 10.00)
        example_shc_even_item_count.add_item("OJ", 4.00, 2)
        self.assertEqual(example_shc_even_item_count.median_item_price(), 4.50)

    def test_item_names_method(self):
        example_shc = ShoppingCart()
        example_shc.add_item("ice cream", 5.00)
        example_shc.add_item("cereal", 10.00)
        example_shc.add_item("OJ", 4.00, 3)
        self.assertItemsEqual(example_shc.item_names(), ["ice cream", "cereal", "OJ", "OJ", "OJ"])

    def test_apply_discount_method(self):
        example_shc = ShoppingCart(20)
        example_shc.total = 100
        self.assertEqual(example_shc.apply_discount(), 80)
        self.assertEqual(example_shc.total, 100)

    def test_void_last_item_method(self):
        example_shc_void_last_item = ShoppingCart()
        example_shc_void_last_item.add_item("ice cream", 5.00)
        example_shc_void_last_item.add_item("cereal", 10.00)
        example_shc_void_last_item.add_item("OJ", 4.00, 2)
        example_shc_void_last_item.void_last_item()
        self.assertEqual(len(example_shc_void_last_item.items), 3)
        self.assertEqual(example_shc_void_last_item.total, 19.0)
        while example_shc_void_last_item.items:
            example_shc_void_last_item.void_last_item()
        self.assertEqual(example_shc_void_last_item.void_last_item(), "There are no items in your cart!")
