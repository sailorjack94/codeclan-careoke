import unittest 
from src.room import *
from src.song import *

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.song1 = Song("Ace of Spades", "Motorhead")
        self.song2 = Song("Number of the Beast", "Iron Maiden")
        self.playlist = [self.song1, self.song2]
        self.roomrock = Room("Rock Room", 6, 10, self.playlist)

    def test_room_has_roomname(self):
        self.assertEqual("Rock Room", self.roomrock.roomname)