import tkinter
import pickle

phone_book = {}
index = 0

mainWindow = tkinter.Tk()

이름lbl = tkinter.Label(mainWindow, text="이름")
이름lbl.grid(row=0, column=0)

이름ent = tkinter.Entry(mainWindow)
이름ent.grid(row=0, column=1, columnspan=5)

전화번호lbl = tkinter.Label(mainWindow, text="전화번호")
전화번호lbl.grid(row=1, column=0)

전화번호ent = tkinter.Entry(mainWindow)
전화번호ent.grid(row=1, column=1, columnspan=5)

추가btn = tkinter.Button(mainWindow, text="추가")
추가btn.grid(row=2, column=0)

처음btn = tkinter.Button(mainWindow, text="처음")
처음btn.grid(row=2, column=1)

다음btn = tkinter.Button(mainWindow, text="다음")
다음btn.grid(row=2, column=2)

이전btn = tkinter.Button(mainWindow, text="이전")
이전btn.grid(row=2, column=3)

마지막btn = tkinter.Button(mainWindow, text="마지막")
마지막btn.grid(row=2, column=4)

파일읽기btn = tkinter.Button(mainWindow, text="파일읽기")
파일읽기btn.grid(row=2, column=5)

def clearEntry():
    이름ent.delete(0, tkinter.END)
    전화번호ent.delete(0, tkinter.END)

def movePhoneBook(indset=None, indmove=0):
    global index
    if indset is not None:
        index = indset
    if index == 0 and indmove < 0:
        pass
    elif index == -1 and indmove > 0:
        pass
    else:
        index += indmove
    global phone_book
    name_list = list(phone_book)
    이름ent.insert(0, name_list[index])
    전화번호ent.insert(0, phone_book[name_list[index]])

def save():
    name = 이름ent.get()
    phone = 전화번호ent.get()
    global phone_book
    phone_book[name] = phone
    file = open("phone_book.dat", "wb")
    pickle.dump(phone_book, file)
    file.close()
    clearEntry()
추가btn.config(command=save)

def goFirst():
    clearEntry()
    movePhoneBook(indset=0)
처음btn.config(command=goFirst)

def Next():
    clearEntry()
    movePhoneBook(indmove=1)
다음btn.config(command=Next)

def previous():
    clearEntry()
    movePhoneBook(indmove=-1)
이전btn.config(command=previous)

def goLast():
    clearEntry()
    movePhoneBook(indset=-1)
마지막btn.config(command=goLast)

def load():
    file = open("phone_book.dat", "rb")
    global phone_book
    phone_book = pickle.load(file)
    file.close()
    goFirst()
파일읽기btn.config(command=load)

mainWindow.mainloop()
