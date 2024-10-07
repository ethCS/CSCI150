#Ethan Elliott
#ZyLabs Game Creation
#September, 2024
#CSCI150

#This is the python file for the GameCreation zyLabs assignment.
#This file was included in the github directory just incase it is required for the Adventure Game Project. 
#If not, disregard the existence of this file. 


def name():
    name_input = input('What is your name?\n')
    return name_input

def choose_class(player_name):
    class_type = input(f'Choose a class for {player_name} (Warrior, Mage, Rogue): ').strip().lower()
    if class_type == 'warrior' or class_type == 'w':
        return ("Warrior", 200, "Shield_Block")
    elif class_type == 'mage' or class_type == 'm':
        return ("Mage", 100, "Fireball")
    elif class_type == 'rogue' or class_type == 'r':
        return ("Rogue", 150, "Backstab")
    else:
        print('That is not an allowed class')
        return None

def get_weapon_options(class_type):
    if class_type[0].lower() == 'warrior' or class_type[0].lower() == 'w':
        return ['Sword', 'Axe']
    elif class_type[0].lower() == 'mage' or class_type[0].lower() == 'm':
        return ['Staff', 'Wand']
    elif class_type[0].lower() == 'rogue' or class_type[0].lower() == 'r':
        return ['Dagger', 'Bow']
    else:
        print(f'{class_type[0]} is not valid.')
        return None

def choose_weapon(class_type):
    weapon_options = get_weapon_options(class_type)

    if weapon_options is None:
        return None

    if class_type[0].lower() == 'warrior' or class_type[0].lower() == 'w':
        weapon_choice = input('Choose a weapon for your Warrior (Sword, Axe): ').strip()
    elif class_type[0].lower() == 'mage' or class_type[0].lower() == 'm':
        weapon_choice = input('Choose a weapon for your Mage (Staff, Wand): ').strip()
    elif class_type[0].lower() == 'rogue' or class_type[0].lower() == 'r':
        weapon_choice = input('Choose a weapon for your Rogue (Dagger, Bow): ').strip()
    else:
        print('That class type is not recognized.')
        return None

    if weapon_choice.capitalize() in weapon_options:
        return weapon_choice.capitalize()
    else:
        print('That weapon type is not allowed')
        return None

if __name__ == "__main__":
    player_name = name()
    chosen_class = choose_class(player_name)
    if chosen_class is not None:
        chosen_weapon = choose_weapon(chosen_class)