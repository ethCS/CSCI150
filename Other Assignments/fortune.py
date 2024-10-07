# Fortune.py
# Ethan Elliott
# 9/20/24

# This is my Fortune Teller game.
# This game uses elements of origami, commonly found in children's games.
# -------------------------------------------
# I used the same quotes from the video that the teacher provided.

# I made this primary loop so i could restart the game at the end
while True:
    while True:
        user_choice = int(input("\nWelcome to my Fortune Teller game!\nGive me an integer value from 1 to 8:\n"))
        if 1 <= user_choice <= 8:
            break
        else:
            print("You gotta choose an integer between 1 and 8.")

    # Is there a better way to do this?
    quote1 = str("You'll make a friend.\n")
    quote2 = str("It's your lucky day.\n")
    quote3 = str("You'll fall in love.\n")
    quote4 = str("Everybody likes you.\n")
    quote5 = str("You'll be rich.\n")
    quote6 = str("You'll be happy.\n")
    quote7 = str("You'll travel a lot.\n")
    quote8 = str("You'll be famous.\n")

    # Just like the video, I'm going to have certain values only be present if user_choice allows it to be visible.
    cluster_one = [7, 2, 6, 3]
    cluster_two = [8, 1, 5, 4]
    selected_cluster = []

    # Detect if even or odd input to assign cluster
    if user_choice % 2 == 0:
        selected_cluster = cluster_two
    else:
        selected_cluster = cluster_one

    print(f'\nYour current fortune possibilities are hidden behind the values of: {selected_cluster}\n')

    # Checking to make sure the second prompt is within the list of selected_cluster
    while True:
        user_choice2 = int(input("With this knowledge in mind, please choose a number in the list above.\n"))
        if user_choice2 not in selected_cluster:
            print("You didn't choose a valid number from the list above. Try again.\n")
        else:
            break

    # I wish I knew how to automate this part easier... Hmmm...
    if user_choice2 == 1:
        print(quote1)
    elif user_choice2 == 2:
        print(quote2)
    elif user_choice2 == 3:
        print(quote3)
    elif user_choice2 == 4:
        print(quote4)
    elif user_choice2 == 5:
        print(quote5)
    elif user_choice2 == 6:
        print(quote6)
    elif user_choice2 == 7:
        print(quote7)
    elif user_choice2 == 8:
        print(quote8)

    # I suppose I will ask the player if they want to restart the game on all of my assignments from here on out.
    while True:
        restart = input("Would you like to play again? (y/n):\n").lower()
        if restart == 'y' or restart == 'yes':
            break
        elif restart != 'y' or restart != 'yes':
            print("See you later alligator! ")
            exit()