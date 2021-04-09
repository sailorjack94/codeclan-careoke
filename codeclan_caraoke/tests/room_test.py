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
        self.guest3 = Guest("Bill Gates", 10000000000)
        self.guestlist = []
        self.playlist = [self.song1, self.song2]
        self.rockroom = Room("Rock Room", 6, 10, self.playlist, self.guestlist, 0)

    def test_room_has_roomname(self):
        self.assertEqual("Rock Room", self.rockroom.roomname)

    def test_room_has_capacity(self):
        self.assertEqual(6, self.rockroom.capacity)

    def test_room_has_entry_price(self):
        self.assertEqual(10, self.rockroom.costpp)


# Ask about this... Can check to see if type the same??
    def test_room_has_playlist(self):
        self.assertEqual(self.playlist, self.rockroom.playlist)

    def test_room_has_guestlist(self):
        self.assertEqual([], self.rockroom.guestlist)

    def test_add_guest_to_room(self):
        self.rockroom.add_guest_to_room(self.guest1)
        self.assertEqual([self.guest1], self.rockroom.guestlist)

    def test_room_takings_increase(self):
        self.rockroom.add_guest_to_room(self.guest1)
        self.assertEqual(10, self.rockroom.roomtakings)
    
    def test_guest_cash_decreases(self):
        self.rockroom.add_guest_to_room(self.guest2)
        self.assertEqual(15, self.guest2.cash)

    def test_room_at_capacity(self):
        self.rockroom.add_guest_to_room(self.guest3)
        self.rockroom.add_guest_to_room(self.guest3)
        self.rockroom.add_guest_to_room(self.guest3)
        self.rockroom.add_guest_to_room(self.guest3)
        self.rockroom.add_guest_to_room(self.guest3)
        self.rockroom.add_guest_to_room(self.guest3)
        self.assertEqual(6, len(self.rockroom.guestlist))