import turtle
import random

def draw_shape(t, c, length, sides, x, y):
    t.up()
    t.goto(x, y)
    t.down()

    t.fillcolor(c)
    t.begin_fill()
    for i in range(sides):
        t.forward(length)
        t.left(360 / sides)
    t.end_fill()

t = turtle.Turtle("turtle")

for c in ["red", "orange", "yellow", "green", "blue", "purple", "pink"]:
    length = random.randint(10, 100)
    sides = random.randint(3, 6)
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    draw_shape(t, c, length, sides, x, y)
