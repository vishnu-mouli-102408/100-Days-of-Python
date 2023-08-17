import turtle as t;

tim = t.Turtle()
tim.shape("turtle")
tim.color("green")

def turn_right():
    for i in range(0,4):
        tim.forward(100)
        tim.right(90)

# turn_right()

def dashed_line():
    for i in range(15):
        tim.forward(10)
        tim.penup()
        tim.forward(10)
        tim.pendown()

# dashed_line();   

# def draw_shapes(num_sides):
#     angle = 360 / num_sides;
#     for i in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)

# for x in range(3,11):
#     draw_shapes(x)  

import random

t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

directions = [0,90,180,270]

# tim.pensize(10)
tim.speed("fastest")

# for i in range(100):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

def draw_spirograph(size):
    for i in range(int(360/size)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size)

draw_spirograph(3)        

screen = t.Screen()

screen.exitonclick()