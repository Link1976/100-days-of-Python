from turtle import Turtle, Screen
import random

"""tim = Turtle()
screen = Screen()

#sketch game
def move_forwards(): 
    tim.forward(10)
def move_backwards(): 
    tim.backward(10)
def counter_clockwise(): 
    tim.left(10)
def clockwise():
    tim.right(10)
def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()

screen.listen()
screen.onkey(key = "w", fun = move_forwards)
screen.onkey(key = "s", fun = move_backwards)
screen.onkey(key = "a", fun = counter_clockwise)
screen.onkey(key = "d", fun = clockwise)
screen.onkey(key = "c", fun = clear_screen)
screen.exitonclick()"""

#turtle race
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? enter a color")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

position_y = 90
for turtle_index in range(0,6): 
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=position_y)
    all_turtles.append(new_turtle)
    position_y -= 30
    
if user_bet: 
    is_race_on = True

while is_race_on:  
    for turtle in all_turtles:
        if turtle.xcor() > 220: 
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet: 
                print(f"You've won! the {winning_color} turtle is the winner!")
            else: 
                print(f"You lose, the winner is the {winning_color} turtle")
        
        move = random.randint(0,10)
        turtle.forward(move)

screen.exitonclick()







