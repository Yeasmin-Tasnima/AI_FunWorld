from tkinter import *

root = Tk()
root.title("Animal World")
root.iconbitmap("images/title/A.ico")
root.geometry('400x400')

list_option = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

clicked = StringVar()
clicked.set(list_option[0])

dropdown = OptionMenu(root, clicked, *list_option)
dropdown.pack()

root.mainloop()
