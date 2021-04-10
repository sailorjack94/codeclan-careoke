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