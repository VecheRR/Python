from tkinter import *

root = Tk()

color = Label(root)
code = Entry(root)
frame = Frame(root)


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


color.pack(side=TOP)

code.config(justify=CENTER)
code.pack(side=TOP)

frame.pack()

# padx - параметр, указываюшийся, когда элемент вставляется в окно. Он делает отступы от элемента по горизонтали на указанный промежуток(в пикселях).
# pady - он делает отступы от элемента по вертикали на указанный промежуток(в пикселях).
# ipadx - он делает отступы внутри элемента по горизонтали на указанный промежуток(в пикселях).
# ipady - он делает отступы внутри элемента по вертикали на указанный промежуток(в пикселях).

purple = Button(frame, highlightbackground='#7d00ff', width=4, height=2, command=set_purple).pack(side=RIGHT, padx=4, pady=4)
dark_blue = Button(frame, highlightbackground='#0000ff', width=4, height=2, command=set_dark_blue).pack(side=RIGHT, padx=4, pady=4)
blue = Button(frame, highlightbackground='#007dff', width=4, height=2, command=set_blue).pack(side=RIGHT, padx=4, pady=4)
green = Button(frame, highlightbackground='#00ff00', width=4, height=2, command=set_green).pack(side=RIGHT, padx=4, pady=4)
yellow = Button(frame, highlightbackground='#ffff00', width=4, height=2, command=set_yellow).pack(side=RIGHT, padx=4, pady=4)
orange = Button(frame, highlightbackground='#ff7d00', width=4, height=2, command=set_orange).pack(side=RIGHT, padx=4, pady=4)
red = Button(frame, highlightbackground='#ff0000', width=4, height=2, command=set_red).pack(side=RIGHT, padx=4, pady=4)

root.resizable(False, False)

root.mainloop()