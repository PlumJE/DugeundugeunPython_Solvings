import tkinter

mainWindow = tkinter.Tk()

lbl이름 = tkinter.Label(mainWindow, text="이름")
lbl이름.grid(row=0, column=0, columnspan=2)

lbl직업 = tkinter.Label(mainWindow, text="직업")
lbl직업.grid(row=1, column=0, columnspan=2)

lbl국적 = tkinter.Label(mainWindow, text="국적")
lbl국적.grid(row=2, column=0, columnspan=2)

ent이름 = tkinter.Entry(mainWindow)
ent이름.grid(row=0, column=2)

ent직업 = tkinter.Entry(mainWindow)
ent직업.grid(row=1, column=2)

ent국적 = tkinter.Entry(mainWindow)
ent국적.grid(row=2, column=2)

btnShow = tkinter.Button(mainWindow, text="Show")
btnShow.grid(row=3, column=0)

btnQuit = tkinter.Button(mainWindow, text="Quit")
btnQuit.grid(row=3, column=1)

mainWindow.mainloop()
