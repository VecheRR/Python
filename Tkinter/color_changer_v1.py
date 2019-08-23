from tkinter import *

root = Tk()

color = Label(root)
code = Entry(root)


# delete - это функция, которая принимает на вход 'Entry' или 'Text'. Так как это поля ввода, то из этих полей можно и удалить.
# insert - это функция, вставляющая в 'Entry' или 'Text' какой-то текст.

def set_purple():
    color['text'] = 'Фиолетовый'
    code.delete(0, END)
    code.insert(0, '#7d00ff')


def set_red():
    color['text'] = 'Красный'
    code.delete(0, END)
    code.insert(0, '#ff0000')


def set_green():
    color['text'] = 'Зеленый'
    code.delete(0, END)
    code.insert(0, '#00ff00')


def set_blue():
    color['text'] = 'Голубой'
    code.delete(0, END)
    code.insert(0, '#007dff')


def set_dark_blue():
    color['text'] = 'Синий'
    code.delete(0, END)
    code.insert(0, '#0000ff')


def set_orange():
    color['text'] = 'Оранжевый'
    code.delete(0, END)
    code.insert(0, '#ff7d00')


def set_yellow():
    color['text'] = 'Желтый'
    code.delete(0, END)
    code.insert(0, '#ffff00')

# highlightbackground - параметр, чтобы Button на Mac могла покрасится в указанный цвет.
# Идентичная ей функция - это bg.
# command - параметр, который принимает функцию. Работает только в 'Button', 'Radiobutton', 'Checkbutton'.


purple = Button(root, highlightbackground='#7d00ff', width=20, height=2, command=set_purple).pack(side=BOTTOM)
dark_blue = Button(root, highlightbackground='#0000ff', width=20, height=2, command=set_dark_blue).pack(side=BOTTOM)
blue = Button(root, highlightbackground='#007dff', width=20, height=2, command=set_blue).pack(side=BOTTOM)
green = Button(root, highlightbackground='#00ff00', width=20, height=2, command=set_green).pack(side=BOTTOM)
yellow = Button(root, highlightbackground='#ffff00', width=20, height=2, command=set_yellow).pack(side=BOTTOM)
orange = Button(root, highlightbackground='#ff7d00', width=20, height=2, command=set_orange).pack(side=BOTTOM)
red = Button(root, highlightbackground='#ff0000', width=20, height=2, command=set_red).pack(side=BOTTOM)


color.pack()

# justify - параметр, который выравнивает элемент.

code.config(justify=CENTER)
code.pack()

# resizable - это функция, которая дает(или не дает) право на изменение размера по оси X и Y.

root.resizable(False, False)

root.mainloop()
