from tkinter import *
import random
from my_colors import colors

root = Tk()

root.title('Прямовал')

c = Canvas(root, width=600, height=600, bg='lightgrey')
c.grid(row=0, column=0)


def add_figure():
    field = Toplevel()
    field.title('Ребенок')
    field.geometry('200x200+610+30')

    Label(field, text='x', fg='white').grid(row=0, column=0, pady=10, sticky=W)

    Label(field, text='x1').grid(row=0, column=1, pady=10, sticky=E)
    e1 = Entry(field, width=4)
    e1.grid(row=0, column=2, sticky=W)

    Label(field, text='x', fg='white').grid(row=0, column=3, pady=10)

    Label(field, text='y1').grid(row=0, column=4, pady=10, sticky=W)
    e2 = Entry(field, width=4)
    e2.grid(row=0, column=5, sticky=E)

    Label(field, text='x', fg='white').grid(row=1, column=6, pady=10, sticky=E)

    Label(field, text='x', fg='white').grid(row=1, column=0, pady=10, sticky=W)

    Label(field, text='x2').grid(row=1, column=1, pady=10, sticky=E)
    e3 = Entry(field, width=4)
    e3.grid(row=1, column=2, sticky=W)

    Label(field, text='x', fg='white').grid(row=1, column=3, pady=10)

    Label(field, text='y2').grid(row=1, column=4, pady=10, sticky=W)
    e4 = Entry(field, width=4)
    e4.grid(row=1, column=5, sticky=E)

    Label(field, text='x', fg='white').grid(row=1, column=6, pady=10, sticky=E)

    r = BooleanVar()
    r.set(0)

    r1 = Radiobutton(field, value=0, variable=r, text='Rectangle')
    r2 = Radiobutton(field, value=1, variable=r, text='Oval')

    r1.grid(row=2, column=1, columnspan=3, sticky=W, pady=5)
    r2.grid(row=3, column=1, columnspan=3, sticky=W)

    def func_draw():
        if r.get() == 0:
            c.create_rectangle(e1.get(), e2.get(), e3.get(), e4.get(), fill=random.choice(colors))
        elif r.get() == 1:
            c.create_oval(e1.get(), e2.get(), e3.get(), e4.get(), fill=random.choice(colors))

    Button(field, text='Draw figure', command=func_draw).grid(row=4, column=1, columnspan=3, pady=10)


Button(text='Add a new figure', command=add_figure).grid(row=1, column=0, columnspan=3)

root.mainloop()
