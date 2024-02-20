import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

import ventana_libros as veli
import ventana_laminas as vela
import libros_baja as vere
import laminas_baja as laba

class NotebookInventario(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        self.venlib = veli.VentanaLibros()
        self.venlam = vela.VentanaLaminas()
        self.venret = vere.BajaLibro()
        self.lambaj = laba.BajaLamina()
        
        self.mytabcontrol = ttk.Notebook(self.master, bootstyle='primary')

        self.libro_tab = ttk.Frame(self.mytabcontrol)
        self.libro_tab.columnconfigure(0, weight=1, minsize=370)
        self.libro_tab.columnconfigure(1, weight=10)
        self.libro_tab.rowconfigure(0, weight=1)
        
        self.lamina_tab = ttk.Frame(self.mytabcontrol) 
        self.lamina_tab.columnconfigure(0, weight=1, minsize=370)
        self.lamina_tab.columnconfigure(1, weight=10)
        self.lamina_tab.rowconfigure(0, weight=1)
        
        self.bajalibro_tab = ttk.Frame(self.mytabcontrol)
        self.bajalibro_tab.columnconfigure(0, weight=1, minsize=340)
        self.bajalibro_tab.columnconfigure(1, weight=1)
        self.bajalibro_tab.rowconfigure(0, weight=1)
        
        self.bajalamina_tab = ttk.Frame(self.mytabcontrol)
        self.bajalamina_tab.columnconfigure(0, weight=1, minsize=340)
        self.bajalamina_tab.columnconfigure(1, weight=1)
        self.bajalamina_tab.rowconfigure(0, weight=1)
        
        
        self.mytabcontrol.add(self.libro_tab, text ='Libros')
        self.mytabcontrol.add(self.lamina_tab, text ='Laminas')
        self.mytabcontrol.add(self.bajalibro_tab, text ='Dados de Baja')
        self.mytabcontrol.add(self.bajalamina_tab, text ='Dados de Baja')
        
        self.mytabcontrol.grid(column=0, row=0, padx=10, pady=10, sticky='nswe')
        
        self.widgets()
        
    def widgets(self):
        #! Funciones label
        libro1p_frame = ttk.LabelFrame(self.libro_tab, text='Información Libro', bootstyle='dark')
        libro1p_frame.grid(column=0, row=0, padx=5, pady=5, sticky='nsw')
        libro1p_frame.columnconfigure(0, weight=1, minsize=180)
        libro1p_frame.columnconfigure(1, weight=1, minsize=180)
        
        libro2p_frame = ttk.LabelFrame(self.libro_tab, text='Visualizacion', bootstyle='dark')
        libro2p_frame.grid(column=1, row=0, padx=5, pady=5, sticky='nsew')
        libro2p_frame.columnconfigure(0, weight=1)
        libro2p_frame.rowconfigure(0, weight=0)
        libro2p_frame.rowconfigure(1, weight=10)
        
        lamina1p_frame = ttk.LabelFrame(self.lamina_tab, text='Información Lamina', bootstyle='dark')
        lamina1p_frame.grid(column=0, row=0, padx=5, pady=5, sticky='nsw')
        lamina1p_frame.columnconfigure(0, weight=1, minsize=180)
        lamina1p_frame.columnconfigure(1, weight=1, minsize=180)
        
        lamina2p_frame = ttk.LabelFrame(self.lamina_tab, text='Visualizacion', bootstyle='dark')
        lamina2p_frame.grid(column=1, row=0, padx=5, pady=5, sticky='nsew')
        lamina2p_frame.columnconfigure(0, weight=1)
        lamina2p_frame.rowconfigure(0, weight=0)
        lamina2p_frame.rowconfigure(1, weight=10)
        
        bajali1p_frame = ttk.LabelFrame(self.bajalibro_tab, text='Funciones', bootstyle='dark')
        bajali1p_frame.grid(column=0, row=0, padx=5, pady=5, sticky='ns')
        bajali1p_frame.columnconfigure(0, weight=1, minsize=139)
        bajali1p_frame.columnconfigure(1, weight=1, minsize=185)
        
        bajali2p_frame = ttk.LabelFrame(self.bajalibro_tab, text='Visualizacion', bootstyle='dark')
        bajali2p_frame.grid(column=1, row=0, padx=5, pady=5, sticky='nsew')
        bajali2p_frame.columnconfigure(0, weight=1)
        bajali2p_frame.rowconfigure(0, weight=0)
        bajali2p_frame.rowconfigure(1, weight=10)

        bajala1p_frame = ttk.LabelFrame(self.bajalamina_tab, text='Funciones', bootstyle='dark')
        bajala1p_frame.grid(column=0, row=0, padx=5, pady=5, sticky='ns')
        bajala1p_frame.columnconfigure(0, weight=1, minsize=139)
        bajala1p_frame.columnconfigure(1, weight=1, minsize=185)
        
        bajala2p_frame = ttk.LabelFrame(self.bajalamina_tab, text='Visualizacion', bootstyle='dark')
        bajala2p_frame.grid(column=1, row=0, padx=5, pady=5, sticky='nsew')
        bajala2p_frame.columnconfigure(0, weight=1)
        bajala2p_frame.rowconfigure(0, weight=0)
        bajala2p_frame.rowconfigure(1, weight=10)

        self.venlib.seccion_uno(libro1p_frame)
        self.venlib.seccion_dos(libro2p_frame)
        self.venlam.seccion_uno(lamina1p_frame)
        self.venlam.seccion_dos(lamina2p_frame)
        self.venret.seccion_uno(bajali1p_frame)
        self.venret.seccion_dos(bajali2p_frame)
        self.lambaj.seccion_uno(bajala1p_frame)
        self.lambaj.seccion_dos(bajala2p_frame)
        