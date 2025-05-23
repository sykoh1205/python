from tkinter import *
from time import *

fnameList = ["flowers.gif", "ghost.gif", "hamburger.gif", "halloween.gif", "rgth.gif", "parrot.gif", "skeleton.gif", "skull.gif", "snowman.gif"]
photoList = [None]*9
num = 0

def clickNext():
    global num
    num +=1
    if num > 8:
        num = 0
    photo = PhotoImage(file="C:\\Users\\delta\\OneDrive\\바탕 화면\\git\\python\\9weekHW\\"+fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image = photo
    label1.configure(text=fnameList[num])
    label1.pack()

def clickPrev():
    global num
    num -=1
    if num < 0:
        num = 8
    photo = PhotoImage(file="C:\\Users\\delta\\OneDrive\\바탕 화면\\git\\python\\9weekHW\\"+fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image = photo
    label1.configure(text=fnameList[num])
    label1.pack()

window = Tk()
window.geometry("700x500")
window.title("사진 앨범 보기")

btnPrev = Button(window, text = "<<< 이전", command=clickPrev)
btnNext = Button(window, text = "다음 >>>", command=clickNext)

photo = PhotoImage(file="C:\\Users\\delta\\OneDrive\\바탕 화면\\git\\python\\9weekHW\\"+fnameList[0])
pLabel = Label(window, image=photo)
label1 = Label(window, text=fnameList[num])

btnPrev.place(x = 200, y = 10)
btnNext.place(x = 400, y = 10)
pLabel.place(x = 200, y = 50)
label1.place(x = 300, y = 20)

window.mainloop()