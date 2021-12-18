from random import choice
import random
choice = ["rock", "paper", "scissors"]
while True:
    computer = random.choice(choice)
    player = None
    while player not in choice:
        player = input("Pick rock, paper or scissors: ").lower()
    print("You picked: ", player)
    print("Computer picked: ", computer)
    if player == computer:
        print("Tie!") 
    elif player == "rock":
        if computer == "paper":
            print("You lose!")
        if computer == "scissors":
            print("You win!")
    elif player == "scissors":
        if computer == "rock":
            print ("You lose!")
        if computer == "paper":
            print ("You win!")
    elif player == "paper":
        if computer == "scissors":
            print ("You lose!")
        if computer == "rock":
            print ("You win!")
    cont = input("Do you want to continue? (y/n): ").lower()
    if cont != "y":
        break
print ("Bye!")