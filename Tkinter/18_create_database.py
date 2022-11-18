import sqlite3
from tkinter import *

root = Tk()
root.title("Animal World")
root.iconbitmap("images/title/A.ico")
root.geometry('400x400')

conn = sqlite3.connect("animal_database.db")
c = conn.cursor()

c.execute("""CREATE TABLE addresses (
          first_name text,
          last_name text,
          city text,
          state text,
          zipcode integer)
          """)

conn.commit()

conn.close()

root.mainloop()
