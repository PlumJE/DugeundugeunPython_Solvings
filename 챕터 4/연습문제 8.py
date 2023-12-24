import turtle

x = [0, 0, 0]
y = [0, 0, 0]

x[0] = int(input("x1: "))
y[0] = int(input("y1: "))
x[1] = int(input("x2: "))
y[1] = int(input("y2: "))
x[2] = int(input("x3: "))
y[2] = int(input("y3: "))

t = turtle.Turtle("turtle")

t.goto(x[0], y[0])
t.goto(x[1], y[1])
t.goto(x[2], y[2])
