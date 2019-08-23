from tkinter import *

products = ['apple', 'bananas', 'carrot', 'bread', 'butter', 'meat', 'potato', 'pineapple', 'tomato', 'milk']

root = Tk()

btn_frame = Frame(root)

# Listbox - это список чего-то.
# selectmode=EXTENDED - позволяет в списке выбирать несколько элементов(с помощью зажатой клавиши Ctrl).

shop = Listbox(width=20, height=10, selectmode=EXTENDED)

for product in products:
    shop.insert(END, product)  # Кдаем в конец списка продукты.


def to_man():
    selected_products = list(shop.curselection())  # Получаем список элементов, которые в данный момент выбраны.
    #  Далее идет просто реализация удаления из данного списка, и добавление в другой 'Listbox'.
    b = shop.get(0, END)
    selected_products.reverse()
    for product_id in selected_products:
        a = b[product_id]
        shop.delete(product_id)
        man.insert(0, a)


def to_shop():
    # В этой функции все тоже самое, что и в прошлой, но перекидываение из другого 'Listbox'.
    selected_products = list(man.curselection())
    b = man.get(0, END)
    selected_products.reverse()
    for product_id in selected_products:
        a = b[product_id]
        man.delete(product_id)
        shop.insert(0, a)


man = Listbox(width=20, height=10, selectmode=EXTENDED)
shop_to_man = Button(btn_frame, text=" >>> ", command=to_man)
man_to_shop = Button(btn_frame, text=" <<< ", command=to_shop)

shop.pack(side=LEFT)

btn_frame.pack(side=LEFT)

shop_to_man.pack(side=TOP)
man_to_shop.pack(side=BOTTOM)

man.pack()

root.mainloop()
