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