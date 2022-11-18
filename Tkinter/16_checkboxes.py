from tkinter import *

root = Tk()
root.title("Animal World")
root.iconbitmap("images/title/A.ico")
root.geometry('400x400')


def show_boxes():
    label = Label(root, text=var.get())
    label.pack()


var = IntVar()
checkboxes = Checkbutton(root, text="Check me, I'm a box.", variable=var, command=show_boxes)
checkboxes.pack()


def show_food():
    label = Label(root, text=food_var.get())
    label.pack()


food_var = StringVar()
checkboxes_food = Checkbutton(root, text="Check me, I'm a food container.", variable=food_var, onvalue='pizza',
                              offvalue='burger', command=show_food)
checkboxes_food.deselect()
checkboxes_food.pack()

root.mainloop()
