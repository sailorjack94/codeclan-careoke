import unittest
from src.guest import *
from src.song import *
from src.food_drink import *

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.song = Song("A Boy Named Sue", "Johnny Cash")
        self.guest = Guest("Niall", 20, self.song)
        self.chips = FoodDrink("Chips", 2.50)

    def test_guest_has_name(self):
        self.assertEqual("Niall", self.guest.name)

    def test_guest_has_cash(self):
        self.assertEqual(20, self.guest.cash)

    def test_guest_has_fav_song(self):
        self.assertEqual(self.song, self.guest.fav_song)

    def test_buy_item(self):
        self.guest.buy_item(self.chips)
        self.guest.buy_item(self.chips)
        self.assertEqual(15, self.guest.cash)