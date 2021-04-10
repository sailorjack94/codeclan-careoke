import unittest
from src.guest import *
from src.song import *

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.song = Song("A Boy Named Sue", "Johnny Cash")
        self.guest = Guest("Niall", 20, self.song)

    def test_guest_has_name(self):
        self.assertEqual("Niall", self.guest.name)

    def test_guest_has_cash(self):
        self.assertEqual(20, self.guest.cash)

    def test_guest_has_fav_song(self):
        self.assertEqual(self.song, self.guest.fav_song)