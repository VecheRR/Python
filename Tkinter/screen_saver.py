from tkinter import *
from PIL import ImageGrab, ImageTk
from save_photo_func import save_photo


def capture():
    root.iconify()
    root.after(1)
    screen = ImageGrab.grab()
    save_photo(screen)
    root.deiconify()
    if check.get() == True:
        screen.show()


root = Tk()
root.title("-_-")

check = BooleanVar()
check.set(False)

Button(root, text="Make screenshot!", command=capture).pack()
Checkbutton(root, text='Show photo', onvalue=True, variable=check, offvalue=False).pack()

# root.withdraw()
# root.deiconify()

root.mainloop()
