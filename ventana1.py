import tkinter  as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from PIL import Image, ImageTk
from time import strftime
import pandas as pd
import openpyxl

from conexion_sqlite import Comunicacion
from informes import Informe

class Widgets1v():
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
        self.palabra = tk.StringVar()
        self.nombre_columna = tk.StringVar()
        self.bd = Comunicacion()
        self.photo1 = ImageTk.PhotoImage(Image.open("images/reload.png"))
        self.photo2 = ImageTk.PhotoImage(Image.open("images/excel.png"))
        self.informe = Informe()
        
    def seccion_uno(self, frame_uno):
        #! TEXTO
        reminente_label = ttk.Label(frame_uno, text='Remitente', bootstyle='dark') 
        reminente_label.grid(column=0, row=0, padx=30, pady=[10,5], sticky='we')
        año_recepcion = ttk.Label(frame_uno, text='Año de Recepcion', bootstyle='dark')
        año_recepcion.grid(column=0, row=1, padx=30, pady=5, sticky='we')
        nivel_educativo = ttk.Label(frame_uno, text='Nivel Educativo', bootstyle='dark')
        nivel_educativo.grid(column=0, row=2, padx=30, pady=5, sticky='we')
        titulo = ttk.Label(frame_uno, text='Titulo', bootstyle='dark')
        titulo.grid(column=0, row=3, padx=30, pady=5, sticky='we')
        autor = ttk.Label(frame_uno, text='Autor', bootstyle='dark')
        autor.grid(column=0, row=4, padx=30, pady=5, sticky='we')
        editorial = ttk.Label(frame_uno, text='Editorial', bootstyle='dark')
        editorial.grid(column=0, row=5, padx=30, pady=5, sticky='we')
        año_edicion = ttk.Label(frame_uno, text='Año de edicion', bootstyle='dark')
        año_edicion.grid(column=0, row=6, padx=30, pady=5, sticky='we')
        condicion_libro = ttk.Label(frame_uno, text='Condicion', bootstyle='dark')
        condicion_libro.grid(column=0, row=7, padx=30, pady=5, sticky='we')
        cantidad = ttk.Label(frame_uno, text='Cantidad', bootstyle='dark')
        cantidad.grid(column=0, row=8, padx=30, pady=[5,10], sticky='we')
        #! ENTRADAS
        reminente_entry = ttk.Entry(frame_uno, textvariable=self.remitente, width=10, bootstyle='primary')
        reminente_entry.grid(column=1, row=0, padx=5 ,pady=[10,5], sticky='w')
        añorecepcion_entry = ttk.Entry(frame_uno, textvariable=self.año_recepcion, width=7, bootstyle='primary')
        añorecepcion_entry.grid(column=1, row=1, padx=5 ,pady=5, sticky='w')
        nied_list = ["Primaria", "Secundaria"]
        niveleducativo_combobox = ttk.Combobox(frame_uno, textvariable=self.nivel_educativo ,value=nied_list, width=10, bootstyle='primary')
        niveleducativo_combobox.current(0)
        niveleducativo_combobox.state(["readonly"])
        niveleducativo_combobox.grid(column=1, row=2, padx=5 ,pady=5, sticky='w')
        titulo_entry = ttk.Entry(frame_uno, textvariable=self.titulo, width=20, bootstyle='primary')
        titulo_entry.grid(column=1, row=3, padx=5 ,pady=5, sticky='w')
        autor_entry = ttk.Entry(frame_uno, textvariable=self.autor, width=20, bootstyle='primary')
        autor_entry.grid(column=1, row=4, padx=5 ,pady=5, sticky='w')
        editorial_entry = ttk.Entry(frame_uno, textvariable=self.editorial, bootstyle='primary')
        editorial_entry.grid(column=1, row=5, padx=5 ,pady=5, sticky='w')
        añoedicion_entry = ttk.Entry(frame_uno, textvariable=self.año_edicion, width=7, bootstyle='primary')
        añoedicion_entry.grid(column=1, row=6, padx=5 ,pady=5, sticky='w')
        coli_list = ["A", "B", "C"]
        condicionlibro_combobox = ttk.Combobox(frame_uno, textvariable=self.condicion_libro ,value=coli_list, width=2, bootstyle='primary')
        condicionlibro_combobox.grid(column=1, row=7, padx=5 ,pady=5, sticky='w')
        condicionlibro_combobox.current(0)
        condicionlibro_combobox.state(["readonly"])
        cantidad_entry = ttk.Spinbox(frame_uno, textvariable=self.cantidad, from_=0, to=100, width=5, bootstyle='primary')
        cantidad_entry.state(["readonly"])
        cantidad_entry.grid(column=1, row=8, padx=5 ,pady=[5,10], sticky='w')
        #! Botones
        update_boton = ttk.Button(frame_uno, text='Actualizar Fila', width=15, command=self.actualizar_fila, bootstyle='primary-outline')
        update_boton.grid(column=0, row=9, padx=30, pady=10, sticky='w')
        clear_boton = ttk.Button(frame_uno, text='Limpiar Campos', width=15, command=self.limpiar_campos, bootstyle='primary-outline')
        clear_boton.grid(column=1, row=9, padx=5, pady=10, sticky='w')
        add_boton = ttk.Button(frame_uno, text='Añadir Fila', width=15, command=self.agregar_fila, bootstyle='primary-outline')
        add_boton.grid(column=0, row=10, padx=30, pady=10, sticky='w')
    
    def seccion_dos(self, frame_dos):
        frame_busqueda = ttk.Frame(frame_dos)
        frame_busqueda.grid(column=0, row=0, padx=5, pady=1, sticky='nsew')
        
        l_columna = ("Autor", "Titulo", "Editorial", "AñoRecepcion", "AñoEdicion", "Remitente", "NivelEducativo", "AñoEdicion", "CondicionLibro", "Cantidad")
        buscar_palabra = ttk.Combobox(frame_busqueda, width=15, value=l_columna, 
                                      textvariable=self.nombre_columna, bootstyle='success')
        buscar_palabra.current(0)
        buscar_palabra.state(["readonly"])
        buscar_palabra.pack(side='left', padx=4)
        
        palaba_entry = ttk.Entry(frame_busqueda, textvariable=self.palabra, width=40, bootstyle='success')
        palaba_entry.pack(side='left', padx=4)

        busc_boton = ttk.Button(frame_busqueda, text='Buscar', width=10, 
                                command=self.buscar, bootstyle='success')
        busc_boton.pack(side='left', padx=4)

        save_boton = ttk.Button(frame_busqueda, width=20, image=self.photo2, 
                                command=self.guardar_datos, bootstyle='success-link')
        save_boton.pack(side='left', padx=4)

        show_boton = ttk.Button(frame_busqueda, image=self.photo1,
                                command=self.mostrar_tabla, bootstyle='success-link')
        show_boton.pack(side='right', padx=4)
        
        #! TABLA
        frame_tabla = ttk.LabelFrame(frame_dos, text='Tabla', bootstyle='primary')
        frame_tabla.grid(column=0, row=1, padx=5, pady=[1,5] ,sticky='nsew')
        frame_tabla.columnconfigure(1 , weight=15)
        frame_tabla.rowconfigure(0 , weight=15)
        
        self.tabla = ttk.Treeview(frame_tabla, bootstyle='primary')
        self.tabla.grid(column=1, row=0, sticky='nsew',padx=5, pady=5)
        #! SCROLLBARS
        ladox = ttk.Scrollbar(frame_tabla, orient='horizontal', command=self.tabla.xview, bootstyle='primary-round')
        ladox.grid(column=1, row=1, sticky='ew', padx=5)
        ladoy = ttk.Scrollbar(frame_tabla, orient='vertical', command=self.tabla.yview, bootstyle='primary-round')
        ladoy.grid(column=0, row=0, sticky='ns', pady=5)
        self.tabla.configure(xscrollcommand=ladox.set, yscrollcommand=ladoy.set)
        #! COLUMNAS
        self.tabla['columns'] = ('Remitente', 'Añorecepcion', 'Niveleducativo', 'Titulo', 'Autor', 'Editorial', 'Añoedicion', 'Condicion', 'Cantidad')
        self.tabla.column('#0', minwidth=60, width=60, anchor='center')
        self.tabla.column('#1', minwidth=100, width=100, anchor='center')
        self.tabla.column('#2', minwidth=90, width=110, anchor='center')
        self.tabla.column('#3', minwidth=120, width=120, anchor='center')
        self.tabla.column('#4', minwidth=200, width=200, anchor='w')
        self.tabla.column('#5', minwidth=200, width=200, anchor='w')
        self.tabla.column('#6', minwidth=100, width=105, anchor='w')
        self.tabla.column('#7', minwidth=100, width=100, anchor='center')
        self.tabla.column('#8', minwidth=90, width=90, anchor='center')
        self.tabla.column('#9', minwidth=90, width=90, anchor='center')
            
        self.tabla.heading('#0', text='Nº', anchor='center')
        self.tabla.heading('#1', text='Remitente', anchor='center')
        self.tabla.heading('#2', text='Año Recepcion', anchor='center')
        self.tabla.heading('#3', text='Nivel Educativo', anchor='center')
        self.tabla.heading('#4', text='Titulo', anchor='center')
        self.tabla.heading('#5', text='Autor', anchor='center')
        self.tabla.heading('#6', text='Editorial', anchor='center')
        self.tabla.heading('#7', text='Año Edicion', anchor='center')
        self.tabla.heading('#8', text='Condicion', anchor='center')
        self.tabla.heading('#9', text='Cantidad', anchor='center')
        
        self.tabla.bind("<<TreeviewSelect>>", self.obtener_fila)
        self.tabla.bind("<Double-1>", self.eliminar_datos)

    def obtener_fila(self, event):
        item_selec = self.tabla.focus()
        diccionario_fila = self.tabla.item(item_selec)
        if 'values' in diccionario_fila and len(diccionario_fila['values']) >= 4:
            self.remitente.set(diccionario_fila['values'][0])
            self.año_recepcion.set(diccionario_fila['values'][1])
            self.nivel_educativo.set(diccionario_fila['values'][2])
            self.titulo.set(diccionario_fila['values'][3])
            self.autor.set(diccionario_fila['values'][4])
            self.editorial.set(diccionario_fila['values'][5])
            self.año_edicion.set(diccionario_fila['values'][6])
            self.condicion_libro.set(diccionario_fila['values'][7])
            self.cantidad.set(diccionario_fila['values'][8])
        else:
            self.limpiar_campos()
            
    def mostrar_tabla(self):
        self.limpiar_campos()
        l_datos = self.bd.show_libros()
        self.tabla.delete(*self.tabla.get_children())
        i = -1
        for fila in l_datos:
            i = i+1
            self.tabla.insert('', i,text=i+1, values=fila[0:11])
            
    def limpiar_campos(self):
        self.remitente.set('')
        self.año_recepcion.set('')
        self.nivel_educativo.set('')
        self.titulo.set('')
        self.autor.set('')
        self.editorial.set('')
        self.año_edicion.set('')
        self.condicion_libro.set('')
        self.cantidad.set(0)
    
    def actualizar_fila(self):
        item_l = self.tabla.focus()
        diccionario_fila = self.tabla.item(item_l)
        if len(diccionario_fila['values']) != 0:
            id = diccionario_fila['values'][9]
            l_datos = self.bd.show_libros()
            
            for fila in l_datos:
                id_bd = fila[9]
                if id_bd == id and id_bd != None:
                    remitente = self.remitente.get()
                    añorecepcion = self.año_recepcion.get()
                    niveleducativo = self.nivel_educativo.get()
                    titulo = self.titulo.get()
                    autor = self.autor.get()
                    editorial = self.editorial.get()
                    añoedicion = self.año_edicion.get()
                    condicionlibro = self.condicion_libro.get()
                    cantidad = self.cantidad.get()
                    confirmar_box = messagebox.askokcancel('Información', 'Se modificará la fila seleccionada')
                    if remitente and niveleducativo and titulo and condicionlibro and cantidad != '' and confirmar_box == True:
                        self.bd.update_libros(id, remitente, añorecepcion, niveleducativo, titulo, autor, editorial, añoedicion, condicionlibro, cantidad)
                        messagebox.showinfo('Información', 'Fila modificada')
                        self.mostrar_tabla()
        else:
            messagebox.showerror('ERROR', 'Falta Rellenar')

    def agregar_fila(self):
        remitente = self.remitente.get()
        añorecepcion = self.año_recepcion.get()
        niveleducativo = self.nivel_educativo.get()
        titulo = self.titulo.get()
        autor = self.autor.get()
        editorial = self.editorial.get()
        añoedicion = self.año_edicion.get()
        condicionlibro = self.condicion_libro.get()
        cantidad = self.cantidad.get()
        c_filas = len(self.tabla.get_children())
        datos = (remitente, añorecepcion, niveleducativo, titulo, autor, editorial ,añoedicion, condicionlibro, cantidad)

        if remitente and niveleducativo and titulo and condicionlibro != '' and cantidad > 0:
            question_box = messagebox.askquestion('Información', '¿Desea agregar la fila?')
            if question_box == 'yes':
                self.bd.agregar_libro(remitente, añorecepcion, niveleducativo, titulo, autor, editorial ,añoedicion, condicionlibro, cantidad)
                self.tabla.insert('',"end",text=c_filas+1, values=datos)
                messagebox.showinfo('Información', 'Fila agregada')
                self.limpiar_campos()
        else:
            messagebox.showerror('ERROR', 'Falta Rellenar')
    
    def eliminar_datos(self, event):
        self.limpiar_campos()
        l_item = self.tabla.selection()[0]
        diccionario_fila = self.tabla.item(l_item)
        question_box = messagebox.askquestion('Información', '¿Desea eliminar la fila?')
        if question_box == 'yes':
            self.tabla.delete(l_item)
            self.limpiar_campos()
            self.bd.delete_libro(diccionario_fila['values'][9])
            messagebox.showinfo('Información', 'Fila Eliminada')
    
    def buscar(self):
        self.limpiar_campos()
        palabra = self.palabra.get()
        columna = self.nombre_columna.get()
        if palabra != '':
            l_datos = self.bd.buscar_libros(columna, palabra)
            self.tabla.delete(*self.tabla.get_children())
            i = -1
            for fila in l_datos:
                i = i+1
                self.tabla.insert('', i,text=i+1, values=fila[0:11])
        else:
            messagebox.showerror('ERROR', 'No se agrego una busqueda')
    
    def guardar_datos(self):
        self.limpiar_campos()
        self.informe.guardar_datos()
        messagebox.showinfo('Informacion', 'Datos guardados')