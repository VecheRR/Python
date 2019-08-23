# scissors, paper, stone

from tkinter import *
import random

root = Tk()


def scissors():
    enemy = random.randint(1, 3)
    total['fg'] = 'yellow' if enemy == 1 else 'green' if enemy == 2 else 'red'
    total['text'] = 'Draw\nThe enemy chose SCISSORS.' if enemy == 1 else 'You won\nThe enemy chose PAPER.' if enemy == 2 else 'You lose\nThe enemy chose STONE.'


def paper():
    enemy = random.randint(1, 3)
    total['fg'] = 'red' if enemy == 1 else 'yellow' if enemy == 2 else 'green'
    total['text'] = 'You lose\nThe enemy chose SCISSORS.' if enemy == 1 else 'Draw\nThe enemy chose PAPER.' if enemy == 2 else 'You won\nThe enemy chose STONE.'


def stone():
    enemy = random.randint(1, 3)
    total['fg'] = 'green' if enemy == 1 else 'red' if enemy == 2 else 'yellow'
    total['text'] = 'You won\nThe enemy chose SCISSORS.' if enemy == 1 else 'You lose\nThe enemy chose PAPER.' if enemy == 2 else 'Draw\nThe enemy chose STONE.'


rb_var = BooleanVar()
rb_var.set(0)

radio_frame = Frame(root)
number_frame = Frame(root)

radio_frame.pack(side=LEFT)
number_frame.pack(side=RIGHT)

rb1 = Radiobutton(radio_frame, indicatoron=0, width=15, height=3, text="Scissors", variable=rb_var, value=0, command=scissors)
rb2 = Radiobutton(radio_frame, indicatoron=0, width=15, height=3, text="Paper", variable=rb_var, value=1, command=paper)
rb3 = Radiobutton(radio_frame, indicatoron=0, width=15, height=3, text="Stone", variable=rb_var, value=2, command=stone)
total = Label(number_frame, width=35, height=9, text="Select something from this list, please.\n1) Scissors.\n2) Paper.\n3) Stone.\n", font="Times 18")

rb1.pack()
rb2.pack()
rb3.pack()
total.pack()

root.mainloop()
