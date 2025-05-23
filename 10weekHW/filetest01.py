inFp = None
inStr =""

inFp = open("C:\\Users\\delta\\OneDrive\\바탕 화면\\git\\python\\10weekHW\\data1.txt","r",encoding="UTF8")

count= int(1)

while True:
    inStr=inFp.readline()
    if inStr == "":
        break;
    print("%d: %s"%(count, inStr), end="")
    count += 1


inFp.close()