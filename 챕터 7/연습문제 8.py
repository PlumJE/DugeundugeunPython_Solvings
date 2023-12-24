def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

x = int(input("정수를 입력하시오: "))
y = int(input("정수를 입력하시오: "))

print(x, "+", y, "=", add(x, y))
print(x, "-", y, "=", sub(x, y))
print(x, "*", y, "=", mul(x, y))
print(x, "/", y, "=", div(x, y))
