import turtle

t = turtle.Turtle("turtle")
t.goto(300, 0)
t.goto(0, 0)
t.goto(0, 300)
t.goto(0, 0)

def f(x):
    return x ** 2 + 1

for a in range(151):
    t.goto(a, f(a) * 0.01)
