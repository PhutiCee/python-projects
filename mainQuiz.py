import random
import time

OPERATORS =["+", "-", "*"]
MIN_OPARAND = 1
MAX_OPARAND = 12
TOTAL_PROBLEMS = 5

def generate_problems():
    left = random.randint(MIN_OPARAND,MAX_OPARAND)
    right = random.randint(MIN_OPARAND,MAX_OPARAND)
    oparator = random.choice(OPERATORS)

    expression = str(left) + " " + oparator + " " + str(right)
    answer = eval(expression)
    return expression, answer

input("Press ENTER to start!")
time_start = time.time()
print("---------------------------------------")

for i in range(TOTAL_PROBLEMS):
    expression, answer = generate_problems()
    while True:
        problem = input("Problem #" + str(i+1) + ": "+ expression+ " = ")

        if problem == str(answer):
            break
        else:
            continue

time_finish = time.time()
total_time = time_finish - time_start
print("---------------------------------------")
print("You finished in", round(total_time, 2),"seconds!")