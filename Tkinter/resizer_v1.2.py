from tkinter import *

root = Tk()

main_frame = Frame(root)
f1_2 = Frame(main_frame)
f1 = Frame(f1_2)  # entries
f2 = Frame(f1_2)  # button
f3 = Frame(main_frame)  # text

e1 = Entry(f1, width=2)
e2 = Entry(f1, width=2)
btn = Button(f2, text='Change')
text = Text(f3, bg='lightgrey')
text.bind('<FocusIn>', lambda event, color="white": text.config(bg=color))
text.bind('<FocusOut>', lambda event, color="lightgrey": text.config(bg=color))

main_frame.pack()
f1_2.pack(side=TOP)
f3.pack(side=BOTTOM)
f1.pack(side=LEFT)
f2.pack(side=LEFT)

e1.pack()
e2.pack()
btn.pack()
text.pack()

btn.bind('<Button-1>', lambda event: text.config(width=e1.get(), height=e2.get()))
btn.bind('<Return>', lambda event: text.config(width=e1.get(), height=e2.get()))

root.mainloop()