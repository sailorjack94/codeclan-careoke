import unittest 
from src.food_drink import *

class TestFoodDrink(unittest.TestCase):
    def setUp(self):
        self.food = FoodDrink("Chips", 2.50)
        self.drink = FoodDrink("Beer", 3.50)

    def test_has_name(self):
        self.assertEqual("Chips", self.food.name)

    def test_has_price(self):
        self.assertEqual(3.50, self.drink.price)