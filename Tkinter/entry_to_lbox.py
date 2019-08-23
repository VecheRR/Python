from tkinter import *

root = Tk()


# Кода идет дело с bind'ами, то в функции, которая передается bind'у должна иметь в себе параметр - event(это обязательно!).


def to_lbox(event):
    lbox.insert(END, entry.get())
    entry.delete(0, END)


def to_entry(event):
    entry.delete(0, END)
    entry.insert(0, lbox.get(lbox.curselection()))
    lbox.delete(lbox.curselection())


entry = Entry(root)
lbox = Listbox(root)

# bind - полезная вещь, которая позволяет легко сделать бинд на что-то.
# Сначала передается название кнопки, а потом функция.


entry.bind('<Return>', to_lbox)
lbox.bind('<Double-Button-1>', to_entry)

entry.pack(side=LEFT)
lbox.pack(side=LEFT)

root.mainloop()

# Напишите программу по следующему описанию.
# Нажатие Enter в однострочном текстовом поле приводит
# к перемещению текста из него в список (экземпляр Listbox).
# При двойном клике (<Double-Button-1>) по элементу-строке списка,
# она должна копироваться в текстовое поле.
