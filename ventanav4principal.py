import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

import ventana1 as ven1
import ventana2 as ven2
import ventana3 as ven3
import ventana4 as ven4

class Ventana(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        self.v1 = ven1.Widgets1v()
        self.v2 = ven2.Widgets2v()
        self.v3 = ven3.Widgets3v()
        self.v4 = ven4.Widgets4v()
        self.mytabcontrol = ttk.Notebook(self.master)
        self.mytab1 = ttk.Frame(self.mytabcontrol)
        self.mytab1.columnconfigure(0, weight=1, minsize=340)
        self.mytab1.columnconfigure(1, weight=1)
        self.mytab1.rowconfigure(0, weight=1)
        self.mytab2 = ttk.Frame(self.mytabcontrol) 
        self.mytab2.columnconfigure(0, weight=1, minsize=340)
        self.mytab2.columnconfigure(1, weight=1)
        self.mytab2.rowconfigure(0, weight=1)
        self.mytab3 = ttk.Frame(self.mytabcontrol) 
        self.mytab3.columnconfigure(0, weight=1, minsize=340)
        self.mytab3.columnconfigure(1, weight=1)
        self.mytab3.rowconfigure(0, weight=1)
        self.mytab4 = ttk.Frame(self.mytabcontrol)
        self.mytab4.columnconfigure(0, weight=1, minsize=330)
        self.mytab4.columnconfigure(1, weight=1)
        self.mytab4.rowconfigure(0, weight=1)
        self.mytab5.columnconfigure(0, weight=1, minsize=330)
        self.mytab5.columnconfigure(1, weight=1)
        self.mytab5.rowconfigure(0, weight=1)
        
        
        self.mytabcontrol.add(self.mytab1, text ='Libros')
        self.mytabcontrol.add(self.mytab2, text ='Laminas')
        self.mytabcontrol.add(self.mytab3, text ='Pedidos')
        self.mytabcontrol.add(self.mytab4, text ='Devoluciones')
        self.mytabcontrol.add(self.mytab5, text ='Baja')
        self.mytabcontrol.grid(column=0, row=0, padx=10, pady=10, sticky='nswe')
        
        self.widgets()
        
    def widgets(self):
        #! Funciones label
        frame_uno = ttk.LabelFrame(self.mytab1, text='Funciones')
        frame_uno.grid(column=0, row=0, padx=5, pady=5, sticky='nswe')
        frame_uno.columnconfigure(0, weight=1)
        
        frame_dos = ttk.LabelFrame(self.mytab1, text='Visualizacion')
        frame_dos.grid(column=1, row=0, padx=5, pady=5, sticky='nsew')
        frame_dos.columnconfigure(0, weight=1)
        frame_dos.rowconfigure(0, weight=0)
        frame_dos.rowconfigure(1, weight=10)
        
        frame_tres = ttk.LabelFrame(self.mytab2, text='Funciones')
        frame_tres.grid(column=0, row=0, padx=5, pady=5, sticky='nsew')
        frame_tres.columnconfigure(0, weight=1)
        
        frame_cuatro = ttk.LabelFrame(self.mytab2, text='Visualizacion')
        frame_cuatro.grid(column=1, row=0, padx=5, pady=5, sticky='nsew')
        frame_cuatro.columnconfigure(0, weight=1)
        frame_cuatro.rowconfigure(0, weight=0)
        frame_cuatro.rowconfigure(1, weight=10)
        
        frame_cinco = ttk.LabelFrame(self.mytab3, text='Funciones')
        frame_cinco.grid(column=0, row=0, padx=5, pady=5, sticky='nswe')
        frame_cinco.columnconfigure(0, weight=1, minsize=159)
        frame_cinco.columnconfigure(1, weight=1, minsize=181)
        
        frame_seis = ttk.LabelFrame(self.mytab3, text='Visualizacion')
        frame_seis.grid(column=1, row=0, padx=5, pady=5, sticky='nsew')
        frame_seis.columnconfigure(0, weight=1)
        frame_seis.rowconfigure(0, weight=0)
        frame_seis.rowconfigure(1, weight=10)
        frame_seis.rowconfigure(2, weight=0)
        frame_seis.rowconfigure(3, weight=10)
        
        frame_siete = ttk.LabelFrame(self.mytab4, text='Funciones')
        frame_siete.grid(column=0, row=0, padx=5, pady=5, sticky='nswe')
        frame_siete.columnconfigure(0, weight=1, minsize=165)
        frame_siete.columnconfigure(1, weight=1, minsize=125)
        
        frame_ocho = ttk.LabelFrame(self.mytab4, text='Visualizacion')
        frame_ocho.grid(column=1, row=0, padx=5, pady=5, sticky='nsew')
        frame_ocho.columnconfigure(0, weight=1)
        frame_ocho.rowconfigure(0, weight=0)
        frame_ocho.rowconfigure(1, weight=10)

        self.v1.seccion_uno(frame_uno)
        self.v1.seccion_dos(frame_dos)
        self.v2.seccion_uno(frame_tres)
        self.v2.seccion_dos(frame_cuatro)
        self.v3.seccion_uno(frame_cinco)
        self.v3.seccion_dos(frame_seis)
        self.v4.seccion_uno(frame_siete)
        self.v4.seccion_dos(frame_ocho)
        