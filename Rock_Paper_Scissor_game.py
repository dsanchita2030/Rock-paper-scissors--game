# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
user=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n "))
computer_choice= random.randint(0,2)
if(user== 0):
  print(rock)
elif(user== 1):
  print(paper)
else:
  print(scissors)
print("It's computer's turn")
if(computer_choice == 0):
  print(rock)
elif(computer_choice== 1):
  print(paper)
else:
  print(scissors)
if user >= 3 or user < 0: 
  print("You typed an invalid number, you lose!") 
elif user == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user == 2:
  print("You lose")
elif computer_choice > user:
  print("You lose")
elif user > computer_choice:
  print("You win!")
elif computer_choice == user:
  print("It's a draw")
