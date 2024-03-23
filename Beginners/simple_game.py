import random

print("Welcome to the game!")


def get_choice():
    player_choice = input("Enter your choice: rock, paper, or scissors! ")

    all_choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(all_choices)

    choices = {"player": player_choice, "computer": computer_choice}

    return choices


def determine_winner(player, computer):
    # print("You chose: " + player + "Computer chose: " + computer)
    print(f"You chose: {player} and computer chose: {computer}")
    if player == computer:
        return "It's a tie"
    elif player == "rock" and computer == "scissors":
        return "You win! rocky"
    elif player == "scissors" and computer == "rock":
        return "You loss! scissors"
    elif player == "paper" and computer == "rock":
        return "You win! papery"
    elif player == "rock" and computer == "paper":
        return "You loss! rocky"
    else:
        return "Invalid choice"


choices = get_choice()

player_choice = choices["player"]
computer_choice = choices["computer"]

print(determine_winner(player_choice, computer_choice))


# age = 20

# if age < 18:
#     print("You are a minor")
# elif age == 18:
#     print("You are 18")
# elif age > 18:
#     print("You are an adult")


# choices = get_choice()
# print(choices)


# def gretting():
#     return "Hello, welcome to the game!"


# gretting_response = gretting()
# print(gretting_response)

# dict = {
#     "name": "John",
#     "age": 30,
# }
