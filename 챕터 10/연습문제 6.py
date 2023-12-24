import tkinter
import random

def 컴퓨터차례():
    RCPnumber = random.randint(1, 3)
    if RCPnumber == 1:
        lbl컴퓨터['text'] = "가위"
    elif RCPnumber == 2:
        lbl컴퓨터['text'] = "바위"
    elif RCPnumber == 3:
        lbl컴퓨터['text'] = "보"
    
def 가위():
    lbl사용자['text'] = "가위"
    컴퓨터차례()
    if lbl컴퓨터['text'] == "가위":
        lbl결과['text'] = "무승부!"
    elif lbl컴퓨터['text'] == "바위":
        lbl결과['text'] = "컴퓨터 승!"
    elif lbl컴퓨터['text'] == "보":
        lbl결과['text'] = "사용자 승!"

def 바위():
    lbl사용자['text'] = "바위"
    컴퓨터차례()
    if lbl컴퓨터['text'] == "가위":
        lbl결과['text'] = "사용자 승!"
    elif lbl컴퓨터['text'] == "바위":
        lbl결과['text'] = "무승부!"
    elif lbl컴퓨터['text'] == "보":
        lbl결과['text'] = "컴퓨터 승!"

def 보():
    lbl사용자['text'] = "보"
    컴퓨터차례()
    if lbl컴퓨터['text'] == "가위":
        lbl결과['text'] = "컴퓨터 승!"
    elif lbl컴퓨터['text'] == "바위":
        lbl결과['text'] = "사용자 승!"
    elif lbl컴퓨터['text'] == "보":
        lbl결과['text'] = "무승부!"

#GUI 디자인
mainWindow = tkinter.Tk()

lbl사용자 = tkinter.Label(mainWindow, text="(준비)")
lbl사용자.grid(row=0, column=0)

lblVS = tkinter.Label(mainWindow, text="사용자 vs 컴퓨터")
lblVS.grid(row=0, column=1)

lbl컴퓨터 = tkinter.Label(mainWindow, text="(준비)")
lbl컴퓨터.grid(row=0, column=2)

lbl결과 = tkinter.Label(mainWindow, text="(준비)")
lbl결과.grid(row=1, column=1)

btn가위 = tkinter.Button(mainWindow, text="가위", command=가위)
btn가위.grid(row=2, column=0)

btn바위 = tkinter.Button(mainWindow, text="바위", command=바위)
btn바위.grid(row=2, column=1)

btn보 = tkinter.Button(mainWindow, text="보", command=보)
btn보.grid(row=2, column=2)

mainWindow.mainloop()
