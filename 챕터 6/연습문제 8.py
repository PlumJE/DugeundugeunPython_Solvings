import turtle

t = turtle.Turtle("turtle")
t.color("red")
t.left(180)

for i in range(10):
    for j in range(5):
        t.forward(200)
        t.right(144)
    t.left(10)
