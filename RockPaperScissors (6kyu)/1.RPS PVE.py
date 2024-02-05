import random


def rps(user_action, computer_action):
    if (user_action == "scissors" and computer_action == "paper") or (
            user_action == "paper" and computer_action == "rock") or (
            user_action == "rock" and computer_action == "scissors"):
        print("You chose " + user_action + ", CPU chose " + computer_action + ". You won!")
    elif (user_action == "scissors" and computer_action == "rock") or (
            user_action == "paper" and computer_action == "scissors") or (
            user_action == "rock" and computer_action == "paper"):
        print("You chose " + user_action + ", CPU chose " + computer_action + ". CPU won!")
    elif user_action == computer_action:
        print("You and CPU have chosen " + user_action + ". It's a draw!")


user_action = input("Player, what do you choose? Pick one (rock, paper, scissors)!:")
possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)
rps(user_action, computer_action)
