import tkinter

total = 100

def add():
    global total
    total += int(ent숫자입력.get())
    lbl숫자출력['text'] = str(total)

def sub():
    global total
    total -= int(ent숫자입력.get())
    lbl숫자출력['text'] = str(total)

def initialize():
    global total
    total = 100
    lbl숫자출력['text'] = str(total)

#GUI 디자인
mainWindow = tkinter.Tk()

lbl현재합계 = tkinter.Label(mainWindow, text="현재 합계:")
lbl현재합계.grid(row=0, column=0)

lbl숫자출력 = tkinter.Label(mainWindow, text=str(total))
lbl숫자출력.grid(row=0, column=1)

ent숫자입력 = tkinter.Entry(mainWindow)
ent숫자입력.grid(row=1, column=0, columnspan=3)

btn더하기 = tkinter.Button(mainWindow, text="더하기(+)", command=add)
btn더하기.grid(row=2, column=0)

btn빼기 = tkinter.Button(mainWindow, text="빼기(-)", command=sub)
btn빼기.grid(row=2, column=1)

btn초기화 = tkinter.Button(mainWindow, text="초기화", command=initialize)
btn초기화.grid(row=2, column=2)

mainWindow.mainloop()
