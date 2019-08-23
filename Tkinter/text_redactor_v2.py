from tkinter import *
from tkinter import ttk
import os

root = Tk()

# Frame - это новое поле, в котором можно укладывать элементы. Frame создают чтобы красивее уложить элементы методом pack.

frame_top = Frame(root)
frame_bot = Frame(root)
frame = Frame(root)

# Если нужно очистить текстовое поле, то нужно начинать с 1 столбца и 0 строки, и идти то END.


def open_file():
    text.delete(1.0, END)
    name_file = enter.get()
    if os.path.isfile(name_file):
        # Мы получаем название файла из однострочного поля, и открываем его с типов 'r'. Этот тип открытия файла озночает только чтение файла.
        file = open(name_file, 'r')
        text.insert(1.0, file.read())
        file.close()
    else:
        text.delete(1.0, END)
        text.insert(1.0, "File was not found.")


def save_file():
    new_text = text.get(1.0, END)
    name_file = enter.get()
    if os.path.isfile(name_file):
        # Тип открытия файла('w') озночает перезапись файла, или создание нового файла(если такого файла не существует).
        # А данный тип ('a') открывает файл, если он существует. Так же в нем можно перезаписывать.
        file = open(name_file, 'a')
        file.write(new_text)
        file.close()
        # Обязательно нужно закрывать файл, после работы с ним, чтобы не засорять память.
    else:
        text.delete(1.0, END)
        text.insert(1.0, "File was not found.")

# Далее идут функции, которая делают полноэкранный режим, и оконный. Можно не вдаваться в подробности, потому что это легче прогуглить, чем запоминать.

def set_fullscreen():
    changer['text'] = 'Windowed'
    changer['command'] = set_windowed
    root.attributes("-fullscreen", True)


def set_windowed():
    changer['text'] = 'Fullscreen'
    changer['command'] = set_fullscreen
    root.attributes("-fullscreen", False)


def delete_file():
    pass


changer = Button(frame, text="Fullscreen", command=set_fullscreen)
enter = ttk.Entry(frame_top)
opn = Button(frame_top, text="Open", command=open_file)
save = Button(frame_top, text="Save", command=save_file)
delete = Button(frame_bot, text="Delete", command=delete_file)

text = Text(frame_bot, font=("", 18), width=600, height=100)
scroll = Scrollbar(command=text.yview)
scroll.pack(side=RIGHT, fill=Y)
text.config(yscrollcommand=scroll.set)

# Сначала нужно pack'овать фреймы, а только потом элементы, которые хранятся в этих фреймах.

frame.pack()
frame_top.pack()
frame_bot.pack()

changer.pack()
enter.pack(side=LEFT)
opn.pack(side=LEFT)
save.pack(side=LEFT)
text.pack()

root.mainloop()
