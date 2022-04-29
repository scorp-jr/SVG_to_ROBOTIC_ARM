
from math import acos, atan2, degrees, sqrt 
import turtle

def angles(length, destination):
    x, y = destination
    third_side = sqrt(x**2 + y**2)

    alpha = acos(((length**2 + length**2) - third_side**2) / (2*length *length))
    alpha = degrees(alpha)

    beta = (180 - alpha) / 2
    beta += degrees(atan2(y, x))

    return alpha, beta

show_turtle = turtle.Turtle()
show_turtle.hideturtle()
def show(x, y, length):
    
    alpha, beta = angles(length, [x, y])

    show_turtle.up()
    show_turtle.goto(0, 0)
    show_turtle.down()
    show_turtle.seth(beta)
    show_turtle.fd(length)
    show_turtle.right(180)
    show_turtle.left(alpha)
    show_turtle.fd(length)
    show_turtle.dot()
