from tkinter import *


class Calc:  # Создаем класс для калькулятора
    def __init__(self, master):
        self.num1 = Entry(master, width=20)  # Entry - это однострочное текстовое поле.
        self.num2 = Entry(master, width=20)
        self.plus = Button(master, width=10, text='+')  # Button - это обычная кнопка.
        self.minus = Button(master, width=10, text='-')
        self.mult = Button(master, width=10, text='*')
        self.div = Button(master, width=10, text="/")
        self.answer = Label(master, width=20)  # Label - это поле, в котором можно что-либо показывать.

        self.plus['command'] = eval('self.' + 'func_plus')  # Eval - функция, которая переводит передаваемые данные(string) в код tcl.
        self.minus['command'] = eval('self.' + 'func_minus')
        self.mult['command'] = eval('self.' + 'func_mult')
        self.div['command'] = eval('self.' + 'func_div')

        self.num1.pack()  # По умолчанию pack, пакует элементы с side=TOP.
        self.num2.pack()  # Если так и нужно, то можно side=TOP не писать.
        self.plus.pack()
        self.minus.pack()  # Так пакуем все элементы в нужном нам порядке.
        self.mult.pack()
        self.div.pack()
        self.answer.pack()

    # Далее создаем функции(сложения, вычитания, умножения и деления).
    def func_plus(self):
        try:  # Проверка на правильность введенных данных.
            a = float(self.num1.get())  # С помощью функции get, мы получаем данные в этом поле.
            b = float(self.num2.get())
            self.answer['text'] = str(a + b)  # У каждого элемента в Tkinter есть свойства. Их можно изменять, например так.
        except:
            self.answer['text'] = "ERROR! Input only INT or FLOAT numbers, please."

    def func_minus(self):
        try:
            a = float(self.num1.get())
            b = float(self.num2.get())
            self.answer['text'] = str(a - b)
        except:
            self.answer['text'] = "ERROR! Input only INT or FLOAT numbers, please."

    def func_mult(self):
        try:
            a = float(self.num1.get())
            b = float(self.num2.get())
            self.answer['text'] = str(a * b)
        except:
            self.answer['text'] = "ERROR! Input only INT or FLOAT numbers, please."

    def func_div(self):
        try:
            a = float(self.num1.get())
            b = float(self.num2.get())
            self.answer['text'] = str(a / b)
        except:
            self.answer['text'] = "ERROR! Input only INT or FLOAT numbers, please."


root = Tk()  # Создаем главное поле(обычно его называют root). И оно принадлежит классу Tk.

calculator = Calc(root)

root.geometry("400x175+300+300")  # Устанавливаем размер и расположение на экране нашего окна.

root.mainloop()  # Запускаем главный цикл, чтобы программа запустилась.
