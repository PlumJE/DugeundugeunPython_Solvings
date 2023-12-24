import tkinter
import random

answer = 0
guess = -1

def enterNumber():
    global answer
    global guess
    guess = int(ent숫자입력.get())
    if answer < guess:
        lbl대소비교['text'] = "너무 높아요!!"
    elif answer > guess:
        lbl대소비교['text'] = "너무 낮습니다!!"
    else:
        lbl대소비교['text'] = "정답입니다!!"

def reset():
    global answer
    answer = random.randint(0, 100)
    lbl대소비교['text'] = "숫자 맞추기 게임!!"

#GUI 디자인 부분
mainWindow = tkinter.Tk()

lbl대소비교 = tkinter.Label(mainWindow)
lbl대소비교.grid(row=0, column=0, columnspan=2)

reset()

ent숫자입력 = tkinter.Entry(mainWindow)
ent숫자입력.grid(row=1, column=0, columnspan=2)

btn숫자입력 = tkinter.Button(mainWindow, text="숫자를 입력", command=enterNumber)
btn숫자입력.grid(row=2, column=0)

btn게임재시작 = tkinter.Button(mainWindow, text="게임을 다시 실행", command=reset)
btn게임재시작.grid(row=2, column=1)

mainWindow.mainloop()
