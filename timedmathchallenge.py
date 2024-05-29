import random
import time

MAX_VAL = 12
MIN_VAL = 1
OPERATORS = ["+", "-", "*"]
TOTAL_PROB = 10

def gen_prob():
    left = random.randint(MIN_VAL, MAX_VAL)
    right = random.randint(MIN_VAL, MAX_VAL)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer

score = 0
print("Press Enter to start")
print("-----------------------")

star_time = time.time()
for i in range(TOTAL_PROB):
    expr, answer = gen_prob()
    while True:
        guess = input("problem #" + str(i+1) + ": " + expr + " = ")
        if guess == str(answer):
            break
        score += 1
end_time = time.time()
total_time = end_time - star_time

print("-----------------------")
print(f"You finished in {round(total_time)} seconds ")
