import tkinter

mainWindow = tkinter.Tk()

lbl = tkinter.Label(mainWindow, text = "간단한 GUI 프로그램!")
lbl.pack()

btn1 = tkinter.Button(mainWindow, text = "환영합니다.")
btn1.pack()

btn2 = tkinter.Button(mainWindow, text = "종료")
btn2.pack()

mainWindow.mainloop()
