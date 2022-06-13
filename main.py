import random

while True:
    choices = ["rock","paper","scissors"]

    computer_input = random.choice(choices)
    user_input = None

    while user_input not in choices:
        user_input = input("rock, paper, or scissors?: ").lower()

    if user_input == computer_input:
        print("CPU:", computer_input)
        print("player:", user_input)
        print("Tie:")
    
    elif user_input == "rock":
        if computer_input == "scissors":
            print("CPU:", (computer_input))
            print("player:", (user_input))
            print("Winner!")
        if computer_input == "paper":
            print("CPU:", (computer_input))
            print("player:", (user_input))
            print("You Lose!")
        
    elif user_input == "paper":
        if computer_input == "scissors":
            print("CPU:", computer_input)
            print("player:", user_input)
            print("You Lose!")
        if computer_input == "rock":
            print("CPU:", computer_input)
            print("player:", user_input)
            print("Winner!") 
                               
    elif user_input == "scissors":
        if computer_input == "rock":
            print("CPU:", computer_input)
            print("player:", user_input)
            print("You Lose!")
        if computer_input == "paper":
            print("CPU:", computer_input)
            print("player:", user_input)
            print("Winner!")
        
    play_again = input("Play again? (yes/no):").lower()

    if play_again != "yes":
        break
    
print("Bye!")