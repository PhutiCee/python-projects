import turtle
import time
import random

#constants
WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']

def get_number_of_racers():
    racer = 0
    while True:
        racer = input("Enter the number of racers (2 - 10): ")
        if racer.isdigit():
            racer =int(racer)
            if 2 <= racer <= 10:
                return racer
            else:
                print("Number not in range 2-10. Try Again!")
        else:
            print("Enter numeric values... Try Again!")

def turtle_model(colors):
    turtles = []
    spaceX = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH // 2 + (i+1) * spaceX, -HEIGHT // 2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles

def race(colors):
    turtles = turtle_model(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]

def turtle_screen():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Fastest Turtle Race')

racers = get_number_of_racers()
turtle_screen()

random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
print("The winner is the turtle with color:", winner)
time.sleep(2)