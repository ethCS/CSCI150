"""
This module is where I will pull functions from gamefunctions.py and create a text game.
My game.py currently guides the player through a series of questions and string-based prompts.

My game allows for the player to:
* Enter their name
* Choose options
* Encounter randomly generated monsters
* Decide their fate
"""
from gamefunctions import (print_welcome, print_shop_menu, purchase_item, new_random_monster, fight_monster, sleep, shop, print_inventory, equip_item, json_save_game, json_load_game)

#Starting stats
health = 50
gold = 10
inventory = {}

# Let player choose to load a saved game or start new
player_choice = input("Choose: (n)ew game | (l)oad game? ").strip().lower()
if player_choice == 'l':
    saved_game = json_load_game()
    if saved_game:
        player_name, health, gold, inventory = saved_game
        print(f"Health: {health}, Gold: {gold}\n")
        updated_gold = shop(player_name, gold, True, inventory)
        gold = updated_gold
    else:
        print("No load detected... Creating new game.\n(New Game)")
        player_name = input("Enter new name:\n")
        print_welcome(player_name, 30)
        print(f"Health: {health}, Gold: {gold}\n")
        updated_gold = shop(player_name, gold, True, inventory)
        gold = updated_gold
else:
    player_name = input("Enter your name: ")
    print_welcome(player_name, 30)
    print(f"Health: {health}, Gold: {gold}\n")
    updated_gold = shop(player_name, gold, True, inventory)
    gold = updated_gold

# Define main game loop function
def main(player_name: str, health: int, gold: float, inventory: dict) -> tuple:
    """
    This function will serve as a very basic game that allows the player
    to interact with a menu and choose options to fight, sleep, or quit.

    Parameters:
        player_name (str): Name of the player
        health (int): Current health points
        gold (float): Current gold amount
        inventory (dict): Player's inventory

    Returns:
        tuple: Updated (health, gold, inventory)
    """
    playing = True
    while playing:
        print(f"Health: {health}, Gold: {gold}\n")

        print("""What would you like to do?\n
            1) Fight Monster\n
            2) Sleep (Gain 10 health in exchange for 5 Gold)\n
            3) Enter Shop\n
            4) View Inventory\n
            5) Equip Item\n
            6) Save and Quit\n
            7) Quit Without Saving\n""")

        choice = input("Choose from options 1-7: ").strip()
        if choice == '1':
            monster = new_random_monster()
            health, gold = fight_monster(monster, health, gold, inventory)
        elif choice == '2':
            health, gold = sleep(health, gold)
        elif choice == '3':
            updated_gold = shop(player_name, gold, False, inventory)
            gold = updated_gold
        elif choice == '4':
            print_inventory(inventory)
        elif choice == '5':
            equip_item(inventory)
        elif choice == '6':
            json_save_game(player_name, health, gold, inventory)
            print("Thanks for playing.\n")
            playing = False
        elif choice == '7':
            print("Thanks for playing.\n")
            playing = False
        else:
            print("That won't work. Try again with an option from 1-7.\n")

    return health, gold, inventory

# Start the game
if __name__ == "__main__":
    health, gold, inventory = main(player_name, health, gold, inventory)