"""
This module is where I will pull functions from gamefunctions.py and create a mini-text game.

It imports utility functions from the gamefunctions module to provide
interactive gameplay for the player. They can input their name, view
a shop menu, make purchases, and may even get a visit from rng monsters.

Here is how my mini-game currently works:
First: User will be prompted for their name.
Second: Terminal will display a welcome message.
Third: Terminal will show available items in the shop.
Fourth: User will be prompted for their money amount as a float.
Fifth: Prompts the user to purchase item based on their available money.
Sixth: Generates and displays an rng monster with their description.
"""

#--------------------------------------------------------------------

#gamefunctions.py
#Ethan Elliott
#October 20th, 2024
#CSCI150 w/ Jeff
#The purpose of this module is defined in the docstring above.

#--------------------------------------------------------------------

from gamefunctions import print_welcome, print_shop_menu, purchase_item, new_random_monster

def main():
    name = input("Enter your name: ")
    print()
    print_welcome(name, 30)

    # This is a test call for the shop menu function.
    print()
    print("Here is our shop selection:\n")
    print_shop_menu("Sword", 15.00, "Shield", 10.00)

    # This is where I ask the user how much money they have.
    starting_money = float(input(f"How much money do you have, {name}? $"))
    print()
    
    # This is where i check to see if they have enough money.
    if starting_money < 10.00:
        print(f"Interesting... It looks like you only have ${starting_money}. \nYou might not have enough... But you can try.\n")

    # This is where i ask the user which item they prefer.
    item_choice = input("Would you like to buy a Sword or a Shield? ").strip().lower()
    
    if item_choice == "sword":
        item_price = 15.00
    elif item_choice == "shield":
        item_price = 10.00
    else:
        print("Invalid choice! You can only choose 'Sword' or 'Shield'. Come back later.")
        return

    quantity_to_purchase = int(input(f"How many {item_choice.capitalize()}(s) would you like to purchase? "))
    quantity_purchased, remaining_money = purchase_item(item_price, starting_money, quantity_to_purchase)

    print(f"You purchased {quantity_purchased} {item_choice.capitalize()}(s). Remaining money: ${remaining_money:.2f}")

    if quantity_purchased == 0:
        print("\nYou cannot afford to purchase this item! How are you going to defend yourself now?! GG I guess...\n")
    else:
        print("Thank goodness. Now you have something to defend yourself! You came prepared.\n")

    # this test generates and displays an rng monster
    monster = new_random_monster()
    print()
    print(f"Oh no! You've encountered a monster: {monster['name']} - {monster['description']}.\nGood luck surviving...\n")

if __name__ == "__main__":
    main()