import random

print("Welcome to Dan's game of Rock, Paper, Scissors\n")
allowed_list = ("rock", "paper", "scissors", "thermo-nuclear detonation")
player_choice = str.lower (input("Enter your choice: "))

if player_choice in allowed_list:
    pass

else:
    quit(" You are not allowed to choose " + player_choice + "\n You can only choose from Rock, Paper or Scissors")

def play(num):
    return random.randint(1, num)

ai_choice = (play(3))

if ai_choice == 1:
    print(" The computor chooses Rock")
    if player_choice == 'rock':
        print(" You both choose Rock, No winners!")
    elif player_choice == 'paper':
        print(" You choose Paper\n Paper wraps Rock\n You Win!")
    elif player_choice == 'scissors':
        print(" You choose Scissors\n Rock blunts Scissors\n You Lose!")
    else:
        print(" You choose Thermo-nuclear detonation\n As the dust settled you see everything is obliterated. \n You Win I guess!")

elif ai_choice ==2:#
    print(" The Computor chooses Paper")
    if player_choice == 'paper':
        print(" You both choose Paper, No winners!")
    elif player_choice == 'scissors':
        print(" You choose Scissors\n Scissors cut Paper\n You Win!")
    elif player_choice == 'rock':
        print(" You choose Rock\n Paper wraps Rock\n You Lose!")
    else:
        print(" You choose Thermo-nuclear detonation\n As the dust settled you see everything is obliterated. \n You Win I guess!")

else:
    print(" The Computor chooses Scissors")
    if player_choice == 'scissors':
        print(" You both choose Scissors, No winners!")
    elif player_choice == 'rock':
        print(" You choose Rock\n Rock blunts Scissors\n You Win!")
    elif player_choice == 'paper':
        print(" You choose paper\n Scissors cut Paper\n You Lose!")
    else:
        print(" You choose Thermo-nuclear detonation\n As the dust settled you see everything is obliterated. \n You Win I guess!")


