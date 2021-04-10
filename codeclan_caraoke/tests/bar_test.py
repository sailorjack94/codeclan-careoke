import unittest
from src.guest import * 
from src.bar import *

class TestBar(unittest.TestCase):
    def setUp(self):
        self.bar = Bar(1000)

    def test_bar_has_name(self):
        self.assertEqual("CodeClanCaraoke", self.bar.name)