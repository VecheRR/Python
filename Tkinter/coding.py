from tkinter import *

root = Tk()

def foo():
    n = int(inp.get())
    output['text'] = "{0:x}".format(n)


def moo():
    n = int(inp.get())
    output['text'] = "{0:o}".format(n)


def boo():
    n = int(inp.get())
    output['text'] = "{0:b}".format(n)


root.title("Coding")
root.geometry("350x175+100+100")

inp = Entry(root, width=20, text='10')
inp.place(x=20, y=20)

r_var = IntVar()
r_var.set(0)

Radiobutton(root, text='16', variable=r_var, value=0, command=foo).place(x=238, y=20)
Radiobutton(root, text='8', variable=r_var, value=1, command=moo).place(x=238, y=50)
Radiobutton(root, text='2', variable=r_var, value=2, command=boo).place(x=238, y=80)

output = Label(root, width=20, bg='lightgreen')
inp.insert(0, '10')
output['text'] = 'a'
output.place(x=20, y=120)

root.mainloop()
