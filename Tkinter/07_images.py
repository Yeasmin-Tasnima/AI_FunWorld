from tkinter import *
from PIL import ImageTk, Image
import glob

root = Tk()

root.title("Elephant")
root.iconbitmap("images/title/elephant_3.ico")


def forward(image_number):
    global img_label
    global button_forward
    global button_backward

    if image_number == len(image_list) - 1:
        img_label.grid_forget()

        img_label = Label(image=image_list[image_number])
        button_forward = Button(root, text=">>", fg='white', bg='blue', state=DISABLED)
    else:
        img_label.grid_forget()

        img_label = Label(image=image_list[image_number])
        button_forward = Button(root, text=">>", fg='white', bg='blue',
                                command=lambda: forward(image_number + 1))

    button_backward = Button(root, text="<<", fg='white', bg='blue', command=lambda: backward(image_number))
    img_label.grid(row=0, column=0, columnspan=3)
    button_forward.grid(row=1, column=2)
    button_backward.grid(row=1, column=0)


def backward(image_number):
    global img_label
    global button_forward
    global button_backward

    if image_number == 1:
        img_label.grid_forget()

        img_label = Label(image=image_list[image_number - 1])
        button_backward = Button(root, text="<<", fg='white', bg='blue', state=DISABLED)
    else:
        img_label.grid_forget()

        img_label = Label(image=image_list[image_number - 1])
        button_backward = Button(root, text="<<", fg='white', bg='blue',
                                 command=lambda: backward(image_number - 1))

    button_forward = Button(root, text=">>", fg='white', bg='blue', command=lambda: forward(image_number))
    img_label.grid(row=0, column=0, columnspan=3)
    button_forward.grid(row=1, column=2)
    button_backward.grid(row=1, column=0)


img_list = glob.glob('images/animal/elephant/*')
image_list = []
for i in img_list:
    image_list.append(ImageTk.PhotoImage(Image.open(i).resize((500, 500))))

img_label = Label(image=image_list[0])
img_label.grid(row=0, column=0, columnspan=3)

button_backward = Button(root, text="<<", fg='white', bg='blue',
                         command=lambda: backward(1), state=DISABLED)
button_quit = Button(root, text="Exit", fg='white', bg='red', command=root.quit)
button_forward = Button(root, text=">>", fg='white', bg='blue', command=lambda: forward(1))

button_backward.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

root.mainloop()
