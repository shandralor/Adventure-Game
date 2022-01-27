from ast import While
from msilib.schema import Error
from xmlrpc.client import boolean


class Inventory:
    def __init__(self, contents):
        self.contents = []

#Function for getting items from your inventory and thus removing them from the list            
    def get_item_from_inventory(self):
        item_needed = input("What item do you want to retrieve from your inventory? ").capitalize().strip()
        if item_needed not in self.contents:
            print(f"You don't have a {item_needed} in your inventory.")
        else:
            self.contents.remove(item_needed)
            print(f"The {item_needed} was taken out of your inventory and can now be used.")

       

#Function for showing inventory contents
    def show_inventory_contents(self):
        print(f"{' ':<20}{'--------Inventory--------':<40}")
        print(f"{' ':<20}{'-------------------------':<40}")
        for x in range (len(self.contents)):
            print(f"{' ':<30}{self.contents[x]}{' ':<40}")
        print(f"{' ':<20}{'-------------------------':<40}\n")

#Function for putting items in your inventory and thus adding them to the list
    def put_item_in_inventory(self, item_name):

        item_name = item_name

        print(f"You found the following loot: {item_name}.\n")
        while True:
            respons = input("Please type Yes if you want to put the item in your inventory or No if you want to discard it.  ").lower().strip()
            if respons not in ('yes','no'):           
                print("\nYou did not type Yes or No.\n")    
            else:
                break    
                     
        if respons =="yes": 
            self.contents.append(item_name)
            print(f"\nThe {item_name} was added to your inventory.\n")
            
        if respons == "no":
            print(f"\nThe {item_name} you found was discarded.\n")
            
            
        
            
            
        
            
            


