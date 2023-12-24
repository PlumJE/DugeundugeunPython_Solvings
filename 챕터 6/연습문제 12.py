import turtle
import math

t = turtle.Turtle("turtle")
t.color("red", "yellow")

for degree in range(361):
    radian = 3.14 * degree / 180.0
    t.goto(radian * 50, math.sin(radian) * 100)
