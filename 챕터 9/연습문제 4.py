import turtle
import random

t = turtle.Turtle("turtle")

def draw_square(x, y, c):
    t.up()
    t.goto(x, y)
    t.down()

    t.fillcolor(c)
    t.begin_fill()
    for i in range(4):
        t.forward(100)
        t.left(90)
    t.end_fill()

for c in ["yellow", "red", "purple", "blue"]:
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    draw_square(x, y, c)
