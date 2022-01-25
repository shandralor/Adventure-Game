import random


class Ability:
    def __init__(self, name, cost, cooldown, damage):
        self.name = name
        self.cost = cost
        self.cooldown = cooldown
        self.damage = damage

#output to screen method to show ability statistics
    def description(self):
        print(f"This is the {self.name} ability with a MP cost of {self.cost} and a cooldown of {self.cooldown}.")
        print(f"It does {self.damage} points of damage.")

#test to see if it works  
ab1 = Ability("Windwall", 3, 2, 6)

ab1.description()
