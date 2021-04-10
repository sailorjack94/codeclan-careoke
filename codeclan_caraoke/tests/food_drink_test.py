import unittest 
from src.food_drink import *

class TestFoodDrink(unittest.TestCase):
    def setUp(self):
        self.food = FoodDrink(self, "Chips", 2.50)
        self.drink = FoodDrink(self, "Beer", 3.50)

    def test_has_name(self):
        self.assertEqual("Chips", self.food.name)