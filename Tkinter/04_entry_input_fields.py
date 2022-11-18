from tkinter import *

root = Tk()

e = Entry(root, width=50, borderwidth=10, fg="white", bg="black")
e.pack()
e.insert(0, "Enter your name.")


def myButton1_click():
    hello = "Hello! My name is " + e.get()
    myLabel1 = Label(root, text=hello)
    myLabel1.pack()


myButton1 = Button(root, text="Enter your name.", command=myButton1_click)
myButton1.pack()

root.mainloop()
