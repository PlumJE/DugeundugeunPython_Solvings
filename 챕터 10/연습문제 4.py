import tkinter

def convert():
    inch_val = float(ent인치입력.get())
    lbl센치결과['text'] = str(inch_val * 2.54)

#GUI 디자인
mainWindow = tkinter.Tk()

lbl제목 = tkinter.Label(mainWindow, text="인치를 센티미터로 변환하는 프로그램")
lbl제목.grid(row=0, column=0, columnspan=2)

lbl인치 = tkinter.Label(mainWindow, text="인치(inch)")
lbl인치.grid(row=1, column=0)

ent인치입력 = tkinter.Entry(mainWindow)
ent인치입력.grid(row=1, column=1)

lbl센티미터 = tkinter.Label(mainWindow, text="센티미터(cm)")
lbl센티미터.grid(row=2, column=0)

lbl센치결과 = tkinter.Label(mainWindow, text="0")
lbl센치결과.grid(row=2, column=1)

btn변환 = tkinter.Button(mainWindow, text="변환!", command=convert)
btn변환.grid(row=3, column=1)

mainWindow.mainloop()
