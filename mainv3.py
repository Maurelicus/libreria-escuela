# from tkinter import ttk
import tkinter as tk
import ttkbootstrap as ttk

from ventanav4principal import Ventana



if __name__ == "__main__":
    """ 
    # root.destroy()
    app = Ventana()
    app.title('Biblioteca Colegio')
    app.minsize(width=1200, height=650)
    # 1440x900
    app.geometry('1000x600')
    app.columnconfigure(0, weight=1)
    app.rowconfigure(0, weight=1)
    app.mainloop()
    """
    ven_pri = ttk.Window(themename='superhero')
    ven_pri.title('Biblioteca Colegio')
    ven_pri.minsize(width=1200, height=650)
    # 1440x900
    ven_pri.geometry('1000x600')
    ven_pri.columnconfigure(0, weight=1)
    ven_pri.rowconfigure(0, weight=1)
    app = Ventana(ven_pri)
    app.mainloop()
""" 
def ingresar():
root = ttk.Window(themename= 'darkly')
root.geometry('600x400')
root.title('prueba')

button1 = ttk.Button(root, text='ingresar', command = ingresar)
button1.pack(expand=True)

root.mainloop()
"""
