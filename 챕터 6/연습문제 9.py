import turtle
import random

t = turtle.Turtle("turtle")

for i in range(10):
    t.up()
    t.goto(random.randint(-300, 300), random.randint(-100, 100))
    t.down()
    t.circle(random.randint(1, 100))
