import unittest 
from src.song import *

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Ace of Spades", "Motorhead")

    def test_song_has_title(self):
        self.assertEqual("Ace of Spades", self.song.title)

    def test_song_has_artist(self):
        self.assertEqual("Motorhead", self.song.artist)