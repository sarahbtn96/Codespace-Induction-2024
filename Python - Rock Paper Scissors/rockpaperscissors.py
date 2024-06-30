import random

print ("Let's play Rock, Paper Scissors!\nRock smashes Scissors. Paper covers Rock. Scissors cut Paper.")

options = ["Rock", "Paper", "Scissors"]

while True: 
    user_choice = input("Choose Rock, Paper or Scissors: ")
    computer_choice = random.choice(options)

    print("You chose: ", user_choice)
    print("Computer chose: ", computer_choice)

    if user_choice == computer_choice:

        print("Draw!")

    elif user_choice == "Rock" and computer_choice == "Scissors":

        print("You win!")

    elif user_choice == "Paper" and computer_choice == "Rock":

        print("You win!")

    elif user_choice == "Scissors" and computer_choice == "Paper":

        print("You win!")

    else:

        print("Computer wins!")

    repeat = input("\nPlay again? (yes/no): ")
    if repeat.lower() != "yes":
        print("Thanks for playing!")
        break