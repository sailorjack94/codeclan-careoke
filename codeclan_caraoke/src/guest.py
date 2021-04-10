from src.food_drink import *

class Guest:

    def __init__(self, name, cash, fav_song):
        self.name = name
        self.cash = cash
        self.fav_song = fav_song

# This function always removes cash - so it must be checked that the customer can afford the product before calling it.
    def buy_item(self, food_drink):
            self.cash -= food_drink.price