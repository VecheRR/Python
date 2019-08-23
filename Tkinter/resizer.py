from tkinter import *

root = Tk()

# screen_width = root.winfo_reqwidth()
# screen_height = root.winfo_reqheight()
# print(str(screen_width) + 'x' + str(screen_height))

main_frame = Frame(root)
f1 = Frame(main_frame)  # entries
f2 = Frame(main_frame)  # button
f3 = Frame(main_frame)  # text

e1 = Entry(f1, width=2)
e2 = Entry(f1, width=2)
btn = Button(f2, text='Change')
text = Text(f3, bg='lightgrey')
text.bind('<FocusIn>', lambda event, color="white": text.config(bg=color))
text.bind('<FocusOut>', lambda event, color="lightgrey": text.config(bg=color))

main_frame.pack()

f1.pack(anchor=S)
f2.pack(anchor=S)
f3.pack(anchor=W)

e1.pack()
e2.pack()
btn.pack()
text.pack()

root.bind('Control-q', lambda event: root.destroy())
btn.bind('<Button-1>', lambda event: text.config(width=e1.get(), height=int(e2.get())))
btn.bind('<Return>', lambda event: text.config(width=e1.get(), height=int(e2.get())))

root.mainloop()