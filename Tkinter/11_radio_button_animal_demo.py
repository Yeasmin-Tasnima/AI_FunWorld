from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Animal")
root.iconbitmap("images/title/A.ico")


def click_radio_button(text, animal_image):
    img = ImageTk.PhotoImage(Image.open(animal_image).resize((500, 500)))
    image_label.config(text=text, image=img)
    image_label.text = text
    image_label.image = img


animal_images = [
    ('elephant', 'images/animal/elephant/elephant_1.png'),
    ('cat', 'images/animal/cat.png'),
    ('tiger', 'images/animal/tiger.png'),
    ('lion', 'images/animal/lion.jpg'),
    ('cow', 'images/animal/cow.jpg')
]

animal = StringVar()
animal.set(' ')

for animal_name, image in animal_images:
    text = 'I am ' + animal_name

    animal_button = Radiobutton(root, text=animal_name, variable=animal, value=image,
                                command=lambda: click_radio_button(text, animal.get()))
    animal_button.pack()

image_label = Label(root, text='Animals', compound='bottom', fg='white', bg='blue')
image_label.pack(pady=10)

button_exit = Button(root, text='Exit', fg='white', bg='red', command=root.quit).pack()

root.mainloop()
