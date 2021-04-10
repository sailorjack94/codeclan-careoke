import unittest
from src.guest import * 
from src.bar import *
from src.food_drink import *

class TestBar(unittest.TestCase):
    def setUp(self):
        self.bar = Bar(1000)
        self.chips = FoodDrink("Chips", 2.50)
        self.beer = FoodDrink("Beer", 3.50)
        self.wine = FoodDrink("Wine", 4.50)
        self.guest = Guest("Niall", 20, "Aces High")

    def test_bar_has_name(self):
        self.assertEqual("CodeClanCaraoke", self.bar.name)

    def test_bar_has_till(self):
        self.assertEqual(1000, self.bar.till)

    def test_add_food_or_drink(self):
        self.bar.add_food_or_drink(self.chips)
        self.assertEqual({self.chips : 1}, self.bar.menu)
        
    def test_can_increase_stock_level(self):
        self.bar.add_food_or_drink(self.chips)
        self.bar.add_food_or_drink(self.chips)
        self.assertEqual({self.chips : 2}, self.bar.menu)

    def test_check_stock_level(self):
        self.bar.add_food_or_drink(self.chips)
        self.bar.add_food_or_drink(self.chips)
        self.assertEqual(2, self.bar.check_stock_level(self.chips))

    def test_sell_food_drink(self):
        self.bar.add_food_or_drink(self.chips)
        self.bar.add_food_or_drink(self.chips)
        self.bar.sell_food_drink(self.chips, self.guest)
        self.assertEqual(17.50, self.guest.cash)
        self.assertEqual(1002.50, self.bar.till)
