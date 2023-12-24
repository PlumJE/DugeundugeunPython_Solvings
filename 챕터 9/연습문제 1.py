alist = []
for i in range(5):
    alist.append(int(input("정수를 입력하시오: ")))
    
average = 0.0
for i in range(5):
    average += alist[i]
average /= len(alist)

print("평균=", average)
