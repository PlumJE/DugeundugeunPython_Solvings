import turtle

class MyTurtle(turtle.Turtle):  #Myturtle은 Turtle를 상속
    def drawSquare(self):
        for i in range(4):
            self.right(90)
            self.forward(100)

my_turtle = MyTurtle()
my_turtle.forward(100)
my_turtle.drawSquare()
