import turtle

color = ["", "", ""]

color[0] = input("색상 #1을 입력하시오: ")
color[1] = input("색상 #2을 입력하시오: ")
color[2] = input("색상 #3을 입력하시오: ")

t = turtle.Turtle("turtle")

t.fillcolor(color[0])
t.begin_fill()
t.circle(50)
t.end_fill()
t.forward(100)

t.fillcolor(color[1])
t.begin_fill()
t.circle(50)
t.end_fill()
t.forward(100)

t.fillcolor(color[2])
t.begin_fill()
t.circle(50)
t.end_fill()
