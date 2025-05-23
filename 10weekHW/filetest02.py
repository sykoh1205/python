inFp = None
inList, inStr = [], ""

inFp = open("C:\\Users\\delta\\OneDrive\\바탕 화면\\git\\python\\10weekHW\\data1.txt", "r", encoding="utf-8")

inList = inFp.readlines()
count = 1

for inStr in inList:
    print("%d: %s"%(count, inStr), end="")
    count += 1

inFp.close()