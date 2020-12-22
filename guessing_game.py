"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces.

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking:
File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():
    """Psuedo-code Hints

    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".

    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.

    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.
    print("============================================")
    print("    Welcome to the Number Guessing Game!")
    print("============================================\n")

    # Running variables
    game_running = True
    game_init = True
    ai_number = random.randint(1, 10)
    number_of_guesses = 1
    high_score = 0

    while game_init:
        try:
            user_number = int(input("Choose a number between 1 and 10 \n"))
            break
        except ValueError:
            print("That isn't an number, please try again.")

    while game_running:
        # while user_number != ai_number:  # Need to fix as it doesn't load the correct answer
        if user_number > 10 or user_number < 1:
            print("The numbers MUST be between and including 1 and 10. You are outside of that range, you silly billy.")
            try:
                user_number = int(input("Try again but between 1 and 10."))
            except ValueError:
                print("That isn't an number, please try again.")
        elif user_number > ai_number:
            print("Try again but with a lower number!\n")
            try:
                user_number = int(input("Choose another number. \n"))
                number_of_guesses += 1
            except ValueError:
                print("That isn't an number, please try again.")
        elif user_number < ai_number:
            print("Try again but with a higher number!\n")
            try:
                user_number = int(input("Choose another number. \n"))
                number_of_guesses += 1
            except ValueError:
                print("That isn't an number, please try again.")
        else:
            print("You got it correct. My number is indeed, " + str(ai_number) + "!\n")
            print("It's only taken you " + str(number_of_guesses) + " guesses.")

            if high_score < number_of_guesses:
                high_score = number_of_guesses

            print("High Score: " + str(high_score))

            replay_game = input("Would you like to keep playing? [Y]es or [N]o\n").lower()
            if replay_game == "y" or replay_game == "yes":
                break
            elif replay_game == "n" or replay_game == "no":
                print("Thanks for playing!\nGood Bye...")
                game_running = False
                game_init = False
            else:
                replay_game = input("You need to either type Y for yes or N for no.\n")


# Kick off the program by calling the start_game function.
start_game()
