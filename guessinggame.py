import random


top_range = input("Set top range of number: ")

if top_range.isdigit():
    top_range = int(top_range)
    if top_range <=0:
        print("Enter number greater than 0")
        quit()
else:
    print("Enter a valid number")
    quit()

rand_num = random.randint(1, top_range)
guesses = 0
while True:
    guesses += 1
    guess_num = input("Guess a number: ")
    if guess_num.isdigit():
        guess_num = int(guess_num)
    else:
        print("Enter a valid number")
        continue
    
    if guess_num > rand_num:
        print(f"You got it wrong! Correct Number is lesser than {guess_num}")
    elif guess_num < rand_num:
        print(f"You got it wrong! Correct Number is greater than {guess_num}")
    else:
        print("You got it right!")
        break
print("You got it right in", guesses, "guesses")