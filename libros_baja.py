import tkinter  as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from PIL import Image, ImageTk
from time import strftime
import pandas as pd
import openpyxl

from conexion_sqlite import Comunicacion
from informes import Informes

class BajaLibro():
    def __init__(self):
        self.remitente = tk.StringVar()
        self.año_recepcion = tk.StringVar()
        self.nivel_educativo = tk.StringVar()
        self.titulo = tk.StringVar()
        self.autor = tk.StringVar()
        self.editorial = tk.StringVar()
        self.año_edicion = tk.StringVar()
        self.condicion_libro = tk.StringVar()
        self.cantidad = tk.IntVar()
        self.categoria = tk.StringVar()
        self.palabra = tk.StringVar()
        self.nombre_columna = tk.StringVar()
        self.bd = Comunicacion()
        self.photo1 = ImageTk.PhotoImage(Image.open("images/reload.png"))
        self.photo2 = ImageTk.PhotoImage(Image.open("images/excel.png"))
        self.informe = Informes()
        self.cat_dic = {}

        
    def seccion_uno(self, frame_datos):
        #! TEXTO
        ttk.Label(frame_datos, 
            text='DATOS DEL LIBRO:', 
            bootstyle='danger'
            ).grid(column=0, row=1, padx=30, pady=10, sticky='w', columnspan=2)

        titulo_label = ttk.Label(frame_datos, text='Titulo', bootstyle='dark')
        titulo_label.grid(column=0, row=2, padx=30, pady=5, sticky='we')
        autor_label = ttk.Label(frame_datos, text='Autor', bootstyle='dark')
        autor_label.grid(column=0, row=3, padx=30, pady=5, sticky='we')
        editorial_label = ttk.Label(frame_datos, text='Editorial', bootstyle='dark')
        editorial_label.grid(column=0, row=4, padx=30, pady=5, sticky='we')
        cantidad_label = ttk.Label(frame_datos, text='Cantidad', bootstyle='dark')
        cantidad_label.grid(column=0, row=5, padx=30, pady=5, sticky='we')
        condicionlibro_label = ttk.Label(frame_datos, text='Condicion', bootstyle='dark')
        condicionlibro_label.grid(column=0, row=6, padx=30, pady=5, sticky='we')

        #! ENTRADAS
        dtitulo_label = ttk.Label(frame_datos, textvariable=self.titulo, wraplength=160, bootstyle='primary')
        dtitulo_label.grid(column=1, row=2, padx=5, pady=5, sticky='w')
        dautor_label = ttk.Label(frame_datos, textvariable=self.autor, wraplength=160, bootstyle='primary')
        dautor_label.grid(column=1, row=3, padx=5, pady=5, sticky='w')
        deditorial_label = ttk.Label(frame_datos, textvariable=self.editorial, wraplength=160, bootstyle='primary')
        deditorial_label.grid(column=1, row=4, padx=5, pady=5, sticky='w')
        dcantidad_label = ttk.Label(frame_datos, textvariable=self.cantidad, wraplength=160, bootstyle='primary')
        dcantidad_label.grid(column=1, row=5, padx=5 ,pady=5, sticky='w')
        dcondicion_label = ttk.Label(frame_datos, textvariable=self.condicion_libro, wraplength=160, bootstyle='primary')
        dcondicion_label.grid(column=1, row=6, padx=5, pady=5, sticky='w')

        #! Botones
        reponer_boton = ttk.Button(frame_datos, text='Reponer', width=20, command=self.reponer_libro, bootstyle='primary-outline')
        reponer_boton.grid(column=0, row=7, padx=30, pady=10, sticky='w', columnspan=2)
        
    def seccion_dos(self, frame_vista):
        busqueda_frame = ttk.Frame(frame_vista)
        busqueda_frame.grid(column=0, row=0, padx=5, pady=1, sticky='nsew')
        # falta trabajar cantidad y categoria
        col_list = ("Autor", "Titulo", "Editorial", "Año de recepcion",
                     "Año de edicion", "Remitente", "Nivel educativo", 
                     "Condicion del libro", "Cantidad")
        buscarpalabra_combobox = ttk.Combobox(busqueda_frame, width=15, value=col_list, 
                                      textvariable=self.nombre_columna, bootstyle='success')
        buscarpalabra_combobox.current(0)
        buscarpalabra_combobox.state(["readonly"])
        buscarpalabra_combobox.pack(side='left', padx=4)
        
        palabra_entry = ttk.Entry(busqueda_frame, textvariable=self.palabra, width=40, bootstyle='success')
        palabra_entry.pack(side='left', padx=4)

        serch_boton = ttk.Button(busqueda_frame, text='Buscar', width=10, 
                                command=self.buscar, bootstyle='success')
        serch_boton.pack(side='left', padx=4)

        save_boton = ttk.Button(busqueda_frame, width=20, image=self.photo2, 
                                command=self.limpiar_campos, bootstyle='success-link')
        save_boton.pack(side='left', padx=4)

        show_boton = ttk.Button(busqueda_frame, image=self.photo1,
                                command=self.mostrar_libros, bootstyle='success-link')
        show_boton.pack(side='right', padx=4)
        
        #! TABLA
        tabla_frame = ttk.LabelFrame(frame_vista, text='Lista de Libros', bootstyle='primary')
        tabla_frame.grid(column=0, row=1, padx=5, pady=[1,5] ,sticky='nsew')
        tabla_frame.columnconfigure(1 , weight=15)
        tabla_frame.rowconfigure(0 , weight=15)
        
        self.tabla = ttk.Treeview(tabla_frame, bootstyle='primary')
        self.tabla.grid(column=1, row=0, sticky='nsew',padx=5, pady=5)
        #! SCROLLBARS
        ladox = ttk.Scrollbar(tabla_frame, orient='horizontal', command=self.tabla.xview, bootstyle='primary-round')
        ladox.grid(column=1, row=1, sticky='ew', padx=5)
        ladoy = ttk.Scrollbar(tabla_frame, orient='vertical', command=self.tabla.yview, bootstyle='primary-round')
        ladoy.grid(column=0, row=0, sticky='ns', pady=5)
        self.tabla.configure(xscrollcommand=ladox.set, yscrollcommand=ladoy.set)
        #! COLUMNAS
        self.tabla['columns'] = ('Titulo','Autor','Editorial','Añoedicion','Categoria','Cantidad','Remitente','Niveleducativo', 'Condicion', 'Añorecepcion')
        self.tabla.column('#0', minwidth=60, width=60, anchor='center')
        self.tabla.column('#1', minwidth=150, width=200, anchor='w')
        self.tabla.column('#2', minwidth=100, width=150, anchor='w')
        self.tabla.column('#3', minwidth=80, width=120, anchor='w')
        self.tabla.column('#4', minwidth=50, width=100, anchor='center')
        self.tabla.column('#5', minwidth=80, width=140, anchor='center')
        self.tabla.column('#6', minwidth=50, width=100, anchor='center')
        self.tabla.column('#7', minwidth=80, width=120, anchor='w')
        self.tabla.column('#8', minwidth=80, width=120, anchor='center')
        self.tabla.column('#9', minwidth=50, width=100, anchor='center')
        self.tabla.column('#10', minwidth=50, width=100, anchor='center')
            
        self.tabla.heading('#0', text='Nº', anchor='center')
        self.tabla.heading('#1', text='Titulo', anchor='center')
        self.tabla.heading('#2', text='Autor', anchor='center')
        self.tabla.heading('#3', text='Editorial', anchor='center')
        self.tabla.heading('#4', text='Año Edicion', anchor='center')
        self.tabla.heading('#5', text='Tipo', anchor='center')
        self.tabla.heading('#6', text='Cantidad', anchor='center')
        self.tabla.heading('#7', text='Remitente', anchor='center')
        self.tabla.heading('#8', text='Nivel Educativo', anchor='center')
        self.tabla.heading('#9', text='Condicion', anchor='center')
        self.tabla.heading('#10', text='Año Recepcion', anchor='center')
        self.tabla.tag_configure('Baja', background='#bfc9ca')

        self.tabla.bind("<<TreeviewSelect>>", self.obtener_libro)

    def mostrar_libros(self):
        self.limpiar_campos()
        l_datos = self.bd.show_libros()
        # print(l_datos)
        self.tabla.delete(*self.tabla.get_children())
        i = -1
        for fila in l_datos:
            i = i+1
            if fila[4] == 'Baja':
                self.tabla.insert('', i,text=i+1, values=fila[0:11], tags=fila[4])

    def obtener_libro(self, event):
        item_selec = self.tabla.focus()
        diccionario_fila = self.tabla.item(item_selec)
        # print(diccionario_fila)
        if 'values' in diccionario_fila and len(diccionario_fila['values']) != 0:
            self.titulo.set(diccionario_fila['values'][0])
            self.autor.set(diccionario_fila['values'][1])
            self.editorial.set(diccionario_fila['values'][2])
            self.cantidad.set(diccionario_fila['values'][5])
            self.condicion_libro.set(diccionario_fila['values'][8])
        else:
            self.limpiar_campos()
        
            
    def limpiar_campos(self):
        self.titulo.set('')
        self.autor.set('')
        self.editorial.set('')
        self.cantidad.set(0)
        self.condicion_libro.set('')
    
    
    def buscar(self):
        self.limpiar_campos()
        palabra = self.palabra.get()
        columna = self.nombre_columna.get()
        if columna == "Año de recepcion":
            columna = "AñoRecepcion"
        elif columna == "Nivel educativo":
            columna = "NivelEducativo"
        elif columna == "Año de edicion":
            columna = "AñoEdicion"
        elif columna == "Condicion del libro":
            columna = "CondicionLibro"
            
        if palabra != '':
            l_datos = self.bd.search_libros(columna, palabra)
            self.tabla.delete(*self.tabla.get_children())
            i = -1
            for fila in l_datos:
                i = i+1
                if fila[4] == 'Baja':
                    self.tabla.insert('', i,text=i+1, values=fila[0:11], tags=fila[4])
        else:
            messagebox.showerror('ERROR', 'No se agrego una busqueda')
            
    def reponer_libro(self):
        l_item = self.tabla.focus()
        diccionario_libro = self.tabla.item(l_item)
        if 'values' in diccionario_libro and len(diccionario_libro['values']) != 0:
            titulo = diccionario_libro['values'][0]
            autor = diccionario_libro['values'][1]
            editorial = diccionario_libro['values'][2]
            a_edicion = diccionario_libro['values'][3]
            categoria = 25
            cantidad_repuesta = diccionario_libro['values'][5]
            remitente = diccionario_libro['values'][6]
            n_educativo = diccionario_libro['values'][7]
            c_libro = diccionario_libro['values'][8]
            a_recepcion = diccionario_libro['values'][9]
            libroid = diccionario_libro['values'][10]
            question_box = messagebox.askquestion('Información', '¿Desea reponer el libro seleccionado?')
            if question_box == 'yes':
                self.bd.update_libros(libroid,remitente,a_recepcion,n_educativo,titulo,autor,editorial,a_edicion,c_libro,cantidad_repuesta,categoria)
                messagebox.showinfo('Información', 'Libro(s) repuestos')
                self.mostrar_libros()
            else:
                messagebox.showerror('Información', 'Proceso erroneo')
        else:
            messagebox.showerror('ERROR', 'Selecciona un libro')
