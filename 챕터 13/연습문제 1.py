class Circle:
    def __init__(self, radius):
        self.radius = radius
    def calcPerimeter(self):
        return 2 * 3.141592 * self.radius
    def calcArea(self):
        return 3.141592 * self.radius ** 2

circle = Circle(100)
print("반지름 :", circle.radius)
print("원의 면적 :", circle.calcArea())
print("원의 둘레 :", circle.calcPerimeter())
