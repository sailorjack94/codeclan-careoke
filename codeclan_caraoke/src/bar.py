from src.guest import *
from src.food_drink import *

class Bar:
    def __init__(self, till):
        self.name = "CodeClanCaraoke"
        self.till = till
        self.menu = {}

    def add_food_or_drink(self, food_drink):
        if food_drink in self.menu:
            self.menu[food_drink] += 1
        else:
            self.menu[food_drink] = 1

    def check_stock_level(self, food_drink):
        stock_level = 0
        if food_drink in self.menu:
            return self.menu[food_drink]
        else:
            return stock_level

    def sell_food_drink(self, food_drink, guest):
        if (self.check_stock_level(food_drink) > 0) and (guest.cash >= food_drink.price):
            self.till += food_drink.price
            guest.buy_item(food_drink)
            self.menu[food_drink] -= 1