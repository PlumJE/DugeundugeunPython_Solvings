import random

x = random.randint(0, 9)
y = random.randint(0, 9)
answer = x * y - 1

while answer != x * y:
    answer = int(input(str(x) + "*" + str(y) + "는"))
print("맞았습니다.")
    
