from tkinter import *

root = Tk()

def summa():
    # output['text'] = "{0:b}".format(n)
    f = r_var.get()
    if f == 0:
        base = 16
    elif f == 1:
        base = 8
    else:
        base = 2
    num1 = int(inp1.get(), base)
    num2 = int(inp2.get(), base)
    sm_10 = num1 + num2
    sm_10 = sm_10
    if base == 16:
        sm_base = "{0:x}".format(sm_10)
    elif base == 8:
        sm_base = "{0:o}".format(sm_10)
    else:
        sm_base = "{0:b}".format(sm_10)

    output['text'] = str(sm_base)


root.title("Coding")
root.geometry("400x175+100+100")

inp1 = Entry(root, width=20)
inp2 = Entry(root, width=20)
inp1.place(x=20, y=20)
inp2.place(x=20, y=60)

r_var = IntVar()
r_var.set(0)

Radiobutton(root, text='16-я система', variable=r_var, value=0).place(x=238, y=20)
Radiobutton(root, text='8-я система', variable=r_var, value=1).place(x=238, y=50)
Radiobutton(root, text='2-я система', variable=r_var, value=2).place(x=238, y=80)

Button(root, text='Сложить', command=summa).place(x=238, y=120)

output = Label(root, width=20, bg='lightgreen')

output['text'] = 'a'
output.place(x=20, y=120)

root.mainloop()
