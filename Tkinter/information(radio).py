from tkinter import *

root = Tk()


def Vasya():
    number['text'] = "+7-928-466-12-35"


def Petya():
    number['text'] = "+7-928-467-29-64"


def Masha():
    number['text'] = "+7-928-668-77-51"


# Для того, чтобы создать 'Radiobutton', нужно создать переменную, которая хранит номер нажатой в данный момент кнопки.


rb_var = IntVar()  # Вот она.
rb_var.set(0)  # По умолчанию стоит 0-ой элемент.

radio_frame = Frame(root)
number_frame = Frame(root)

radio_frame.pack(side=LEFT)
number_frame.pack(side=RIGHT)

# indicatoron делает из 'Radiobutton' обычную кнопку, но со своими старыми свойствами 'Radiobutton'.

rb1 = Radiobutton(radio_frame, indicatoron=0, width=15, height=3, text="Вася", variable=rb_var, value=0, command=Vasya)
rb2 = Radiobutton(radio_frame, indicatoron=0, width=15, height=3, text="Петя", variable=rb_var, value=1, command=Petya)
rb3 = Radiobutton(radio_frame, indicatoron=0, width=15, height=3, text="Маша", variable=rb_var, value=2, command=Masha)
number = Label(number_frame, width=35, height=9, text="+7-928-466-12-35")

rb1.pack()
rb2.pack()
rb3.pack()
number.pack()

root.mainloop()