"""This module has a purpose of defining various functions for game.py

There are 5 working functions within this module, 
which are defined below and also contain their own docstrings.
These functions allow for (1): welcome message, (2): shop menu, 
(3): purchasing items, (4): creating rng monsters, (5): Testing.

One example of how to use this modules:

'from gamefunctions import print_welcome'
Then view function docstring for instructions.
One example: 'print_welcome("Name", 30)'
"""

#--------------------------------------------------------------------

#gamefunctions.py
#Ethan Elliott
#October 20th, 2024
#CSCI150 w/ Jeff
#The purpose of this module is defined in the docstring above.

#--------------------------------------------------------------------



#Here, I am importing random so I can use the random() commands.
import random

#Creating line separation print for formatting purposes
line_separation = ("*" * 75)




def print_welcome(name: str, width: int):
    """
    This function prints a welcome message for the supplied 'name' parameter. The output is centered within a 20-character field.
    
    Parameters:
        name (str): The name of who will be welcomed.
        width (int): Width amount for centering purposes.

    Returns:
        None

    Example:
        >>> print_welcome("Ethan", 30)
    """
    formatted_name = f"| {'Hello, ' + name + '!':^{width}} |"
    print(f"{formatted_name}")


def print_shop_menu(item1Name: str, item1Price: float, item2Name: str, item2Price: float):
    """
    This function prints a sign that contains a list of two items and their corresponding prices. 

    Parameters:
        item1Name (str): name of the 1st item.
        item1Price (float): price of the 1st item.
        item2Name (str): name of the 2nd item.
        item2Price (float): price of the 2nd item.

    Returns:
        None

    Example:
        >>> print_shop_menu("Orange", 1.20, "Pomegranate", 0.70)
    """
    #this part is for basic formatting required to get the int as a float with decimals to 2 points prior to altering whitespace.
    item1Priced = f"${item1Price:.2f}"
    item2Priced = f"${item2Price:.2f}"
    #here, i used the values of 12 and 8 to define how much space each variable receives prior to printing
    p1 = f"| {item1Name:<12}{item1Priced:>8} |"
    p2 = f"| {item2Name:<12}{item2Priced:>8} |"
    #manually printing the borders proved simple enough to implement.
    border = "/----------------------\\"
    print(border)
    print(p1)
    print(p2)
    print("\\----------------------/")


def purchase_item(itemPrice: float, startingMoney: float, quantityToPurchase: int = 1):
    """
    This function will return the number of items purchased and the quantity of money that is remaining. 
    If unable to afford all the items, it will only buy as many as can be afforded. Nothing is printed by the function call.

    Parameters:
        itemPrice (float): cost of one item.
        startingMoney (float): amt of money to spend.
        quantityToPurchase (int): num of items desired (default is 1).

    Returns:
        tuple: A tuple containing the num of items purchased and the remaining money.

    Example:
        >>> purchase_item(2.50, 10.00, 3)
        (3, 2.50)
    """
    totalPrice = (quantityToPurchase * itemPrice)

    if totalPrice > startingMoney:
        if itemPrice > 0:
            quantityPurchased = int(startingMoney // itemPrice)
        else:
            quantityPurchased = 0
    else:
        quantityPurchased = quantityToPurchase

    leftover_money = startingMoney - quantityPurchased * itemPrice
    return quantityPurchased, leftover_money


def new_random_monster():
    """
    This function generates a new monster when called. 
    There are 3 available monster types with rng unique traits.

    Parameters:
        None

    Returns:
        dict: A dict w/ the monster's name, description, health, power, and money.

    Example:
        >>> new_random_monster()
    """
    monsters = [
        {
            "name": "Ghost",
            "description": "This spooky Ghost will haunt you when the sunlight disappears. That is, if he isn't running errands.",
            "health": random.randint(1, 85),
            "power": random.randint(1, 80),
            "money": round(random.random() * 99, 2)
        },
        {
            "name": "Demon",
            "description": "This terrifying demonic presence will invoke terror in the eyes of all who dare come near. Or maybe he's just shy?",
            "health": random.randint(1, 100),
            "power": random.randint(1, 70),
            "money": round(random.random() * 98, 2)
        },
        {
            "name": "Mysterious Black Cat",
            "description": "This evil cat may seem cute on the surface, yet beware, as one meow can determine your fate. You don't want to see what a purr does...",
            "health": random.randint(1, 60),
            "power": random.randint(1, 75),
            "money": round(random.random() * 100, 2)
        }
    ]
    return random.choice(monsters)

def test_functions() -> None:
    """
    The purpose of this function is to run tests 
    for all other functions within this module.
    Each one of the functions is called 3x times.
    """
    print(line_separation)
    print(f'\nBelow, there are 3x function call tests printed for each function within this module:\n')
    print(line_separation)

    print(f'\nTesting the print_welcome function:\n')
    print(f'\nGreeting Call #1:')
    print_welcome(name="Ethan", width=30)
    print(f'\nGreeting Call #2:')
    print_welcome(name="Jeff", width=40)
    print(f'\nGreeting Call #3:')
    print_welcome(name="Lilith", width=50)
    print()
    print(line_separation)

    print(f'\nTesting the print_shop_menu function:\n')
    print(f'\nShop Menu Call #1:')
    print_shop_menu("Apple", 15, "Pear", 2.521)
    print(f'\nShop Menu Call #2:')
    print_shop_menu("Egg", 0.78, "Pineapple", 4.24)
    print(f'\nShop Menu Call #3:')
    print_shop_menu("Bread", 0.21, "Watermelon", 8.29)
    print()
    print(line_separation)

    print(f'\nTesting the purchase_item function:\n')
    for counter in range(4):
        itemPrice = random.random() * 10.0
        startingMoney = random.random() * 50.0
        quantityToPurchase = random.randint(1, 5)
        quantityPurchased, leftover_money = purchase_item(itemPrice, startingMoney, quantityToPurchase)

        if counter == 3:
            quantityToPurchase = 1
            quantityPurchased, leftover_money = purchase_item(itemPrice, startingMoney)
            print(f'{line_separation}')
            print("\nBelow, you will find a test case for default value of 1.")

        print(f"""
        Money Call #{counter + 1}:
        Initial Quantity Desired:   x{quantityToPurchase}
        Amount Purchased:           x{quantityPurchased}
        Item Price:                ${itemPrice:,.2f}
        Starting Money:            ${startingMoney:,.2f}
        Remaining Money:           ${leftover_money:,.2f}
        """)
    print()
    print(line_separation)

    print(f'\nTesting the new_random_monster function:\n')
    for i in range(3):
        monster = new_random_monster()
        print(f"Monster Call #{i + 1}:")
        print(f"Name:         {monster['name']}")
        print(f"Description:  {monster['description']}")
        print(f"Health:       {monster['health']}")
        print(f"Power:        {monster['power']}")
        print(f"Money:        ${monster['money']:.2f}\n")
        print()
        print(line_separation)

if __name__ == "__main__":
    test_functions()