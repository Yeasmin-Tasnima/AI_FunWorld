from tkinter import *

root = Tk()

myButton1 = Button(root, text="I'm a new button, Click me!")
myButton1.pack()

myButton2 = Button(root, text="Disables button", state=DISABLED)
myButton2.pack()

myButton3 = Button(root, text="padded button by x", padx=50)
myButton3.pack()

myButton4 = Button(root, text="padded button by y", pady=50)
myButton4.pack()

myButton5 = Button(root, text="padded button by x and y", padx=50, pady=25)
myButton5.pack()


def myButton1_click():
    myLabel1 = Label(root, text="Hey, I clicked the functional button!")
    myLabel1.pack()


myButton1 = Button(root, text="I'm a functional button, Click me!", command=myButton1_click, fg="white", bg="black")
myButton1.pack()

root.mainloop()
