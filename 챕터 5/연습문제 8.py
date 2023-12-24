import turtle

x1 = int(input("큰 원의 중심좌표 x1: "))
y1 = int(input("큰 원의 중심좌표 y1: "))
r1 = int(input("큰 원의 반지름: "))
x2 = int(input("작은 원의 중심좌표 x2: "))
y2 = int(input("작은 원의 중심좌표 y2: "))
r2 = int(input("작은 원의 반지름: "))

t = turtle.Turtle("turtle")

t.up()
t.goto(x1, y1-r1)
t.down()
t.circle(r1)

t.up()
t.goto(x2, y2-r2)
t.down()
t.circle(r2)

distance = ((x2-x1)**2 + (y2-y1)**2)**0.5
if distance <= r1 - r2:
    t.write("두번째 원이 첫번째 원의 내부에 있습니다.")
