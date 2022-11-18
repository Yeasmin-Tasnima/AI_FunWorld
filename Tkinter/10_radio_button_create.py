from tkinter import *

root = Tk()
root.title("Elephant")
root.iconbitmap("title_images/elephant_3.ico")


def click_button(value):
    label = Label(root, text="The clicked value is " + str(value))
    label.pack(padx=2, pady=2)


rb = IntVar()

Radiobutton(root, text='I am a new radio button!!', variable=rb, value="1",
            command=lambda: click_button(rb.get())).pack()
Radiobutton(root, text='I am another radio button!!', variable=rb, value="2",
            command=lambda: click_button(rb.get())).pack()
Radiobutton(root, text='I am also a radio button!! Click to test me.', variable=rb, value="3",
            command=lambda: click_button(rb.get())).pack()

root.mainloop()
