import random

print ("Let's play Rock, Paper Scissors!\nRock smashes Scissors. Paper covers Rock. Scissors cut Paper.")

options = ["Rock", "Paper", "Scissors"]
player_score = 0
computer_score = 0

while True: 
    user_choice = input("Choose Rock, Paper or Scissors: ")
    computer_choice = random.choice(options)

    print("You chose: ", user_choice)
    print("Computer chose: ", computer_choice)

    if user_choice == computer_choice:

        print("Draw!")

    elif user_choice == "Rock" and computer_choice == "Scissors":

        print("You win!")
        player_score += 1

    elif user_choice == "Paper" and computer_choice == "Rock":

        print("You win!")
        player_score += 1

    elif user_choice == "Scissors" and computer_choice == "Paper":

        print("You win!")
        player_score += 1

    else:

        print("Computer wins!")
        computer_score += 1
        
    print("Scores:")
    print("Computer:", computer_score)
    print("Player:", player_score)
    
    repeat = input("\nPlay again? (yes/no): ")
    if repeat.lower() != "yes":
        print("Thanks for playing!")
        break
        
    
