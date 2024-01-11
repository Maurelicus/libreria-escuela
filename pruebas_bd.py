import tkinter as tki
from tkinter import ttk
import sqlite3

bd = sqlite3.connect("base_de_dato3.db")
cursor = bd.cursor()
query = "SELECT * FROM bienes_culturales"
cursor.execute(query)
l_filas = cursor.fetchall()
print(l_filas[3])
# print(l_filas[199])

root = tki.Tk()
root.tk.call("source", "forest-light.tcl")
root.tk.call("source", "forest-dark.tcl")

frame = ttk.Frame(root,)
frame.pack()

root.mainloop()