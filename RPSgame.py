import random

Player1 = 0
Computer = 0

options = ["rock", "paper", "scissors"]


while True:
    user_input = input("Enter Rock, Paper, Scissors to play or Q to Quit: ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue
    
    rand_guess = random.randint(0, 2)
    # Rock = 0, Paper = 1, Scissors = 2
    computer_guess = options[rand_guess]
    print(f"Computer picked {computer_guess}.")
    if user_input == "rock" and computer_guess == "scissors":
        print("You won")
        Player1 += 1
    elif user_input == "paper" and computer_guess == "rock":
        print("You won")
        Player1 += 1
    elif user_input == "scissors" and computer_guess == "paper":
        print("You won")
        Player1 += 1
    else:
        print("You lost")
        Computer += 1

print(f"Player1 won {Player1} times")
print(f"Computer won {Computer} times")


