import random

options = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0

while True:
    user_choice = input("Choose between Rock/Paper/Scissors or q to quit: ").lower()

    if user_choice == "q":
        break
    if user_choice not in options:
        continue
    
    # Generate random number to pick choice for computer
    random_number = random.randint(0, 2)
    computer_choice = options[random_number]
    print("Computer picked", computer_choice + ".")

    if user_choice == options[0] and computer_choice == options[2]:
        print("You won!")
        user_score += 1
    elif user_choice == options[1] and computer_choice == options[0]:
        print("You won!")
        user_score += 1
    elif user_choice == options[2] and computer_choice == options[1]:
        print("You won!")
        user_score += 1
    else:
        print("You lose!")
        computer_score += 1

print("Results:")
print("User score: ",user_score)
print("Computer score: ",computer_score)
print("Goodbye!")