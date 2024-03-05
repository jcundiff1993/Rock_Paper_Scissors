import random
import time

rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissors =("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")


player_choice = int(input('What do you choose? Type "0" for Rock, "1" for Paper, or "2" for Scissors. \n '))


computer_choice = random.randint(0, 2)
print("The computer is deciding now.")
time.sleep(5)
print("Ready?")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("GO!!!")

if player_choice == 0:
    print("Player chooses:")
    print(rock)
elif player_choice == 1:
    print("Player chooses:")
    print(paper)
elif player_choice == 2:
    print("Player chooses:")
    print(scissors)
else:
    print("Player chooses:")
    print("Invalid option, read the rules!")

if computer_choice == 0:
    print("Computer chooses:")
    print(rock)
elif computer_choice == 1:
    print("Computer chooses:")
    print(paper)
else:
    print("Computer chooses:")
    print(scissors)

time.sleep(1)

if player_choice >= 3 or player_choice <0:
    print("You lose, follow the rules next time.")
elif player_choice == 0 and computer_choice == 2:
    print("You Win!")
elif player_choice == 2 and computer_choice == 0:
    print("You Lose!")
elif computer_choice < player_choice:
    print("You Win!")
elif computer_choice > player_choice:
    print("You Lose!")
elif computer_choice == player_choice:
    print("It's a draw!")
else:
    print("Follow the rules next time!")