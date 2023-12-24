import turtle

def draw_line():
    turtle.forward(100)
    turtle.backward(100)
    turtle.right(30)

t = turtle.Turtle("turtle")
for i in range(12):
    draw_line()
