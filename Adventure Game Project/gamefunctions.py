#gamefunctions.py
#Ethan Elliott
#October 6th, 2024
#CSCI150 w/ Jeff
#This is my upload for project Documentation and Strings
#The purpose of this assignment is to learn about functions and how to use them.

#Here, I am importing random so I can use the random() commands.
import random

#Creating line separation print for formatting purposes
line_separation = ("*" * 75)

print("Welcome to my program for creating and testing function calls.\n")
print()
print(line_separation)

def print_welcome(name: str, width: int):
    """
    This function prints a welcome message for the supplied 'name' parameter. The output is centered on within a 20-character field.
    """
    formatted_name = f"| {'Hello, ' + name + '!':^{width}} |"
    print(f"{formatted_name}")

print(f'\nDocumentation and Strings: Part #1:')

#3 calls to the print_welcome function to test functionality. i used the "|" symbol to show where it starts and ends. 
print()
print(f'\nGreeting Call #1:')
print_welcome(name = "Ethan", width = 30)
print(f'\nGreeting Call #2:')
print_welcome(name = "Jeff", width = 40)
print(f'\nGreeting Call #3:')
print_welcome(name = "Lilith", width = 50)
print()

print(line_separation)
print()

print(f'\nDocumentation and Strings: Part #2:')

#defining the shop menu for the user. 
def print_shop_menu(item1Name: str, item1Price: float, item2Name: str, item2Price: float):
    """
    This function prints a sign that contains a list of two items and their corresponding prices. Items are left-aligned in the menu, while the prices are right-aligned (with decimal points lining up).
    Prices are formatted to show 2 decimal places, and preceded with a dollar sign (with no space between the dollar sign and the price).
    The item name field has 12 characters, and the item price field has 8 characters. The sign is surrounded with a nice border to differentiate it from other text.
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

#calling print_shop_menu 3 times for assignment req.
print(f'\nShop Menu Call #1:')
print_shop_menu("Apple", 15, "Pear", 2.521)
print(f'\nShop Menu Call #2:')
print_shop_menu("Egg", .78, "Pineapple", 4.24)
print(f'\nShop Menu Call #3:')
print_shop_menu("Bread", .21, "Watermelon", 8.29)


#Pre-October assignments below (unmodified): Defining the function purchase_item, below, with 3 parameters, and declaring their type in the process.
#Also making quantityToPurchase default to 1 if no proper value is passed through the parameter, which shouldn't ever happen imo.
#I had to google how to do this. I didn't know it was possible to assign value to the type within the parameters at first.
#I initially tried defining to 1 outside of the function but it kept outputting 1 (obviously), so this had to be done.

def purchase_item(itemPrice: float, startingMoney: float, quantityToPurchase: int = 1):
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

print(line_separation)

#Labelling assignments numerically
print(f'\nAdventure Functions: Part #1:')


#Making a loop that executes 3 times for 3 unique calls. I chose random ranges for the variable values instead of input().
for counter in range(4):
    itemPrice = random.random() * 10.0
    startingMoney = random.random() * 50.0
    quantityToPurchase = random.randint(1,5)
    quantityPurchased, leftover_money = purchase_item(itemPrice, startingMoney, quantityToPurchase)

    if (counter == 3):
        quantityToPurchase = 1
        quantityPurchased, leftover_money = purchase_item(itemPrice, startingMoney)
        print(f'{line_separation}')
        print("\nBelow, you will find a test case for default value of 1.\nPrinting quantity to purchase as 1, but quantity purchased is not a passed value in the parameter of the function")

#Spent some time on the formatting to make this look good, like Jeff showed in class involving the usage of whitespace.
    print(f"""
\n{line_separation}
Money Call #{counter + 1}:
Initial Quantity Desired:   x{quantityToPurchase}
Amount Purchased:           x{quantityPurchased}
Item Price:                ${itemPrice:,.2f}
Starting Money:            ${startingMoney:,.2f}
Remaining Money:           ${leftover_money:,.2f}
""")



#----------------------------------------------



#Defining a function for the monsters portion of the assignment, with some funny descriptions sprinkled in there.
def new_random_monster():
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

#Once again, I spent some time on the formatting to make this look good, like Jeff showed in class involving the usage of whitespace.
print(f'\n{line_separation}\nAdventure Functions: Part #2:\n')

for i in range(3):
    monster = new_random_monster()
    print(f"Monster Call #{i + 1}:")
    print(f"Name:         {monster['name']}")
    print(f"Description:  {monster['description']}")
    print(f"Health:       {monster['health']}")
    print(f"Power:        {monster['power']}")
    print(f"Money:        ${monster['money']:.2f}\n")
    print(line_separation)
