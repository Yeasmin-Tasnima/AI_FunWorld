from tkinter import *

root = Tk()

my_label1 = Label(root, text="Hello World!")
my_label2 = Label(root, text="My name is Tasnim")

my_label1.grid(row=0, column=0)
my_label2.grid(row=1, column=0)

my_label3 = Label(root, text="Another text to check the unlimited row, columns")
my_label4 = Label(root, text="This is an example of unlimited column")

blank = "                    "
my_label5 = Label(root, text=blank)
my_label6 = Label(root, text=blank)

my_label5.grid(row=2, column=0)
my_label3.grid(row=3, column=0)
my_label6.grid(row=4, column=1)
my_label4.grid(row=4, column=4)

root.mainloop()