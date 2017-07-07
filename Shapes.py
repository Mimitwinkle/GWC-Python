from turtle import *
import math
import random
import colorsys


# Name your Turtle.
tia = Turtle()

# Set Up your screen and starting position.
tia.penup()
setup(500,300)
x_pos = 0
y_pos = 50
tia.setposition(x_pos, y_pos)

### Write your code below:

sides = input("How many sides should the shape have?")
rcolor = ["powder blue","beige","light green","turquoise","pink", "violet", "blue violet"]

tia.pendown()

for t in range(int(sides)):
#    tia.fillcolor.(t/1000, 1.0, 1.0)
    tia.begin_fill()
    for s in range(int(sides)):
        tia.fillcolor(random.choice(rcolor))
        tia.pencolor(random.choice(rcolor))
        tia.forward(30)
        tia.right(360/int(sides))

    tia.left(360/int(sides))
    tia.end_fill()




exitonclick()
