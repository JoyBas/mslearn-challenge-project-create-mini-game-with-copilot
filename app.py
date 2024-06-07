# build a rock paper scissors game
# it will be a multiplayer game
# the game will have a welcome message
# the game will have a set of rules
# the user and the computer will play against each other
# the user will enter their choice
# which could be rock, paper, or scissors
# the user input will be in lowercase
# the user will be warned if they enter an invalid choice
# the computer will randomly select its choice
# at each round, the player must enter one of the options in the list
# the user will be informed of the computer's choice
# the players will be informed of the result of the round
# if the win, lost, or draw
# By the end of each round, the player can choose whether to play again.
# display the number of rounds played
# display the number of rounds won by each player
# display the number of rounds lost by the players


import random


def welcome_message():
    print("Welcome to the Rock Paper Scissors Game!")
    print("Here are the rules:")
    print("Rock beats Scissors")
    print("Scissors beats Paper")
    print("Paper beats Rock")
    print("You will be playing against the computer.")
    print("Enter your choice: rock, paper, or scissors.")
    print("Let's begin!")

def get_user_choice():
    user_choice = input("Enter your choice: ")
    return user_choice

def get_computer_choice():
    computer_choice = random.choice(["rock", "paper", "scissors"])
    return computer_choice

def check_winner(user_choice, computer_choice):


    if user_choice == computer_choice:
        return "draw"
    elif user_choice == "rock":
        if computer_choice == "scissors":
            return "win"
        else:
            return "lose"
    elif user_choice == "paper":
        if computer_choice == "rock":
            return "win"
        else:
            return "lose"
    elif user_choice == "scissors":
        if computer_choice == "paper":
            return "win"
        else:
            return "lose"
    else:
        return "invalid"
    
def play_game():

    welcome_message()
    rounds = 0
    wins = 0
    losses = 0
    draws = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        result = check_winner(user_choice, computer_choice)
        rounds += 1

        if result == "invalid":
            print("Invalid choice. Please enter rock, paper, or scissors.")
        else:
            print(f"Computer chose: {computer_choice}")
            if result == "win":
                wins += 1
                print("You win!")
            elif result == "lose":
                losses += 1
                print("You lose!")
            elif result == "draw":
                draws += 1
                print("It's a draw!")

        print(f"Rounds played: {rounds}")
        print(f"Rounds won: {wins}")
        print(f"Rounds lost: {losses}")
        print(f"Rounds drawn: {draws}")

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again == "no":
            break

play_game()

