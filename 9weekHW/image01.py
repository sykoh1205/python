from tkinter import *
window = Tk()

photo1 = PhotoImage(file="C:\\Users\\delta\\OneDrive\\바탕 화면\\git\\python\\WindowProgramming\\dog.gif")
label1 = Label(window, image=photo1)
photo2 = PhotoImage(file="C:\\Users\\delta\\OneDrive\\바탕 화면\\git\\python\\WindowProgramming\\dog2.gif")
label2 = Label(window, image=photo2)

label1.pack(side=LEFT)
label2.pack(side=RIGHT)

window.mainloop()