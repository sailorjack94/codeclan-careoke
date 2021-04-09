import unittest 
from src.room import *
from src.song import *

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.song1 = Song(self)
        self.song2 = Song(self)
        self.playlist = [self.song1, self.song2]
        self.roomrock = Room(self, "Rock Room", 6, 10, self.playlist)

