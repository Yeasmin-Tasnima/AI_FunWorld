from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

root = Tk()
root.title("Animal World")
root.iconbitmap("images/title/A.ico")


def file_open():
    global img_pil
    img_file = filedialog.askopenfilename(initialdir='images/', title='Select A File',
                                          filetypes=(('png_files', '*.png'),
                                                     ('jpg_files', '*.jpg'),
                                                     ('all_files', '*.*')))
    img_pil = ImageTk.PhotoImage(Image.open(img_file).resize((500, 500)))
    label_img = Label(root, text="This is an Image", image=img_pil, bg='blue', compound='bottom')
    label_img.pack()
    button_open.pack_forget()


button_open = Button(root, text="Open an Image", fg='white', bg='blue', command=file_open)
button_open.pack(pady=10)

button_quit = Button(root, text="Quit", fg='white', bg='red', command=root.quit)
button_quit.pack()

root.mainloop()
