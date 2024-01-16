import tkinter as tk
from tkinter import ttk

import ventana1 as ven1
import ventana2 as ven2

class Ventana(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.v1 = ven1.Widgets1v()
        self.v2 = ven2.Widgets2v()
        self.mytabcontrol = ttk.Notebook(self)
        self.mytab1 = ttk.LabelFrame(self.mytabcontrol, text='Libros')
        self.mytab1.columnconfigure(0, weight=1, minsize=440)
        self.mytab1.columnconfigure(1, weight=1)
        self.mytab1.rowconfigure(0, weight=1)
        self.mytab2 = ttk.LabelFrame(self.mytabcontrol, text='Laminas') 
        self.mytab2.columnconfigure(0, weight=1, minsize=440)
        self.mytab2.columnconfigure(1, weight=1)
        self.mytab2.rowconfigure(0, weight=1)
        
        self.mytabcontrol.add(self.mytab1, text ='Libros')
        self.mytabcontrol.add(self.mytab2, text ='Laminas')
        self.mytabcontrol.grid(column=0, row=0,padx=10, pady=10, sticky='nswe')
        
        self.widgets()
        
    def widgets(self):
        #! Funciones label
        
        frame_uno = ttk.LabelFrame(self.mytab1, text='Funciones')
        frame_uno.grid(column=0, row=0, padx=5, pady=5, sticky='n')
        frame_uno.columnconfigure(0, weight=1)
        frame_uno.rowconfigure(0, weight=1)
        
        frame_dos = ttk.LabelFrame(self.mytab1, text='Visualizacion')
        frame_dos.grid(column=1, row=0, sticky='nsew')
        frame_dos.columnconfigure(0, weight=1)
        frame_dos.rowconfigure(0, weight=0)
        frame_dos.rowconfigure(1, weight=10)
        
        frame_tres = ttk.LabelFrame(self.mytab2, text='Funciones')
        frame_tres.grid(column=0, row=0, padx=5, pady=5, sticky='n')
        frame_tres.columnconfigure(0, weight=1)
        frame_tres.rowconfigure(0, weight=1)
        
        frame_cuatro = ttk.LabelFrame(self.mytab2, text='Visualizacion')
        frame_cuatro.grid(column=1, row=0, sticky='nsew')
        frame_cuatro.columnconfigure(0, weight=1)
        frame_cuatro.rowconfigure(0, weight=0)
        frame_cuatro.rowconfigure(1, weight=10)
        
        self.v1.widgets(frame_uno, frame_dos)
        self.v2.widgets(frame_tres, frame_cuatro)
        