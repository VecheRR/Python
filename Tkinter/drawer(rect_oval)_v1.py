from tkinter import *
import random
from my_colors import colors

root = Tk()

root.title('Прямовал')

c = Canvas(root, width=600, height=600, bg='lightgrey')
c.pack()


def add_figure():
    field = Toplevel()
    field.title('Ребенок')
    field.geometry('150x200+610+30')

    f1_2 = Frame(field, pady=10)
    f3_4 = Frame(field)

    f1 = Frame(f1_2)
    f2 = Frame(f3_4)
    f3 = Frame(f1_2)
    f4 = Frame(f3_4)

    l1 = Label(f1, text='x1')
    l2 = Label(f2, text='x2')
    l3 = Label(f3, text='y1')
    l4 = Label(f4, text='y2')

    e1 = Entry(f1, width=2)
    e2 = Entry(f2, width=2)
    e3 = Entry(f3, width=2)
    e4 = Entry(f4, width=2)

    f1_2.pack()
    f3_4.pack()

    f1.pack(side=LEFT)
    f2.pack(side=LEFT)
    f3.pack(side=LEFT)
    f4.pack(side=LEFT)

    l1.pack(side=LEFT)
    l2.pack(side=LEFT)
    l3.pack(side=LEFT)
    l4.pack(side=LEFT)

    e1.pack(side=LEFT)
    e2.pack(side=LEFT)
    e3.pack(side=LEFT)
    e4.pack(side=LEFT)

    r = BooleanVar()
    r.set(0)
    r1 = Radiobutton(field, text='Прямоугольник', variable=r, value=0, justify=LEFT)
    r2 = Radiobutton(field, text='Овал', variable=r, value=1, justify=LEFT)

    r1.pack()
    r2.pack()

    def func_draw():
        if r.get() == 0:
            c.create_rectangle(e1.get(), e3.get(), e2.get(), e4.get(), fill=random.choice(colors))
        elif r.get() == 1:
            c.create_oval(e1.get(), e3.get(), e2.get(), e4.get(), fill=random.choice(colors))

    Button(field, bg='grey', text='Draw figure', command=func_draw, width=30).pack(side=BOTTOM)


Button(text='Add a new figure', command=add_figure, width=67).pack(side=BOTTOM)

root.mainloop()
