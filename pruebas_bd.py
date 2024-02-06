from conexion_sqlite import Comunicacion
from datetime import date, datetime
from tkinter import messagebox
from tkinter import ttk
import mainv3 as mv3
import csv

bd = Comunicacion()



root = ttk.Tk()
root.geometry('600x400')
root.title('prueba')

button1 = ttk.Button(root, text='ingresar')

root.mainloop()

def ingresar():
    return