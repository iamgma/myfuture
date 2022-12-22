# Incorporate the random library
import random

# Print Title
print(" Let's Play ROCK PAPER SCISSORS BABY!!!")

# Specify the three options
game_options = ["Rock", "Paper", "Scissors"]

# Computer Selection
computer_choice = random.choice(game_options)

# User Selection
user_choice = input("Choose Rock, Paper or Scissors:")

# Run Conditionals
if (user_choice == "Rock" and computer_choice == "Rock"):
    print("You both chose rock!") 
    print( "aka that's a tie!")

elif (user_choice == "Paper" and computer_choice == "Rock"):
    print("You chose paper and the computer chose rock!")
    print("Wowza you win!")

elif (user_choice == "Scissors" and computer_choice == "Rock"):
    print("You chose scissors and the computer chose rock!")
    print("Bummer dude, you lose!")

elif (user_choice == "Rock" and computer_choice == "Paper"):
    print("You chose rock and the computer chose paper!")
    print("Bummer dude, you lose!")

elif (user_choice == "Rock" and computer_choice == "Scissors"):
    print("You chose rock and the computer chose scissors!")
    print("Wowza you win!")

elif (user_choice == "Paper" and computer_choice == "Paper"):
    print("You both chose paper!") 
    print( "aka that's a tie!")

elif (user_choice == "Paper" and computer_choice == "Scissors"):
    print("You chose paper and the computer chose scissors!")
    print("Bummer dude, you lose!")

elif (user_choice == "Scissors" and computer_choice == "Paper"):
    print("You chose scissors and the computer chose rock!")
    print("Bummer dude, you lose!")

elif (user_choice == "Scissors" and computer_choice == "Scissors"):
    print("You both chose paper!") 
    print( "aka that's a tie!")

else:
    print("What in the world? That's not an answer for this game!")
    print("Please answer with: Rock, Paper or Scissors")