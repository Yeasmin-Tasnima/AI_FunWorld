from tkinter import *

root = Tk()
root.title("Animal World")
root.iconbitmap("images/title/A.ico")
root.geometry('400x400')


def slide(var):
    label = Label(root, text=vertical_slider.get())
    label.pack()


vertical_slider = Scale(root, from_=0, to=400, command=slide)
vertical_slider.pack()

horizontal_slider = Scale(root, from_=0, to=400, orient=HORIZONTAL)
horizontal_slider.pack()

root.mainloop()
