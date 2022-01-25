import random
from Inventory import Inventory



#THIS CLASS WILL BE THE ABSTRACT SUPERCLASS FOR THE ACTUAL PLAYER CLASSES(RANGER, WARRIOR, WITCH, BARD)

#Constructor class for Adventurer
class Adventurer:
    def __init__(self, name, sex, age, contents,str=None, dex=None, int =None, cha=None, health = None, mana = None, ):
        self.name = name
        self.sex = sex
        self.age = age

#Generating the random stats for the characters

        if str is None: 
            str = random.randint(8, 16)
            self.str = str
        if dex is None:
            dex = random.randint(8, 16)
            self.dex = dex
        if int is  None:
            int  = random.randint(8, 16)
            self.int = int
        if cha is None:
            cha = random.randint(8, 16)
            self.cha = cha

#Calculating HP and rounding it off to an int

        if health is None:
            health = (str + dex)/2
            self.health = round(health)

#Calculating MP and rounding it off to an int

        if mana is None:
            mana = int * 3
            self.mana = round(mana)


        self.contents = contents



#List slicing can be used to restrict inventory size to a certain amount
# using list slicing
# to truncate list 
#res = test_list[0 : 5]




       
#Outputting everything to the console to see if it works

    def show_stats(self):
        print(f"The stats of {self.name} are the following:\n-Dexterity = {self.dex} \n-Strength = {self.str} \n-Intelligence = {self.int} \n-Charisma = {self.cha}") 
        if self.sex =="Male":
            print(f"He has {self.health} HP and {self.mana} MP.") 
        else:
            print(f"She has {self.health} HP en {self.mana} MP.")
        Inventory.show_inventory_contents(self)
       
#INVENTORY COMMANDS
    def get_item(self):
        Inventory.get_item_from_inventory(self)

    def set_item(self, Item):
        Inventory.put_item_in_inventory(self, Item)

    def show_inventory(self):
        Inventory.show_inventory_contents(self)

#TESTING PART        

a1 = Adventurer("Tom", "Female", 32, ["Rope", "Torch"])

a1.show_stats()
a1.get_item()
a1.show_inventory()
a1.set_item("Blade")
a1.show_inventory()
