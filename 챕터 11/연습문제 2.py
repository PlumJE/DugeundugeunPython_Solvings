filename = input("파일 이름을 입력하세요 : ")
infile = open(filename, 'r')
originalStr = infile.read()
print("원래 문자열 :", originalStr, "\n")

delStr = input("삭제할 문자열을 입력하세요 : ")
modifiedStr = originalStr.replace(delStr, "")
print("변경된 문자열 :", modifiedStr, "\n")

outfile = open(filename, 'w')
outfile.write(modifiedStr)
print("변경된 파일이 저장되었습니다.")

infile.close()
outfile.close()
