#outFp = None
#outStr = ""

#outFp = open("C:\\Users\\delta\\OneDrive\\바탕 화면\\git\\python\\10weekHW\\data2.txt", "w", encoding="utf=8")

#while True:
#    outStr = input("내용 입력: ")
#    if outStr != "":
#        outFp.writelines(outStr + "\n")
#    else:
#        break

#outFp.close()
#print("---정상적으로 파일에 씀---")

outFp = None
outStr = ""
fname = input("파일명 입력하세요: ")

outFp = open(fname, "w", encoding= "utf-8")

while True:
    outStr = input("내용 입력: ")
    if outStr != "":
        outFp.writelines(outStr + "\n")
    else:
        break

outFp.close()
print("---정상적으로 파일에 씀---")

