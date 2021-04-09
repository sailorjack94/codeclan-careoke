import unittest
from src.guest import *

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Niall", 20)

    def test_guest_has_name(self):
        self.assertEqual("Niall", self.guest.name)

    def test_guest_has_cash(self):
        self.assertEqual(20, self.guest.cash)