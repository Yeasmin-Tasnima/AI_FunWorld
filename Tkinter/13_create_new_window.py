from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Animal World")
root.iconbitmap("images/title/A.ico")


def create_window():
    global img

    window_01 = Toplevel()
    window_01.title("Elephant")
    window_01.iconbitmap("images/title/elephant_3.ico")

    img = ImageTk.PhotoImage(Image.open("images/animal/elephant/elephant_1.png").resize((500, 500)))
    label_image = Label(window_01, text="I am an elephant", image=img, compound='bottom', fg='white', bg='blue')
    label_image.pack(pady=5)

    button_window_quit = Button(window_01, text="Exit Window", fg='white', bg='red', command=window_01.destroy)
    button_window_quit.pack()


button_window_create = Button(root, text="Create New Window", fg='white', bg='blue', command=create_window)
button_window_create.pack(pady=5)

button_quit = Button(root, text="Quit", fg='white', bg='red', command=root.quit)
button_quit.pack()

root.mainloop()
