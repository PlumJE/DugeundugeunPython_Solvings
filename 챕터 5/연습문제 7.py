import random

solution = int(input("복권번호를 입력하시오(0에서 99사이): "))
digit1 = solution // 10
digit2 = solution % 10

answer = random.randint(0, 99)
print("당첨번호는", answer, "입니다.")
digit3 = answer // 10
digit4 = answer % 10

if digit1 == digit3:
    if digit2 == digit3:
        print("상금은 100만원입니다.")
    elif digit2 == digit4:
        print("상금은 100만원입니다.")
    else:
        print("상금은 50만원입니다.")
elif digit1 == digit4:
    if digit2 == digit3:
        print("상금은 100만원입니다.")
    elif digit2 == digit4:
        print("상금은 100만원입니다.")
    else:
        print("상금은 50만원입니다.")
else:
    if digit2 == digit3:
        print("상금은 50만원입니다.")
    elif digit2 == digit4:
        print("상금은 50만원입니다.")
    else:
        print("상금은 없습니다.")
