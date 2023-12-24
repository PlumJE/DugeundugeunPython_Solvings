import turtle
import random

t = turtle.Turtle()
t.shape("turtle")
t.color("black", "white")
s = turtle.Screen()
s.bgcolor("skyblue")

def draw_snowman(x, y):
    t.up()
    t.goto(x, y)
    t.down()
    t.begin_fill()
    t.circle(30)
    t.end_fill()
    
    t.up()
    t.goto(x, y - 30)
    t.down()
    t.begin_fill()
    t.circle(20)
    t.end_fill()

    t.left(30)
    t.forward(50)
    t.backward(50)
    t.left(120)
    t.forward(50)
    t.backward(50)
    t.right(150)
    
    t.up()
    t.goto(x, y - 100)
    t.down()
    t.begin_fill()
    t.circle(40)
    t.end_fill()

for i in range(3):
    draw_snowman(random.randint(-300, 300), random.randint(-200, 200))
