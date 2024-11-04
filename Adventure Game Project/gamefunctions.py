"""This module has a purpose of defining various functions for game.py

There are various functions within this module,
which are defined below and also contain their own docstrings.
These functions allow for (1): welcome message, (2): shop menu,
(3): purchasing items, (4): creating rng monsters, (5): fighting said monsters,
(6): sleeping to gain health, and (7): Testing.

One example of how to use this modules:

'from gamefunctions import print_welcome'
Then view function docstring for instructions.
One example: 'print_welcome("Name", 30)'
"""

#--------------------------------------------------------------------

#gamefunctions.py
#Ethan Elliott
#October 27th, 2024
#CSCI150 w/ Jeff
#The purpose of this module is defined in the docstring above.

#--------------------------------------------------------------------

#Here, I am importing random so I can use the random() commands.
import random

#Creating line separation print for formatting purposes
line_separation = print("*" * 75)

def print_welcome(name: str, width: int) -> None:
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

def print_shop_menu(item1Name: str, item1Price: float, item2Name: str, item2Price: float, item3Name: str, item3Price: float) -> None:
    """
    This function prints a sign that contains a list of two items and their corresponding prices.

    Parameters:
        item1Name (str): name of the 1st item.
        item1Price (float): price of the 1st item.
        item2Name (str): name of the 2nd item.
        item2Price (float): price of the 2nd item.
        item3Name (str): name of the 3rd item.
        item3Price (float): price of the 3rd item.

    Returns:
        None

    Example:
        >>> print_shop_menu("Orange", 1.20, "Pomegranate", 0.70, "Apple", 2.10, "Carrot", 1.41)
    """
    #this part is for basic formatting required to get the int as a float with decimals to 2 points prior to altering whitespace.
    item1Priced = f"${item1Price:.2f}"
    item2Priced = f"${item2Price:.2f}"
    item3Priced = f"${item3Price:.2f}"
    #here, i used the values of 12 and 8 to define how much space each variable receives prior to printing
    p1 = f"| {item1Name:<12}{item1Priced:>19} |"
    p2 = f"| {item2Name:<12}{item2Priced:>8} |"
    p3 = f"| {item3Name:<12}{item3Priced:>14} |"
    #manually printing the borders proved simple enough to implement.
    border = "/------------------------------------------\\"
    print(border)
    print(p1)
    print(p2)
    print(p3)
    print("\\------------------------------------------/")

def purchase_item(itemPrice: float, startingMoney: float, quantityToPurchase: int = 1) -> tuple:
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

    leftover_money = startingMoney - totalPrice
    return quantityPurchased, leftover_money

def shop(name: str, user_gold: float, if_show_view_shop_prompt, inventory) -> float:
    """
    This function handles the entire shop menu functionality for game.py.
    Features include the ability to Purchase item(s), and the amount of item(s).

        Parameters:
        name (str): name of the player.
        user_gold (float): starting currency.
        if_show_view_shop_prompt (any): if the shop prompt should be shown.
        inventory (dict): stores items in user dictionary.

    Returns:
        float: user_gold after transactions.

    Example:
        >>> def shop(name: str, user_gold: float, if_show_view_shop_prompt, inventory):
        {user_gold}'s value
    """
    while True:
        if if_show_view_shop_prompt:
            prompt_to_buy = input(str(f"Would you like to view the shop, {name}?\n(Y)es or (N)o:\n")).strip().lower()
            if prompt_to_buy == 'y' or prompt_to_buy == 'yes':
                print_shop_menu('Sword: (Damage Boost)', 5, 'Shield: (Protection from danger)', 3, 'Special: (Ghost Destroyer)', 20)
            elif prompt_to_buy == 'n' or prompt_to_buy == 'no':
                return user_gold
            else:
                print("That is an invalid input. Try again.\n")
            purchase_choice = input("Which item would you like to purchase?\nYou can leave by entering 'exit'.\n").strip().lower()
        else:
            print_shop_menu('Sword: (Damage Boost)', 5, 'Shield: (Protection from danger)', 3, 'Special: (Ghost Destroyer)', 20)
            purchase_choice = input("Which item would you like to purchase?\nYou can leave by entering 'exit'.\n").strip().lower()

        if purchase_choice == 'exit':
            return user_gold

        elif purchase_choice == 'sword':
            amount_choice = input("How much of this item would you like to purchase?\n").strip()

            if not amount_choice.isnumeric():
                print("Please enter a valid number.\n")
                continue

            amount_choice = int(amount_choice)
            if user_gold >= 5 * amount_choice:
                quantityPurchased, leftover_money = purchase_item(5, user_gold, amount_choice)
                add_item_to_inventory('sword', 'weapon', amount_choice, inventory)
                print(f"You have purchased {amount_choice} sword(s).\nYour inventory has been updated.\n")
                return leftover_money
            else:
                print("You cannot afford to purchase a sword.\n")
                continue

        elif purchase_choice == 'special':
            amount_choice = input("How much of this item would you like to purchase?\n").strip()

            if not amount_choice.isnumeric():
                print("Please enter a valid number.\n")
                continue

            amount_choice = int(amount_choice)
            if user_gold >= 20 * amount_choice:
                quantityPurchased, leftover_money = purchase_item(20, user_gold, amount_choice)
                add_item_to_inventory('special', 'weapon', amount_choice, inventory)
                print(f"You have purchased {amount_choice} Special Item: Ghost Destroyers.\nYour inventory has been updated.\n")
                return leftover_money
            else:
                print("You cannot afford to purchase this special item.\n")
                continue

        elif purchase_choice == 'shield':
            amount_choice = input("How much of this item would you like to purchase?\n").strip()

            if not amount_choice.isnumeric():
                print("Please enter a valid number.\n")
                continue

            amount_choice = int(amount_choice)
            if user_gold >= 3 * amount_choice:
                quantityPurchased, leftover_money = purchase_item(3, user_gold, amount_choice)
                add_item_to_inventory('shield', 'defense', amount_choice, inventory)
                print(f"You have purchased {amount_choice} shield(s).\nYour inventory has been updated.\n")
                return leftover_money
            else:
                print("You cannot afford to purchase a shield.\n")
                continue

        else:
            print("That is not a valid option. Try again.\n")
            continue

    return user_gold

def new_random_monster() -> dict:
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
            "description": "This spooky Ghost will haunt you when the sunlight disappears.",
            "health": random.randint(20, 40),
            "power": random.randint(5, 10),
            "money": round(random.random() * 20, 2)
        },
        {
            "name": "Demon",
            "description": "This terrifying demonic presence will invoke terror.",
            "health": random.randint(25, 50),
            "power": random.randint(7, 12),
            "money": round(random.random() * 30, 2)
        },
        {
            "name": "Mysterious Black Cat",
            "description": "This evil cat may seem cute, yet beware.",
            "health": random.randint(15, 35),
            "power": random.randint(4, 8),
            "money": round(random.random() * 15, 2)
        }
    ]
    return random.choice(monsters)

def durability_modifier(which_item, inventory, dullness, damage_modifier) -> tuple:
    """
    This function is the handler for the item durability.
    The purpose is to calculate the dullness and apply wear to items.
    This function also handles item breaking or deletion and dmg modifiers based
    on the item state itself, if applicable.

    Parameters:
        which_item (str): The name of the item to modify durability for.
        inventory (dict): The player's inventory containing items and their properties.
        dullness (int): Amount of durability to reduce from the item.
        damage_modifier (int): Current damage bonus provided by the item.

    Returns:
        tuple: A tuple containing:
            - int: Updated damage modifier (0 if item breaks)
            - str: Status message about item durability and state

    Example:
        >>> print(message)
        'Your item durability has been extinguished, and you have no more of that item. Your damage modifier is lost!'
    """
    dm = damage_modifier
    # is the item in the dictionary
    if which_item in inventory:
        # make sure that the item is a special item
        if which_item == 'special':
            print("This item can be used once prior to being deleted.\n")
            return
        # it is not special
        else:
            # get the current item
            current_item = inventory.get(which_item)
            # check that by dulling the durability of the item, we are not deleting the item.
            # if we are deleting the item, then we need to handle it
            if (current_item['current durability'] - dullness <= 0):
                # if the item is the only one that exists, then we can just remove it
                # otherwise, we should delete the broken one and reset
                if (current_item['quantity'] > 1):
                    current_item['quantity'] -= 1
                    current_item['current durability'] = 10
                    inventory[which_item] = current_item
                    return dm, print_durability_modifier_formatted_results(current_item)
                else:
                    del inventory[which_item]
                    dm = 0
                    return dm, "Your item durability has been extinguished, and you have no more of that item. Your damage multiplier is lost!"
            else:
                current_item['current durability'] -= dullness
                inventory[which_item] = current_item
                return dm, print_durability_modifier_formatted_results(current_item)
    else:
        print("Your item durability has been depleted.\nPurchase/equip a new item.\n")

def print_durability_modifier_formatted_results(item) -> str:
    """
    This function creates a formatted string displaying item properties after durability modifications.
    It formats the item's status including name, type, quantity, durability stats, equipped status,
    and damage modifier into an aligned, readable string.

    Parameters:
        item: Dictionary containing properties of the item to be formatted

    Returns:
        str: A formatted string containing all item properties aligned in columns

    Example:
        >>> print(print_durability_modifier_formatted_results(item))
        Item: sword      Type: weapon    Quantity: 1         Max durability: 10
        Current durability: 7        Equipped: True      Damage Modifier: 5
    """
    return f"Item: {item['name']:<10} Type: {item['type']:<10} Quantity: {item['quantity']:<10} Max durability: {item['max durability']:<10}\nCurrent durability: {item['current durability']:<10} Equipped: {item['equipped']:<10} Damage Modifier: {item['damage modifier']}\n"

def equip_item(inventory) -> None:
    """
    This function allows the player to equip items from their inventory.
    It displays available items, handles special items that are auto-equipped,
    and updates the equipped status of chosen items.

    Parameters:
        inventory: Dictionary containing the player's inventory items

    Returns:
        None: Function prints messages and modifies inventory directly

    Example:

    >>> equip_item(inventory)
        Which item would you like to equip?
        Available items: sword, special
        > sword
        You have successfully equipped the item.

        >>> print(inventory['sword']['equipped'])
        True
    """
    available_items = ", ".join(inventory.keys())
    which_item = str(input(f"Which item would you like to equip?\nAvailable items: {available_items}\n"))
    if which_item in inventory:
        if which_item == 'special':
            print("This item is equipped by default, at all times.\n")
            return
        else:
            current_item = inventory.get(which_item)
            current_item['equipped'] = 'True'
            inventory[which_item] = current_item
            print("You have successfully equipped the item.\n")
    else:
        print("Unable to equip an item that is not in your inventory.\n")

def fight_monster(monster: dict, user_hp: int, user_gold: int, inventory: dict) -> tuple:
    """
    The purpose of this function is to define the interaction between the
    player and the monster when they are fighting.

    Parameters:
        monster (dict): rng monster the player will fight.
        user_hp (int): current health that the player has.
        user_gold (int): how much money the player has.
        inventory: tracks user items

    Returns:
        A tuple: w/ new health+gold when finished fighting.
    """
    print(f"A wild {monster['name']} appears! {monster['description']}")

    damage_modifier = 0
    for key in inventory.keys():
        if key == 'special':
            continue
        else:
            item = inventory[key]
            if item['equipped'] == 'True':
                damage_modifier += item_damage_modifier(key)

    if monster['name'] == 'Ghost':
        if 'special' in inventory:
            monster['health'] == 0
            print(f"You hit the {monster['name']} for {9999} dmg with the Ghost Defeater (Special Item).\n")
            user_gold += monster['money']
            del inventory['special']
            print("You have used your special item and it has been deleted from your inventory.\n")
            return user_hp, user_gold

    while user_hp > 0 and monster['health'] > 0:
        dmg_to_monster = random.randint(5, 15) + damage_modifier
        monster['health'] -= dmg_to_monster
        print(f"You hit the {monster['name']} for {dmg_to_monster} dmg with a damage modifier of {damage_modifier}\n")
        if 'sword' in inventory:
            item = inventory['sword']
            if item['equipped'] == 'True':
                dullness = 4
                dm, current_item_message = durability_modifier('sword', inventory, dullness, damage_modifier)
                damage_modifier = dm
                print(f"{current_item_message}")

        if monster['health'] <= 0:
            print(f"You killed the {monster['name']}! GG.\n")
            user_gold += monster['money']
            return user_hp, user_gold

        dmg_to_user = random.randint(3, monster['power'])
        user_hp -= dmg_to_user
        print(f"The {monster['name']} dealt {dmg_to_user} damage to you. Your health: {user_hp}\n")

        if user_hp <= 0:
            print("You died! RIP. F's in chat.\n")
            return 0, user_gold

        keep_fighting_choice = input("What do you want to do now?\n Option 1: Keep fighting\n Option 2: Run away\n")
        if keep_fighting_choice == '2':
            print("You left the battle. Coward!")
            return user_hp, user_gold

    return user_hp, user_gold

def sleep(user_hp: int, user_gold: int) -> tuple:
    """
    The purpose of this function is to increase the player health if 
    they decide to sleep, at the cost of 5 gold. They will gain 10 health in return.

    Parameters:
        user_hp: current health of the user.
        user_gold: current gold the user has.

    Returns:
        tuple: this should output the gold after sleeping.
    """
    cost = 5
    if user_gold >= cost:
        user_hp += 10
        user_gold -= cost
        print(f"ZzzZzZZzzZz... ZzzZzz.. \nYou gained 10 HP. Current health: {user_hp}, Current Gold: {user_gold}")
    else:
        print("You can't afford to sleep. You need 5 gold.")
    return user_hp, user_gold

def add_item_to_inventory(item_name, item_type, item_amount, inventory) -> dict:
    """
    This function adds or updates items in the player's inventory.
    If the item exists, it updates the quantity. If it's new, creates
    a complete item entry with durability and damage properties.

    Parameters:
        item_name: Name of the item to add
        item_type: Category of item (weapon, defense, etc.)
        item_amount: Quantity of items to add
        inventory: Player's current inventory dictionary

    Returns:
        dict: The updated or newly created item dictionary

    Example:
        >>> inventory = {}
        >>> # Adding new sword
        >>> item = add_item_to_inventory('sword', 'weapon', 1, inventory)
        >>> # Adding another sword
        >>> item = add_item_to_inventory('sword', 'weapon', 1, inventory)
        >>> print(item['quantity'])
        2
    """
    if item_name in inventory:
        item = inventory[item_name]
        item['quantity'] += item_amount
        inventory[item_name] = item
        return item

    equipped = 'False'
    if item_name == 'special':
        equipped = 'True'

    new_item = {
        "name": item_name,
        "type": item_type,
        "quantity": item_amount,
        "max durability": get_item_initial_durability(item_name),
        "current durability": get_item_initial_durability(item_name),
        "equipped": equipped,
        "damage modifier": item_damage_modifier(item_name)
    }
    inventory[item_name] = new_item
    return new_item

def get_item_initial_durability(item) -> int:
    """
    This function returns the initial durability value for different item types.
    Maps each item to its predefined maximum durability value.

    Parameters:
        item: Name of the item to get durability for

    Returns:
        int: Initial durability value:
            - sword: 10 durability
            - shield: 15 durability
            - special: 1 durability

    Example:
        >>> print(get_item_initial_durability('sword'))
        10
    """
    if item == 'sword':
        return 10
    elif item == 'shield':
        return 15
    elif item == 'special':
        return 1

def item_damage_modifier(item) -> int:
    """
    This function returns the damage modifier value for different item types.
    Maps each item to its predefined damage bonus value.

    Parameters:
        item: Name of the item to get damage modifier for

    Returns:
        int: Damage modifier value:
            - sword: +5 damage
            - shield: +0 damage
            - special: +9999 damage

    Example:
        >>> print(item_damage_modifier('sword'))
        5

    """
    if item == 'sword':
        return 5
    elif item == 'shield':
        return 0
    elif item == 'special':
        return 9999

def print_inventory(inventory) -> None:
    """
    This function displays all items in the player's inventory in a formatted table.
    Shows detailed information about each item including name, type, quantity,
    durability values, equipped status, and damage modifiers.

    Parameters:
        inventory: Dictionary containing all player items and their properties

    Returns:
        None: Function prints inventory contents directly

    Example:
        >>> print_inventory(inventory)

        Current Inventory:
        -----------------
        Item: sword      Type: weapon    Quantity: 1         Max durability: 10
        Current durability: 7        Equipped: True      Damage Modifier: 5

        >>> empty_inventory = {}
        >>> print_inventory(empty_inventory)

        Inventory is empty!
    """
    player_items = inventory
    if not player_items:
        print("\nInventory is empty!")
        return
    else:
        print("\nCurrent Inventory:")
        print("-----------------")
        for item in player_items.values():
            print(f"Item: {item['name']:<10} Type: {item['type']:<10} Quantity: {item['quantity']:<10} Max durability: {item['max durability']:<10}\nCurrent durability: {item['current durability']:<10} Equipped: {item['equipped']:<10} Damage Modifier: {item['damage modifier']}\n")

def test_functions() -> None:
    """
    This function performs comprehensive testing of all module functions
    prior to Octobers assignments. Runs test cases for print_welcome,
    print_shop_menu, purchase_item, and new_random_monster functions w/ various inputs.

    Parameters:
        None

    Returns:
        None: Function prints test results directly

    Tests performed:
        1. print_welcome: 3 tests with different names and widths
        2. print_shop_menu: 3 tests with different items and prices
        3. purchase_item: 4 tests including:
        - 3 random price/quantity combinations
        - 1 test with default quantity value
        4. new_random_monster: 3 tests generating random monsters

    Example output format:

        Testing the print_shop_menu function:

        /------------------------------------------\
        | Apple     $15.00 |
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
    print_shop_menu("Apple", 15, "Pear", 2.521, "Carrot", 5.214)
    print(f'\nShop Menu Call #2:')
    print_shop_menu("Egg", 0.78, "Pineapple", 4.24, "Eggplant", 2.742)
    print(f'\nShop Menu Call #3:')
    print_shop_menu("Bread", 0.21, "Watermelon", 8.29, "Pizza", 8.214)
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