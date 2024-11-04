"""
This module is where I will pull functions from gamefunctions.py and create a text game.
My game.py currently guides the player through a series of questions and string-based prompts.

My game allows for the player to:
* Enter their name
* Choose options
* Encounter randomly generated monsters
* Decide their fate
"""
from gamefunctions import print_welcome, print_shop_menu, purchase_item, new_random_monster, fight_monster, sleep, shop, print_inventory, equip_item

#Here are the global variables that define the initial health and currency.
user_hp = 50
user_gold = 10
inventory = {}

#Getting user name
name = input("Enter your name: ")
print_welcome(name, 30)
print(f"Health: {user_hp}, Gold: {user_gold}\n")

#This is the shop functionality
money = shop(name, user_gold, True, inventory)
user_gold = money

def main() -> None:
    """
    This function will serve as a very basic game that allows the player
    to interact with a menu and choose options to fight, sleep, or quit.
    """

    global name, user_hp, user_gold

    while True:
        print(f"Health: {user_hp}, Gold: {user_gold}\n")

        print("""What would you like to do?\n
            1) Fight Monster\n
            2) Sleep (Gain 10 health in exchange for 5 Gold)\n
            3) Enter Shop\n
            4) View Inventory\n
            5) Equip Item\n
            6) Quit Game\n""")

        choice = input("Choose from options 1-6: ").strip()
        if choice == '1':
            monster = new_random_monster()
            user_hp, user_gold = fight_monster(monster, user_hp, user_gold, inventory)
        elif choice == '2':
            user_hp, user_gold = sleep(user_hp, user_gold)
        elif choice == '3':
            money = shop(name, user_gold, False, inventory)
            user_gold = money
        elif choice == '4':
            print_inventory(inventory)
        elif choice == '5':
            equip_item(inventory)
        elif choice == '6':
            print("Thanks for playing.\n")
            break
        else:
            print("That won't work. Try again with an option from 1-6.\n")

if __name__ == "__main__":
    main()