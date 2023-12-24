import turtle

t = turtle.Turtle("turtle")

def hexagon():
    for i in range(6):
        t.forward(100)
        t.left(60)

for j in range(6):
    hexagon()
    t.forward(100)
    t.right(60)
