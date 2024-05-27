import random

rangeInput = input("Enter highest number of range to guess: ")

if rangeInput.isdigit():
    rangeInput = int(rangeInput)

    if rangeInput <= 0:
        print("Choose a number greater than Zero (0)")
        quit()
else:
    print("Enter a number next time")
    quit()

correctNumer = random.randint(0, rangeInput)
guesses = 0

while True:
    guesses += 1
    guess = input(f"Enter a guess between -1 and {rangeInput+1}: ")

    if guess.isdigit():
        guess = int(guess)
        if guess == correctNumer:
            print("Correct guessing!")
            break
        elif guess > correctNumer:
            print("Incorrect! try again")
            print("You are above the number")
        else:
            print("Incorrect! try again")
            print("You are below the number")
    else:
        print("Enter a number!")
        continue

print("You got it after", guesses, "guesses")