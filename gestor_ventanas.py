import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

import ventana_libros as veli
import ventana_laminas as vela
import pedidos_libros as peli
import pedidos_laminas as pela
import ventana_devoluciones as vede
import ventana_retiro as vere
import ventana_alumnos as veal

class Ventana(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        self.venlib = veli.VentanaLibros()
        self.venlam = vela.VentanaLaminas()
        self.pedlib = peli.PedidosLibros()
        self.pedlam = pela.PedidosLaminas()
        self.vendev = vede.VentanaDevoluciones()
        self.venret = vere.VentanaRetiro()
        self.venalu = veal.VentanaAlumnos()
        self.mytabcontrol = ttk.Notebook(self.master, bootstyle='primary')
        self.libro_tab = ttk.Frame(self.mytabcontrol)
        self.libro_tab.columnconfigure(0, weight=1, minsize=370)
        self.libro_tab.columnconfigure(1, weight=10)
        self.libro_tab.rowconfigure(0, weight=1)
        
        self.lamina_tab = ttk.Frame(self.mytabcontrol) 
        self.lamina_tab.columnconfigure(0, weight=1, minsize=370)
        self.lamina_tab.columnconfigure(1, weight=10)
        self.lamina_tab.rowconfigure(0, weight=1)
        
        self.alumno_tab = ttk.Frame(self.mytabcontrol)
        self.alumno_tab.columnconfigure(0, weight=1, minsize=370)
        self.alumno_tab.columnconfigure(1, weight=10)
        self.alumno_tab.rowconfigure(0, weight=1)
        
        self.pedidoli_tab = ttk.Frame(self.mytabcontrol) 
        self.pedidoli_tab.columnconfigure(0, weight=1, minsize=340)
        self.pedidoli_tab.columnconfigure(1, weight=10)
        self.pedidoli_tab.rowconfigure(0, weight=1)
        
        self.pedidola_tab = ttk.Frame(self.mytabcontrol) 
        self.pedidola_tab.columnconfigure(0, weight=1, minsize=340)
        self.pedidola_tab.columnconfigure(1, weight=10)
        self.pedidola_tab.rowconfigure(0, weight=1)
        
        self.devolu_tab = ttk.Frame(self.mytabcontrol)
        self.devolu_tab.columnconfigure(0, weight=1, minsize=340)
        self.devolu_tab.columnconfigure(1, weight=10)
        self.devolu_tab.rowconfigure(0, weight=1)
        
        self.baja_tab = ttk.Frame(self.mytabcontrol)
        self.baja_tab.columnconfigure(0, weight=1, minsize=340)
        self.baja_tab.columnconfigure(1, weight=1)
        self.baja_tab.rowconfigure(0, weight=1)
        
        
        self.mytabcontrol.add(self.libro_tab, text ='Libros')
        self.mytabcontrol.add(self.lamina_tab, text ='Laminas')
        self.mytabcontrol.add(self.alumno_tab, text ='Alumnos')
        self.mytabcontrol.add(self.pedidoli_tab, text ='Pedidos de Libros')
        self.mytabcontrol.add(self.pedidola_tab, text ='Pedidos de Laminas')
        self.mytabcontrol.add(self.devolu_tab, text ='Devoluciones')
        self.mytabcontrol.add(self.baja_tab, text ='Dados de Baja')
        
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
        
        alumno1p_frame = ttk.LabelFrame(self.alumno_tab, text='Información Alumno', bootstyle='dark')
        alumno1p_frame.grid(column=0, row=0, padx=5, pady=5, sticky='nsw')
        alumno1p_frame.columnconfigure(0, weight=1, minsize=180)
        alumno1p_frame.columnconfigure(1, weight=1, minsize=180)
        
        alumno2p_frame = ttk.LabelFrame(self.alumno_tab, text='Visualizacion', bootstyle='dark')
        alumno2p_frame.grid(column=1, row=0, padx=5, pady=5, sticky='nsew')
        alumno2p_frame.columnconfigure(0, weight=1)
        alumno2p_frame.rowconfigure(0, weight=0)
        alumno2p_frame.rowconfigure(1, weight=10)
        
        peli1p_frame = ttk.LabelFrame(self.pedidoli_tab, text='Informacion Pedido', bootstyle='dark')
        peli1p_frame.grid(column=0, row=0, padx=5, pady=5, sticky='ns')
        peli1p_frame.columnconfigure(0, weight=1, minsize=139)
        peli1p_frame.columnconfigure(1, weight=1, minsize=185)
        
        peli2p_frame = ttk.LabelFrame(self.pedidoli_tab, text='Visualizacion', bootstyle='dark')
        peli2p_frame.grid(column=1, row=0, padx=5, pady=5, sticky='nsew')
        peli2p_frame.columnconfigure(0, weight=1)
        peli2p_frame.rowconfigure(0, weight=0)
        peli2p_frame.rowconfigure(1, weight=10)
        peli2p_frame.rowconfigure(2, weight=0)
        peli2p_frame.rowconfigure(3, weight=10)
        
        pela1p_frame = ttk.LabelFrame(self.pedidola_tab, text='Informacion Pedido', bootstyle='dark')
        pela1p_frame.grid(column=0, row=0, padx=5, pady=5, sticky='ns')
        pela1p_frame.columnconfigure(0, weight=1, minsize=139)
        pela1p_frame.columnconfigure(1, weight=1, minsize=185)
        
        pela2p_frame = ttk.LabelFrame(self.pedidola_tab, text='Visualizacion', bootstyle='dark')
        pela2p_frame.grid(column=1, row=0, padx=5, pady=5, sticky='nsew')
        pela2p_frame.columnconfigure(0, weight=1)
        pela2p_frame.rowconfigure(0, weight=0)
        pela2p_frame.rowconfigure(1, weight=10)
        pela2p_frame.rowconfigure(2, weight=0)
        pela2p_frame.rowconfigure(3, weight=10)
        
        devol1p_frame = ttk.LabelFrame(self.devolu_tab, text='Funciones', bootstyle='dark')
        devol1p_frame.grid(column=0, row=0, padx=5, pady=5, sticky='ns')
        devol1p_frame.columnconfigure(0, weight=1, minsize=139)
        devol1p_frame.columnconfigure(1, weight=1, minsize=185)
        
        devol2p_frame = ttk.LabelFrame(self.devolu_tab, text='Visualizacion', bootstyle='dark')
        devol2p_frame.grid(column=1, row=0, padx=5, pady=5, sticky='nsew')
        devol2p_frame.columnconfigure(0, weight=1)
        devol2p_frame.rowconfigure(0, weight=0)
        devol2p_frame.rowconfigure(1, weight=10)      
        
        baja1p_frame = ttk.LabelFrame(self.baja_tab, text='Funciones', bootstyle='dark')
        baja1p_frame.grid(column=0, row=0, padx=5, pady=5, sticky='ns')
        baja1p_frame.columnconfigure(0, weight=1, minsize=139)
        baja1p_frame.columnconfigure(1, weight=1, minsize=185)
        
        baja2p_frame = ttk.LabelFrame(self.baja_tab, text='Visualizacion', bootstyle='dark')
        baja2p_frame.grid(column=1, row=0, padx=5, pady=5, sticky='nsew')
        baja2p_frame.columnconfigure(0, weight=1)
        baja2p_frame.rowconfigure(0, weight=0)
        baja2p_frame.rowconfigure(1, weight=10)

        self.venlib.seccion_uno(libro1p_frame)
        self.venlib.seccion_dos(libro2p_frame)
        self.venlam.seccion_uno(lamina1p_frame)
        self.venlam.seccion_dos(lamina2p_frame)
        self.pedlib.seccion_uno(peli1p_frame)
        self.pedlib.seccion_dos(peli2p_frame)
        self.pedlam.seccion_uno(pela1p_frame)
        self.pedlam.seccion_dos(pela2p_frame)
        self.vendev.seccion_uno(devol1p_frame)
        self.vendev.seccion_dos(devol2p_frame)
        self.venret.seccion_uno(baja1p_frame)
        self.venret.seccion_dos(baja2p_frame)
        self.venalu.seccion_uno(alumno1p_frame)
        self.venalu.seccion_dos(alumno2p_frame)
        