import turtle

t = turtle.Turtle("turtle")
t.color("blue")
t.left(90)

for i in range(6):
    t.forward(70)
    t.left(60)
    t.forward(30)
    t.forward(-30)
    t.right(60)
    t.forward(30)
    t.forward(-30)
    t.right(60)
    t.forward(30)
    t.forward(-30)
    t.left(60)
    t.forward(-70)
    t.right(60)
