from computer import *
class ResaleShop:

    # Attributes:
   inventory: list

   # Set up constructor
   def __init__(self, start_inventory: list = []):
        self.inventory = start_inventory
   
   # --------- Methods ---------
   """ Takes in an object of the Computer class and adds 
         it to the shops inventory. If the same object is 
         already in the inventory, prints an error message"""
   def buy(self, item: Computer):
      if item in self.inventory:
         print("Buying Error: This computer is already in the inventory. Please try again.")
      else:
         self.inventory.append(item)
         print("New computer added to system: " + item.description)
   
   """ Takes in an object of the Computer class. If it is already 
         in the shope inventory it removes the object from the inventory, 
         if it is not in the inventory it prints an error message"""
   def sell(self, item: Computer):
      if item in self.inventory:
         id = self.inventory.index(item)
         print("Computer sold: " + self.inventory[id].description)
         self.inventory.pop(id)
      else:
         print("Selling Error: Computer not found. Please try again.")
      
   """ Prints the shops inventory, and a welcome message. """
   def print_inventory(self):
      print("\n" + "-"*20 +"Welcome to the Computer Store" + "-"*20+ "\nWe have the following computers in stock:", end = "\n\n")
      for item in self.inventory:
         print(item, end = "\n\n")
         
   """ Takes in an object of the Computer class and an optional string
       representing the operating system to update to. Updates the 
       computer price based on the age attribute. Updates the operating 
       system if new_os is given, otherwise leaves it as is. Prints error
         message if computer is not found in inventory"""
   def refurbish(self, item: Computer, new_os: str = None):
      if item in self.inventory:
            print("Refurbishing comupter: " + str(item.description) + "\n Please wait...")
            if new_os is not None:
               item.update_OS(new_os) # update details after installing new OS
            if int(item.year_made) < 2000:
               new_price = 0 # too old to sell, donation only
            elif int(item.year_made) < 2012:
               new_price = 250 # heavily-discounted price on machines 10+ years old
            elif int(item.year_made) < 2018:
               new_price = 550 # discounted price on machines 4-to-10 year old machines
            else:
               new_price = 1000 # recent stuff
            item.update_price(new_price)
            print("Computer Refurbished.")
      else:
         print("Refurbishing Error: Computer not found. Please try again.")
      