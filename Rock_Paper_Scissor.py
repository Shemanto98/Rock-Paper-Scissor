import random

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

image = [rock, paper, scissors]
choice1 = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if choice1 < 0 or choice1 > 2:
  print("Your typed an invalid number, you lose!")
else:
  print(image[choice1])

comp_choice = random.randint(0,2)
print("Computer Choose:")
print(image[comp_choice])

if (choice1 == 0 and comp_choice == 2) or \
   (choice1 == 2 and comp_choice == 1) or \
   (choice1 == 1 and comp_choice == 0): 
  print("You Win!")
elif choice1 == comp_choice:
  print("It's a draw!")
else:
  print("You lose!")