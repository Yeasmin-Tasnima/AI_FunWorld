from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=10, padx=10, pady=10)


def button_click(number):
    e.insert(END, number)


def button_equal_func():
    total_str = e.get()
    e.delete(0, END)
    e.insert(0, str(eval(total_str)))


def button_clear_func():
    e.delete(0, END)


button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_addition = Button(root, text="+", padx=40, pady=20, command=lambda: button_click('+'))
button_subtraction = Button(root, text="-", padx=40, pady=20, command=lambda: button_click('-'))
button_multiplication = Button(root, text="*", padx=40, pady=20, command=lambda: button_click('*'))
button_division = Button(root, text="/", padx=40, pady=20, command=lambda: button_click('/'))
button_equal = Button(root, text="=", padx=40, pady=20, command=button_equal_func)
button_clear = Button(root, text="C", padx=40, pady=20, command=button_clear_func)

button_clear.grid(row=4, column=0)
button_0.grid(row=4, column=1)
button_equal.grid(row=4, column=2)
button_addition.grid(row=4, column=3)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_subtraction.grid(row=3, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_multiplication.grid(row=2, column=3)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_division.grid(row=1, column=3)

root.mainloop()
