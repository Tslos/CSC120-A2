from computer import *
from oo_resale_shop import *

def main():
    # Create my shop (no inventory yet! We have just opened)
    myshop = ResaleShop()
    # Make two computers
    computer1 = Computer(
        "2020 HP HD",
        "Intel N4000 Series",
        64, 16,
        "Windows 10", 2020, 500
    )
    computer2 = Computer(
        "Mac Air 2018",
        "2.6 GHz 6-Core Intel Core i7",
        1024, 64,
        "macOS Sonoma", 2018, 1200
    )

    # Buy the two computers
    myshop.buy(computer1)
    myshop.buy(computer2)

    # Make sure it worked by checking inventory
    myshop.print_inventory()

    # Refurbish the first computer
    myshop.refurbish(computer1, "Windows 11")

    # Make sure it worked by checking inventory
    myshop.print_inventory()
    
    # Now, let's sell it!
    myshop.sell(computer1)

    # Make sure it worked by checking inventory
    myshop.print_inventory()

    # Trigger some errors to see the response:
    
    # Try to buy the same computer twice:
    myshop.buy(computer2)

    # Try to sell a computer not in the inventory
    myshop.sell(computer1)

    # Try to refurbish a computer not in the inventory
    myshop.refurbish(computer1)


# Calls the main() function when this file is run
if __name__ == "__main__": main()

