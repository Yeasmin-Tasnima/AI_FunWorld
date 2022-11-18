from tkinter import *

root = Tk()
root.title("Elephant")
root.iconbitmap('title_images/elephant_3.ico')

frame1 = LabelFrame(root, text='Elephant things!!', padx=50, pady=50)
frame1.pack(padx=10, pady=10)

frame2 = LabelFrame(root, padx=50, pady=200)
frame2.pack(padx=10, pady=10)

button1 = Button(frame1, text="Click me!", fg='white', bg='blue')
button2 = Button(frame1, text="Click me too!", fg='blue', bg='yellow')

button1.grid(row=1, column=0)
button2.grid(row=2, column=1)

label1 = Label(frame1, text="I am a frame with a title !!", bd=1, relief=SUNKEN, fg='white', bg='green')
label2 = Label(frame2, text="I am a frame without a title !!", bd=1, relief=SUNKEN, fg='white', bg='green')

label1.grid(row=0, column=0, pady=20)
label2.pack()

root.mainloop()
