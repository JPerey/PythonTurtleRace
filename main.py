from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)



# Methods

def create_turtles(turtle_amt):
    turtle_list_inner = []
    for i in range(turtle_amt):
        turtle_list_inner.append(Turtle())
        turtle_list_inner[i].shape("turtle")
        turtle_list_inner[i].penup()
        turtle_list_inner[i].fillcolor((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    return turtle_list_inner


def turtle_positions(turtle_list_second_inner):
    screen_height = (amount_turtles * 10) + 20
    turtle_distances = (screen_height / amount_turtles) + 5
    turtle_i = 0
    for i in range(len(turtle_list_second_inner)):
        turtle_list_second_inner[i].setpos(-200, (screen_height / 2) - (turtle_distances * turtle_i))
        turtle_i += 1
    return turtle_list_second_inner


# timeline

print("Welcome to the turtle races!!")
amount_turtles = int(input("How many turtles in the race?: whole numbers only"))
who_will_win = int(input("Which turtle # do you think will win?: "))

turtle_list = create_turtles(amount_turtles)
screen.setup(width=400, height=((amount_turtles * 20) + 20), startx=0, starty=0)
t_list_with_positions = turtle_positions(turtle_list)


screen.exitonclick()