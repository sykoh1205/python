from tkinter import *
from random import *

btnList = [None]*9
fnameList = ["flowers.gif", "ghost.gif", "hamburger.gif", "halloween.gif", "rgth.gif", "parrot.gif", "skeleton.gif", "skull.gif", "snowman.gif"]
photoList = [None]*9
i,k = 0,0
xPos,yPos = 0,0
num = 0

window = Tk()
window.geometry("810x810")
shuffle(photoList)

for i in range(0,9):
    photoList[i] = PhotoImage(file= "C:\\Users\\delta\\OneDrive\\바탕 화면\\git\\python\\9weekHW\\image\\"+fnameList[i])
    btnList[i] = Button(window, image=photoList[i], width=270, height=270)

for i in range(0,3):
    for k in range(0,3):
        btnList[num] = Button(window, image=photoList[num], width=270, height=270)
        btnList[num].place(x=xPos, y=yPos)
        num += 1
        xPos += 270
    xPos = 0
    yPos += 270

window.mainloop()