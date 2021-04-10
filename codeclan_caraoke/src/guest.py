from src.food_drink import *

class Guest:

    def __init__(self, name, cash, fav_song):
        self.name = name
        self.cash = cash
        self.fav_song = fav_song

    def buy_item(self, food_drink):
            self.cash -= food_drink.price