from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Animal")
root.iconbitmap("images/title/A.ico")


def process():
    response_ques = messagebox.askquestion("Animal World", "Are you ready to reply?")
    if response_ques == 'yes':
        response_kind = messagebox.askyesno("Animal World", "Are you kind to animals?")
        if response_kind:
            messagebox.showinfo("Animal World", "Thank you! You are very kind")
        else:
            messagebox.showinfo("Animal World", "Please be kind to animals.")
            response_person = messagebox.askyesno("Animal World", "Are you be a kind person?")
            if response_person:
                messagebox.showinfo("Animal World", "Thank you! Wishing a good future.")
            else:
                messagebox.showwarning("Animal World", "Please do not harm any animal.")
                response_point = messagebox.askyesno("Animal World", "Have you got the point?")
                if response_point:
                    messagebox.showinfo("Animal World", "Thank you for understanding")
                else:
                    messagebox.showerror("Animal World", "Oh! You are not a human being if you are cruel!")
    else:
        messagebox.showinfo("Animal World", "Okay. Have a good day.")


def popup():
    process()
    continue_task = True
    while continue_task:
        response_last = messagebox.askokcancel("Animal World", "Are you ready to try again?")
        if response_last:
            process()
        else:
            continue_task = False


button = Button(root, text="Message Alert!", fg='white', bg='blue', command=popup)
button.pack(pady=10)

button_quit = Button(root, text="Quit", fg='white', bg='red', command=root.quit)
button_quit.pack()

root.mainloop()
