import unittest
from src.guest import *

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Niall")

    def test_guest_has_name(self):
        self.assertEqual("Niall", self.guest.name)