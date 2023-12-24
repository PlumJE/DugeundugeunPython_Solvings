import turtle
import random

def draw_star(color, length, x, y):
    t.up()
    t.goto(x, y)
    t.down()

    t.color(color)
    t.begin_fill()
    for i in range(5):
        t.forward(length)
        t.right(144)
    t.end_fill()

t = turtle.Turtle("turtle")
s = turtle.Screen()
s.bgcolor("black")

for color in ["red", "orange", "yellow", "green", "blue", "purple", "pink"]:
    length = random.randint(50, 100)
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    draw_star(color, length, x, y)
