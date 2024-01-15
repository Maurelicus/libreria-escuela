import tkinter as tk
from tkinter import ttk, messagebox, PhotoImage
from PIL import Image, ImageTk

from conexion_sqlite import Comunicacion
import g1_widgets as gw1

class Ventana(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.remitente = tk.StringVar()
        self.año_recepcion = tk.StringVar()
        self.nivel_educativo = tk.StringVar()
        self.titulo = tk.StringVar()
        self.autor = tk.StringVar()
        self.editorial = tk.StringVar()
        self.año_edicion = tk.StringVar()
        self.condicion_libro = tk.StringVar()
        self.cantidad = tk.StringVar()
        self.palabra = tk.StringVar()
        self.nombre_columna = tk.StringVar()
        self.bd = Comunicacion()
        self.boton4 = ttk.Button(self, text="Display")
        self.boton4.grid(column=0, row=0,padx=5, pady=30, sticky='n')
        self.widgets()
        
    def widgets(self):
        #! Funciones label
        # height=altura/width=ancho
        self.frame_operaciones = ttk.LabelFrame(self,text='Funciones')
        self.frame_operaciones.grid(column=1, row=0, sticky='ns', padx=10)
        self.frame_operaciones.columnconfigure(0, weight=1)
        self.frame_operaciones.rowconfigure(0, weight=1)
        frame_uno = ttk.LabelFrame(self.frame_operaciones, text='Frame 1')
        frame_uno.grid(column=0, row=0, padx=5, pady=5, sticky='ns')
        #* Widgets de funciones
        lista_atributos1 = [self.remitente, self.año_recepcion, 
                        self.nivel_educativo, self.titulo, 
                        self.autor, self.editorial, self.año_edicion, 
                        self.condicion_libro, self.cantidad]
        lista_metodos1 = [self.limpiar_campos, self.actualizar_fila, 
                        self.agregar_fila]
        gw1.seccion_uno(frame_uno, lista_metodos1, lista_atributos1)
        
        #! Tabla Label
        self.frame_tabla = ttk.LabelFrame(self, text='Tabla')
        self.frame_tabla.grid(column=2, row=0, sticky='nsew')
        self.frame_tabla.columnconfigure(0, weight=1)
        self.frame_tabla.rowconfigure(0, weight=0)
        self.frame_tabla.rowconfigure(1, weight=10)
        
        frame_dos = ttk.LabelFrame(self.frame_tabla, text='Frame 2')
        frame_dos.grid(column=0, row=0, padx=5, pady=5, sticky='ew')
        lista_atributos2 = [self.palabra, self.nombre_columna]
        lista_metodos2 = [self.actualizar_tabla, self.buscador]
        self.photo1 = ImageTk.PhotoImage(Image.open("reload.png"))
        self.photo2 = ImageTk.PhotoImage(Image.open("excel.png"))
        gw1.seccion_dos(frame_dos, lista_metodos2, lista_atributos2, self.photo1, self.photo2)
        #* Widgets de tabla
        #! TABLA
        frame_tablaca = ttk.LabelFrame(self.frame_tabla, text='Frame 3')
        frame_tablaca.grid(column=0, row=1, padx=5, pady=5 ,sticky='nsew')
        frame_tablaca.columnconfigure(1 , weight=10)
        frame_tablaca.rowconfigure(0 , weight=10)
        # frame_tablaca.rowconfigure(1 , weight=1)
        # frame_tablaca.columnconfigure(0 , weight=10)
        
        
        self.tabla = ttk.Treeview(frame_tablaca)
        self.tabla.grid(column=1, row=0, sticky='nsew',padx=5, pady=5)
        # self.tabla.columnconfigure(1, weight=10)
        #! SCROLLBARS
        ladox = ttk.Scrollbar(frame_tablaca, orient='horizontal', command=self.tabla.xview)
        ladox.grid(column=1, row=1, sticky='ew', padx=5)
        ladoy = ttk.Scrollbar(frame_tablaca, orient='vertical', command=self.tabla.yview)
        ladoy.grid(column=0, row=0, sticky='ns', pady=5)
        self.tabla.configure(xscrollcommand=ladox.set, yscrollcommand=ladoy.set)
        #! COLUMNAS
        self.tabla['columns'] = ('Remitente', 'Añorecepcion', 'Niveleducativo', 'Titulo', 'Autor', 'Editorial', 'Añoedicion', 'Condicion', 'Cantidad')
        self.tabla.column('#0', minwidth=60, width=60, anchor='center')
        self.tabla.column('#1', minwidth=100, width=100, anchor='center')
        self.tabla.column('#2', minwidth=100, width=120, anchor='center')
        self.tabla.column('#3', minwidth=120, width=120, anchor='center')
        self.tabla.column('#4', minwidth=200, width=200, anchor='w')
        self.tabla.column('#5', minwidth=200, width=200, anchor='w')
        self.tabla.column('#6', minwidth=100, width=105, anchor='w')
        self.tabla.column('#7', minwidth=100, width=100, anchor='center')
        self.tabla.column('#8', minwidth=90, width=90, anchor='center')
        self.tabla.column('#9', minwidth=90, width=90, anchor='center')
        
        self.tabla.heading('#0', text='Nº', anchor='center')
        self.tabla.heading('#1', text='Remitente', anchor='center')
        self.tabla.heading('#2', text='Año recepcion', anchor='center')
        self.tabla.heading('#3', text='Nivel educativo', anchor='center')
        self.tabla.heading('#4', text='Titulo', anchor='center')
        self.tabla.heading('#5', text='Autor', anchor='center')
        self.tabla.heading('#6', text='Editorial', anchor='center')
        self.tabla.heading('#7', text='Año edicion', anchor='center')
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
            
    def actualizar_tabla(self):
        self.limpiar_campos()
        l_datos = self.bd.mostrar_datos()
        self.tabla.delete(*self.tabla.get_children())
        i = -1
        for fila in l_datos:
            i = i+1
            self.tabla.insert('', i,text=fila[0], values=fila[1:11])
            
    def limpiar_campos(self):
        self.remitente.set('')
        self.año_recepcion.set('')
        self.nivel_educativo.set('')
        self.titulo.set('')
        self.autor.set('')
        self.editorial.set('')
        self.año_edicion.set('')
        self.condicion_libro.set('')
        self.cantidad.set('')
    
    def actualizar_fila(self):
        item_l = self.tabla.focus()
        diccionario_fila = self.tabla.item(item_l)
        id = diccionario_fila['text']
        l_datos = self.bd.mostrar_datos()
        
        for fila in l_datos:
            id_bd = fila[0]
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
                pregunta_box = messagebox.askquestion('Informaciòn', '¿Estas seguro?')
                if remitente and niveleducativo and titulo and condicionlibro and cantidad != '' and pregunta_box == 'yes':
                    self.bd.actualizar_fila(id, remitente, añorecepcion, niveleducativo, titulo, autor, editorial, añoedicion, condicionlibro, cantidad)
                    self.actualizar_tabla()
    
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
        if remitente and niveleducativo and titulo and condicionlibro and cantidad != '':
            self.bd.insertar_fila(remitente, añorecepcion, niveleducativo, titulo, autor, editorial ,añoedicion, condicionlibro, cantidad)
            # falta mejorar
            self.tabla.insert('', "end", values=datos)
            self.limpiar_campos()
        else:
            messagebox.showwarning('error', 'falta rellenar')
    
    def eliminar_datos(self, event):
        self.limpiar_campos()
        l_item = self.tabla.selection()[0]
        diccionario_fila = self.tabla.item(l_item)
        question_box = messagebox.askquestion('Informaciòn', '¿Desea eliminar?')
        if question_box == 'yes':
            self.tabla.delete(l_item)
            self.bd.eliminar_fila(diccionario_fila['text'])
    
    def buscador(self):
        self.limpiar_campos()
        palabra = self.palabra.get()
        columna = self.nombre_columna.get()
        # print(columna)
        # print(palabra)
        l_datos = self.bd.buscador(columna, palabra)
        self.tabla.delete(*self.tabla.get_children())
        i = -1
        for fila in l_datos:
            i = i+1
            self.tabla.insert('', i,text=fila[0], values=fila[1:11])