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
        turtle_list_inner[i].speed(3)
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


def turtle_race(move_em):
    finished = False
    while not finished:
        turtle_num = 1
        for i in move_em:
            i.forward(random.randint(0, 30))
            if i.xcor() > 400:
                finished = True
                return turtle_num
            turtle_num += 1


# timeline

print("Welcome to the turtle races!!")
amount_turtles = int(screen.numinput("amount of turtles", "How many turtles would you want in the race?", 5, minval=2,
                                     maxval=30))
who_will_win = int(screen.numinput("who will win", "Which turtle do you think will win?", 5))

turtle_list = create_turtles(amount_turtles)
screen.setup(width=400, height=((amount_turtles * 20) + 20), startx=0, starty=0)
t_list_with_positions = turtle_positions(turtle_list)
winner = turtle_race(t_list_with_positions)
if winner == who_will_win:
    print(f"you picked turtle #{winner}, the winner! get to the races!")
else:
    print(f"sorry chum, you picked {who_will_win}, but the winner was {winner}. good luck next time!")

screen.exitonclick()
