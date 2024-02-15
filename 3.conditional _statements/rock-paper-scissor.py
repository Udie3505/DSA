'''
rock paper scissor
'''
import random

options = ["rock", "paper","scissor"]
computer_choice = random.choice(options)
print(computer_choice)
user_choice:str = input("enter the action of 1st person :")


if user_choice == computer_choice:
    print("It's a tie")
elif (
    (user_choice == 'rock' and computer_choice == 'scissor') or
    (user_choice == 'paper' and computer_choice == 'rock') or
    (user_choice == 'scissor' and computer_choice == 'paper')
):
    print("You win")
else:
    print("Computer wins")