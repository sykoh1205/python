inFp, outFp = None, None
inStr = ""


sFname = input("소스 파일명 입력하세요: ")
tFname = input("타깃 파일명 입력하세요: ")

inFp = open(sFname, "r", encoding="utf-8")
outFp = open(tFname, "w", encoding="utf-8")

inList = inFp.readlines()
for inStr in inList:
    outFp.writelines(inStr)

inFp.close()
outFp.close()
print("---파일이 정상적으로 복사되었음---")