filename = input("파일 이름을 입력하세요 : ")
infile = open(filename, 'r')

sum = 0
for line in infile:
    words = line.split()
    for word in words:
        sum += len(word)

print("파일 안에는 총", sum, "개의 글자가 있습니다.")
