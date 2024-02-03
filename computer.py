class Computer:

    # Attributes
    description: str
    processor_type: str
    hard_drive_capacity: int 
    memory: int
    operating_system: str
    year_made: int
    price: int

   # Set up constructor
    def __init__(self, description, processor_type, hard_drive_capacity, memory, start_os, year_made, start_price):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = start_os
        self.year_made = year_made
        self.price = start_price
    
    # Set up description of class
    def __str__(self):
        return "This is a " + self.description + " with a " + self.processor_type +" processor, " + str(self.hard_drive_capacity) + " GB of hard drive, " + str(self.memory) + " GB of memory, and runs the operating system " + self.operating_system + ". It was made in " + str(self.year_made)  + " and costs " + str(self.price) + " dollars."
    
   # --------- Methods ---------
    """ Takes an integer and assigns it to be the price attribute"""
    def update_price(self, new_price:int):
        self.price = new_price

    """Takes a string and assigns it to be the operating_system attribute"""
    def update_OS(self, new_os:str):
        self.operating_system = new_os
