from tkinter import *

root = Tk()

c = Canvas(width=600, height=600, bg='white')
c.pack()

ball = c.create_oval(0, 100, 40, 140, fill='red')


def click(event):
    x = event.x
    y = event.y

    def motion_x():
        if c.coords(ball)[2] > x + 16:
            c.move(ball, -1, 0)
            root.after(10, motion_x)  # Через 10 милисекунд запустится функция.
        elif c.coords(ball)[2] < x + 16:
            c.move(ball, 1, 0)
            root.after(10, motion_x)

    def motion_y():
        if c.coords(ball)[3] > y + 16:
            c.move(ball, 0, -1)
            root.after(10, motion_y)
        elif c.coords(ball)[3] < y + 16:
            c.move(ball, 0, 1)
            root.after(10, motion_y)

    motion_x()
    motion_y()


root.bind('<Button-1>', click)

root.mainloop()
