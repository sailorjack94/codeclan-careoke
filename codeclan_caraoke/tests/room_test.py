import unittest 
from src.room import *
from src.song import *
from src.guest import *

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.song1 = Song("Ace of Spades", "Motorhead")
        self.song2 = Song("Number of the Beast", "Iron Maiden")
        self.guest1 = Guest("Dave", 20)
        self.guest2 = Guest("Catherine", 25)
        self.guestlist = [self.guest1, self.guest2]
        self.playlist = [self.song1, self.song2]
        self.rockroom = Room("Rock Room", 6, 10, self.playlist, self.guestlist)

    def test_room_has_roomname(self):
        self.assertEqual("Rock Room", self.rockroom.roomname)

    def test_room_has_capacity(self):
        self.assertEqual(6, self.rockroom.capacity)

    def test_room_has_entry_price(self):
        self.assertEqual(10, self.rockroom.costpp)


# Ask about this... Can check to see if type the same??
    def test_room_has_playlist(self):
        self.assertEqual(self.playlist, self.rockroom.playlist)

    def test_room_has_guests_in(self):
        self.assertEqual([self.guest1, self.guest2], self.rockroom.guestlist)