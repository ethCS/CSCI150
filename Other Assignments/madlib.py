#madlib.py
#Ethan Elliott
#9/6/24

#Below, you will find comments for the teacher.
#This program implements the word-game Mad Libs (for the 9/8/24 assignment).
#The user is prompted for a list of words that are substituted for blanks in a story.

#--------------------------------------------------------

#This is an intro where I explain what the game is about to the user via print statement:
print("\nHello, and welcome to Ethan's 'Mad Libs' word-game!\nTo play, please answer the following questions below:\n")

#This is where I pull the information from the user with descriptive questions.
#I put these input requests under a function named mad_libs so I could call it in the while loop below.
def mad_libs():
    Question1_adjective1 = input("Enter an adjective to describe an adventurer: \n").strip().lower()
    Question2_adjective2 = input("Enter an adjective to describe a creature: \n").strip().lower()
    Question3_gender = input("Enter a gender (example: man, woman): \n").strip().lower()
    Question4_adventurer_name = input("Enter the name associated with the previously mentioned gender: \n").strip().title()
    Question5_creature_name = input("Enter a name for the creature: \n").strip().title()
    Question6_place = input("Enter a place: \n").strip().title()
    Question7_magical_object1 = input("Enter a magical object: \n").strip().lower()
    Question8_magical_object2 = input("Enter another magical object: \n").strip().lower()

    #I made this variable because I'm using it more than once, and I think it looks nicer than without it.
    organize_with_dashes = ("-----------------------")

#Here, I will create variables that define what the print statements will output.
    preview = ("\nYour story is written below.")

#This story was a template from online that I added my own variables to and slightly modified the questions/wording.
    story = (
        "Once upon a time, a " + Question1_adjective1 + " " + Question3_gender + " named " + Question4_adventurer_name +
        " embarked on an incredible journey. With a " + Question7_magical_object1 + " in hand, they ventured into the mystical land of " +
        Question6_place + ". During their travels, they met a " + Question2_adjective2 + " creature named " + Question5_creature_name +
        " who was guarding a magical " + Question8_magical_object2 + ".\n\nTo pass the guardian, " + Question4_adventurer_name +
        " had to solve a tricky riddle: “I am " + Question1_adjective1 + " and " + Question2_adjective2 +
        ". I can be found in " + Question6_place + " but I'm never to be seen with a " + Question7_magical_object1 + ". What am I?” After solving the riddle, " +
        Question4_adventurer_name + " retrieved the magical " + Question8_magical_object2 + " and used it to bring happiness to " +
        Question6_place + ", living " + Question1_adjective1 + " and " + Question2_adjective2 + " ever after."
    )

#Print the variables defined above, in order.
    print(preview)
    print(organize_with_dashes)
    print(story)
    print(organize_with_dashes)

#Added replay functionality. Teacher suggested to use a while loop so I learned how to use them.
#I also learned a lot about scope doing this, in addition to the strip/lower/upper/title modifiers.
while True:
    mad_libs()

    do_you_want_to_play_again = input("Do you want to play again? (Type: 'y' or 'n'):\n").strip().lower()
    if do_you_want_to_play_again != 'y':
        print('\nThank you for playing my game. Goodbye!\n')
        break