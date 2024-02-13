import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

import ventana_libros as ven1
import ventana_laminas as ven2
import ventana_pedidos as ven3
import ventana_devoluciones as ven4
import ventana_retiro as ven5
import ventana_usuarios as ven6

class Ventana(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        self.v1 = ven1.VentanaLibros()
        self.v2 = ven2.VentanaLaminas()
        self.v3 = ven3.VentanaPedidos()
        self.v4 = ven4.VentanaDevoluciones()
        self.v5 = ven5.VentanaRetiro()
        self.v6 = ven6.VentanaUsuarios()
        self.mytabcontrol = ttk.Notebook(self.master, bootstyle='primary')
        self.mytab1 = ttk.Frame(self.mytabcontrol)
        self.mytab1.columnconfigure(0, weight=1, minsize=370)
        self.mytab1.columnconfigure(1, weight=10)
        self.mytab1.rowconfigure(0, weight=1)
        
        self.mytab2 = ttk.Frame(self.mytabcontrol) 
        self.mytab2.columnconfigure(0, weight=1, minsize=370)
        self.mytab2.columnconfigure(1, weight=10)
        self.mytab2.rowconfigure(0, weight=1)
        
        self.mytab3 = ttk.Frame(self.mytabcontrol)
        self.mytab3.columnconfigure(0, weight=1, minsize=370)
        self.mytab3.columnconfigure(1, weight=10)
        self.mytab3.rowconfigure(0, weight=1)
        
        self.mytab4 = ttk.Frame(self.mytabcontrol) 
        self.mytab4.columnconfigure(0, weight=1, minsize=340)
        self.mytab4.columnconfigure(1, weight=10)
        self.mytab4.rowconfigure(0, weight=1)
        
        self.mytab5 = ttk.Frame(self.mytabcontrol)
        self.mytab5.columnconfigure(0, weight=1, minsize=340)
        self.mytab5.columnconfigure(1, weight=10)
        self.mytab5.rowconfigure(0, weight=1)
        
        self.mytab6 = ttk.Frame(self.mytabcontrol)
        self.mytab6.columnconfigure(0, weight=1, minsize=340)
        self.mytab6.columnconfigure(1, weight=1)
        self.mytab6.rowconfigure(0, weight=1)
        
        
        self.mytabcontrol.add(self.mytab1, text ='Libros')
        self.mytabcontrol.add(self.mytab2, text ='Laminas')
        self.mytabcontrol.add(self.mytab3, text ='Usuarios')
        self.mytabcontrol.add(self.mytab4, text ='Pedidos')
        self.mytabcontrol.add(self.mytab5, text ='Devoluciones')
        self.mytabcontrol.add(self.mytab6, text ='Dados de Baja')
        
        self.mytabcontrol.grid(column=0, row=0, padx=10, pady=10, sticky='nswe')
        
        self.widgets()
        
    def widgets(self):
        #! Funciones label
        frame_uno = ttk.LabelFrame(self.mytab1, text='Información Libro', bootstyle='dark')
        frame_uno.grid(column=0, row=0, padx=5, pady=5, sticky='nsw')
        frame_uno.columnconfigure(0, weight=1, minsize=180)
        frame_uno.columnconfigure(1, weight=1, minsize=180)
        
        frame_dos = ttk.LabelFrame(self.mytab1, text='Visualizacion', bootstyle='dark')
        frame_dos.grid(column=1, row=0, padx=5, pady=5, sticky='nsew')
        frame_dos.columnconfigure(0, weight=1)
        frame_dos.rowconfigure(0, weight=0)
        frame_dos.rowconfigure(1, weight=10)
        
        frame_tres = ttk.LabelFrame(self.mytab2, text='Información Lamina', bootstyle='dark')
        frame_tres.grid(column=0, row=0, padx=5, pady=5, sticky='nsw')
        frame_tres.columnconfigure(0, weight=1, minsize=180)
        frame_tres.columnconfigure(1, weight=1, minsize=180)
        
        frame_cuatro = ttk.LabelFrame(self.mytab2, text='Visualizacion', bootstyle='dark')
        frame_cuatro.grid(column=1, row=0, padx=5, pady=5, sticky='nsew')
        frame_cuatro.columnconfigure(0, weight=1)
        frame_cuatro.rowconfigure(0, weight=0)
        frame_cuatro.rowconfigure(1, weight=10)
        
        frame_cinco = ttk.LabelFrame(self.mytab3, text='Información Usuario', bootstyle='dark')
        frame_cinco.grid(column=0, row=0, padx=5, pady=5, sticky='nsw')
        frame_cinco.columnconfigure(0, weight=1, minsize=180)
        frame_cinco.columnconfigure(1, weight=1, minsize=180)
        
        frame_seis = ttk.LabelFrame(self.mytab3, text='Visualizacion', bootstyle='dark')
        frame_seis.grid(column=1, row=0, padx=5, pady=5, sticky='nsew')
        frame_seis.columnconfigure(0, weight=1)
        frame_seis.rowconfigure(0, weight=0)
        frame_seis.rowconfigure(1, weight=10)
        
        frame_siete = ttk.LabelFrame(self.mytab4, text='Informacion Pedido', bootstyle='dark')
        frame_siete.grid(column=0, row=0, padx=5, pady=5, sticky='ns')
        frame_siete.columnconfigure(0, weight=1, minsize=139)
        frame_siete.columnconfigure(1, weight=1, minsize=185)
        
        frame_ocho = ttk.LabelFrame(self.mytab4, text='Visualizacion', bootstyle='dark')
        frame_ocho.grid(column=1, row=0, padx=5, pady=5, sticky='nsew')
        frame_ocho.columnconfigure(0, weight=1)
        frame_ocho.rowconfigure(0, weight=0)
        frame_ocho.rowconfigure(1, weight=10)
        frame_ocho.rowconfigure(2, weight=0)
        frame_ocho.rowconfigure(3, weight=10)
        
        frame_nueve = ttk.LabelFrame(self.mytab5, text='Funciones', bootstyle='dark')
        frame_nueve.grid(column=0, row=0, padx=5, pady=5, sticky='ns')
        frame_nueve.columnconfigure(0, weight=1, minsize=139)
        frame_nueve.columnconfigure(1, weight=1, minsize=185)
        
        frame_diez = ttk.LabelFrame(self.mytab5, text='Visualizacion', bootstyle='dark')
        frame_diez.grid(column=1, row=0, padx=5, pady=5, sticky='nsew')
        frame_diez.columnconfigure(0, weight=1)
        frame_diez.rowconfigure(0, weight=0)
        frame_diez.rowconfigure(1, weight=10)      
        
        frame_once = ttk.LabelFrame(self.mytab6, text='Funciones', bootstyle='dark')
        frame_once.grid(column=0, row=0, padx=5, pady=5, sticky='ns')
        frame_once.columnconfigure(0, weight=1, minsize=139)
        frame_once.columnconfigure(1, weight=1, minsize=185)
        
        frame_doce = ttk.LabelFrame(self.mytab6, text='Visualizacion', bootstyle='dark')
        frame_doce.grid(column=1, row=0, padx=5, pady=5, sticky='nsew')
        frame_doce.columnconfigure(0, weight=1)
        frame_doce.rowconfigure(0, weight=0)
        frame_doce.rowconfigure(1, weight=10)

        self.v1.seccion_uno(frame_uno)
        self.v1.seccion_dos(frame_dos)
        self.v2.seccion_uno(frame_tres)
        self.v2.seccion_dos(frame_cuatro)
        self.v3.seccion_uno(frame_siete)
        self.v3.seccion_dos(frame_ocho)
        self.v4.seccion_uno(frame_nueve)
        self.v4.seccion_dos(frame_diez)
        self.v5.seccion_uno(frame_once)
        self.v5.seccion_dos(frame_doce)
        self.v6.seccion_uno(frame_cinco)
        self.v6.seccion_dos(frame_seis)
        