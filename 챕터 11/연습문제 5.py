infilename = input("입력 파일 이름 : ")
infile = open(infilename, "r")

sum = 0.0
count = 0
for line in infile:
    sum += float(line)
    count += 1
average = sum / count

outfilename = input("출력 파일 이름 : ")
outfile = open(outfilename, "w")

outfile.write("합계="+str(sum)+"\n")
outfile.write("평균="+str(average))

infile.close()
outfile.close()
