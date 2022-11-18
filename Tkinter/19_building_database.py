import sqlite3
from tkinter import *

root = Tk()
root.title("Animal World")
root.iconbitmap("images/title/A.ico")
root.geometry('400x400')


def create_entry(entry_name, row, column=1):
    entry_name = Entry(root, width=30)
    entry_name.grid(row=row, column=column)
    entry.append(entry_name)


def create_text_entry(text_name, row, column=0):
    text_name = Label(root, text=text_name)
    text_name.grid(row=row, column=column)


def submit(entry, entry_list):
    entry_dict = {}
    for i, item in enumerate(entry):
        entry_dict[entry_list[i]] = item.get()
        item.delete(0, END)
    conn = sqlite3.connect("animal_database.db")
    c = conn.cursor()
    c.execute("INSERT INTO addresses "
              "VALUES (:first_name, :last_name, :city, :state, :zipcode);",
              entry_dict)
    conn.commit()
    conn.close()


def record():
    conn = sqlite3.connect("animal_database.db")
    c = conn.cursor()
    c.execute("SELECT *, oid FROM addresses")

    record = c.fetchall()
    record_str = ""
    for i in record:
        record_str += str(i) + "\n"

    record_label = Label(root, text=record_str)
    record_label.grid(row=10, column=0, columnspan=11, ipadx=100)

    conn.commit()
    conn.close()


def delete():
    conn = sqlite3.connect("animal_database.db")
    c = conn.cursor()
    c.execute("DELETE FROM addresses WHERE oid = " + delete_entry.get())

    conn.commit()
    conn.close()


entry_list = ["first_name", "last_name", "city", "state", "zipcode"]
entry = []
for i, item in enumerate(entry_list):
    create_entry(item, row=i)
    create_text_entry(item, row=i)

submit_button = Button(root, text="Add record to Database", command=lambda: submit(entry, entry_list))
submit_button.grid(row=6, column=0, columnspan=11, ipadx=100)

record_button = Button(root, text="Show Record", command=record)
record_button.grid(row=7, column=0, columnspan=11, ipadx=100)

delete_label = Label(root, text="Delete ID: ", pady=10)
delete_label.grid(row=8, column=0)

delete_entry = Entry(root, width=30)
delete_entry.grid(row=8, column=1)

delete_button = Button(root, text="Delete Record", command=delete)
delete_button.grid(row=9, column=0, columnspan=11, ipadx=100)

root.mainloop()
