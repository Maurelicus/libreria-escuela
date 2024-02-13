import tkinter  as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from PIL import Image, ImageTk
from time import strftime
import pandas as pd
import openpyxl

from conexion_sqlite import Comunicacion
from informes import Informe

class VentanaUsuarios():
    def __init__(self):
        self.usuarioid = tk.StringVar()
        self.usuario = tk.StringVar()
        self.sexo = tk.StringVar()
        self.nivel = tk.StringVar()
        self.grado = tk.StringVar()
        self.seccion = tk.StringVar()
        self.palabra = tk.StringVar()
        self.nombre_columna = tk.StringVar()
        self.bd = Comunicacion()
        self.photo1 = ImageTk.PhotoImage(Image.open("images/reload.png"))
        self.photo2 = ImageTk.PhotoImage(Image.open("images/excel.png"))
        self.informe = Informe()
        
    def seccion_uno(self, frame_uno):
        #! TEXTO
        usuarioid_label = ttk.Label(frame_uno, text='Codigo', bootstyle='dark') 
        usuarioid_label.grid(column=0, row=0, padx=30, pady=[10,5], sticky='we')
        usuario = ttk.Label(frame_uno, text='Usuario', bootstyle='dark')
        usuario.grid(column=0, row=1, padx=30, pady=5, sticky='we')
        sexo = ttk.Label(frame_uno, text='Sexo', bootstyle='dark')
        sexo.grid(column=0, row=2, padx=30, pady=5, sticky='we')
        nivel = ttk.Label(frame_uno, text='Nivel', bootstyle='dark')
        nivel.grid(column=0, row=3, padx=30, pady=5, sticky='we')
        grado = ttk.Label(frame_uno, text='Grado', bootstyle='dark')
        grado.grid(column=0, row=4, padx=30, pady=5, sticky='we')
        seccion = ttk.Label(frame_uno, text='Seccion', bootstyle='dark')
        seccion.grid(column=0, row=5, padx=30, pady=[5,10], sticky='we')
        #! ENTRADAS
        usuarioid_entry = ttk.Entry(frame_uno, textvariable=self.usuarioid, width=10, bootstyle='primary')
        usuarioid_entry.grid(column=1, row=0, padx=5 ,pady=[10,5], sticky='w')
        usuario_entry = ttk.Entry(frame_uno, textvariable=self.usuario, width=7, bootstyle='primary')
        usuario_entry.grid(column=1, row=1, padx=5 ,pady=5, sticky='w')
        se_list = ["Hombre", "Mujer"]
        sexo_combobox = ttk.Combobox(frame_uno, textvariable=self.sexo ,value=se_list, width=10, bootstyle='primary')
        sexo_combobox.current(1)
        sexo_combobox.state(["readonly"])
        sexo_combobox.grid(column=1, row=2, padx=5 ,pady=5, sticky='w')
        ni_list = ["Primaria", "Secundaria"]
        nivel_combobox = ttk.Combobox(frame_uno, textvariable=self.nivel ,value=ni_list, width=10, bootstyle='primary')
        nivel_combobox.current(0)
        nivel_combobox.state(["readonly"])
        nivel_combobox.grid(column=1, row=3, padx=5 ,pady=5, sticky='w')
        gra_list = ["PRIMERO", "SEGUNDO", "TERCERO", "CUARTO", "QUINTO", "SEXTO"]
        grado_combobox = ttk.Combobox(frame_uno, textvariable=self.grado ,value=gra_list, width=10, bootstyle='primary')
        grado_combobox.current(0)
        grado_combobox.state(["readonly"])
        grado_combobox.grid(column=1, row=4, padx=5 ,pady=5, sticky='w')
        sec_list = ["A", "B", "C", "D", "E"]
        seccion_combobox = ttk.Combobox(frame_uno, textvariable=self.seccion ,value=sec_list, width=10, bootstyle='primary')
        seccion_combobox.current(0)
        seccion_combobox.state(["readonly"])
        seccion_combobox.grid(column=1, row=5, padx=5 ,pady=[5,10], sticky='w')
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
        
        l_columna = ("Codigo", "Usuario", "Sexo", "Nivel", "Grado", "Seccion")
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
                                bootstyle='success-link')
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
        self.tabla['columns'] = ('UsuarioId', 'Usuario', 'Sexo', 'Nivel', 'Grado', 'Seccion')
        self.tabla.column('#0', minwidth=60, width=60, anchor='center')
        self.tabla.column('#1', minwidth=100, width=100, anchor='center')
        self.tabla.column('#2', minwidth=90, width=110, anchor='center')
        self.tabla.column('#3', minwidth=120, width=120, anchor='center')
        self.tabla.column('#4', minwidth=200, width=200, anchor='w')
        self.tabla.column('#5', minwidth=200, width=200, anchor='w')
        self.tabla.column('#6', minwidth=100, width=105, anchor='w')

        self.tabla.heading('#0', text='Nº', anchor='center')
        self.tabla.heading('#1', text='Codigo', anchor='center')
        self.tabla.heading('#2', text='Usuario', anchor='center')
        self.tabla.heading('#3', text='Sexo', anchor='center')
        self.tabla.heading('#4', text='Nivel', anchor='center')
        self.tabla.heading('#5', text='Grado', anchor='center')
        self.tabla.heading('#6', text='Seccion', anchor='center')
        
        self.tabla.bind("<<TreeviewSelect>>", self.obtener_fila)
        self.tabla.bind("<Double-1>", self.eliminar_datos)

    def mostrar_tabla(self):
        self.limpiar_campos()
        l_datos = self.bd.show_usuarios()
        self.tabla.delete(*self.tabla.get_children())
        i = -1
        for fila in l_datos:
            i = i+1
            self.tabla.insert('', i,text=i+1, values=fila[0:6])
            
    def obtener_fila(self, event):
        item_selec = self.tabla.focus()
        diccionario_fila = self.tabla.item(item_selec)
        if 'values' in diccionario_fila and len(diccionario_fila['values']) >= 2:
            self.usuarioid.set(diccionario_fila['values'][0])
            self.usuario.set(diccionario_fila['values'][1])
            self.sexo.set(diccionario_fila['values'][2])
            self.nivel.set(diccionario_fila['values'][3])
            self.grado.set(diccionario_fila['values'][4])
            self.seccion.set(diccionario_fila['values'][5])
        else:
            self.limpiar_campos()            
            
    def limpiar_campos(self):
        self.usuarioid.set('')
        self.usuario.set('')
        self.sexo.set('')
        self.nivel.set('')
        self.grado.set('')
        self.seccion.set('')
    """ 
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

    """
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
        if columna == "Año de recepcion":
            columna = "AñoRecepcion"
        elif columna == "Nivel educativo":
            columna = "NivelEducativo"
        elif columna == "Año de edicion":
            columna = "AñoEdicion"
        elif columna == "Condicion del libro":
            columna = "CondicionLibro"
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