import tkinter  as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

from conexion_sqlite import Comunicacion

class Widgets3v():
    def __init__(self):
        self.titulo = tk.StringVar()
        self.autor = tk.StringVar()
        self.editorial = tk.StringVar()
        self.aedicion = tk.StringVar()
        self.cantidad = tk.StringVar()
        
        self.usuario = tk.StringVar()
        self.grado = tk.StringVar()
        self.seccion = tk.StringVar()
        self.nivel = tk.StringVar()
        self.cantidad = tk.StringVar()
        self.palabra = tk.StringVar()
        self.palabra2 = tk.StringVar()
        self.nombre_columna = tk.StringVar()
        self.nombre_columna2 = tk.StringVar()
        self.bd = Comunicacion()
        
        
    def widgets(self, frame_cinco, frame_seis):
        #! parte1
        self.seccion_uno(frame_cinco)
        #! parte2
        # lista_atributos2 = []
        lista_metodos2 = []
        self.photo1 = ImageTk.PhotoImage(Image.open("reload.png"))
        self.photo2 = ImageTk.PhotoImage(Image.open("excel.png"))
        
        self.seccion_dos(frame_seis)    
        
    def seccion_uno(self, frame_cinco):
        # print(funciones[0])
        #! TEXTO
        titulo_label = ttk.Label(frame_cinco, textvariable=self.titulo)
        titulo_label.grid(column=0, row=1, padx=5, pady=[10,5], sticky='w')
        autor_label = ttk.Label(frame_cinco, textvariable=self.autor)
        autor_label.grid(column=0, row=2, padx=5, pady=[10,5], sticky='w')
        editorial_label = ttk.Label(frame_cinco, textvariable=self.editorial)
        editorial_label.grid(column=0, row=3, padx=5, pady=[10,5], sticky='w')
        aedicion_label = ttk.Label(frame_cinco, textvariable=self.aedicion)
        aedicion_label.grid(column=0, row=4, padx=5, pady=[10,5], sticky='w')
        cantidad_label = ttk.Label(frame_cinco, text='Cantidad')
        cantidad_label.grid(column=0, row=5, padx=5, pady=[5,10])
        
        ttk.Label(frame_cinco, text='USUARIO').grid(column=0, row=6, padx=5, pady=[5,10])
        
        nombre_label = ttk.Label(frame_cinco, textvariable=self.usuario)
        nombre_label.grid(column=0, row=7, padx=5, pady=[10,5])
        grado_label = ttk.Label(frame_cinco, textvariable=self.grado)
        grado_label.grid(column=0, row=8, padx=5, pady=5)
        seccion_label = ttk.Label(frame_cinco, textvariable=self.seccion)
        seccion_label.grid(column=0, row=9, padx=5, pady=5)
        nivel_label = ttk.Label(frame_cinco, textvariable=self.nivel)
        nivel_label.grid(column=0, row=9, padx=5, pady=5)
        #! ENTRADAS
        
        cantidad_entry = ttk.Entry(frame_cinco, textvariable=self.cantidad)
        cantidad_entry.grid(column=1, row=5, padx=5 ,pady=[5,10])
        #! Botones
        pedido_boton = ttk.Button(frame_cinco, text='Hacer pedido', width=20)#, command=lista_metodos[1])
        pedido_boton.grid(column=0, row=10, padx=5, pady=[5,10])
    
    def seccion_dos(self, frame_seis):
        frame_busqueda1 = ttk.LabelFrame(frame_seis, text='Opciones Libro')
        frame_busqueda1.grid(column=0, row=0, padx=5, pady=5, sticky='ew')
        l_columna = ("Titulo", "Editorial", "Autor")
        buscar_palabra = ttk.Combobox(frame_busqueda1, width=20, value=l_columna, textvariable=self.nombre_columna)
        buscar_palabra.current(0)
        buscar_palabra.grid(column=0, row=0, padx=5, pady=5)
        buscar_palabra.state(["readonly"])
        filtro_libroid = ttk.Entry(frame_busqueda1, textvariable=self.palabra)
        filtro_libroid.grid(column=1, row=0, padx=5 ,pady=1 )
        buscar_boton = ttk.Button(frame_busqueda1, text='buscar', width=20, command=self.buscador2)
        buscar_boton.grid(column=2, row=0, padx=5, pady=5)
        
        #! TABLA
        frame_tabla1 = ttk.LabelFrame(frame_seis, text='Tabla Libros')
        frame_tabla1.grid(column=0, row=1, padx=5, pady=5 ,sticky='nsew')
        frame_tabla1.columnconfigure(1 , weight=10)
        frame_tabla1.rowconfigure(0 , weight=10)
        self.tabla_libro = ttk.Treeview(frame_tabla1)
        self.tabla_libro.grid(column=1, row=0, sticky='nsew',padx=5, pady=5)
        #! SCROLLBARS
        ladox1 = ttk.Scrollbar(frame_tabla1, orient='horizontal', command=self.tabla_libro.xview)
        ladox1.grid(column=1, row=1, sticky='ew', padx=5)
        ladoy1 = ttk.Scrollbar(frame_tabla1, orient='vertical', command=self.tabla_libro.yview)
        ladoy1.grid(column=0, row=0, sticky='ns', pady=5)
        self.tabla_libro.configure(xscrollcommand=ladox1.set, yscrollcommand=ladoy1.set)
        #! COLUMNAS
        self.tabla_libro['columns'] = ('NivelEducativo', 'Titulo', 'Autor', 'Editorial', 'Año Edicion', 'Cantidad')
        self.tabla_libro.column('#0', minwidth=60, width=60, anchor='center')
        self.tabla_libro.column('#1', minwidth=100, width=120, anchor='center')
        self.tabla_libro.column('#2', minwidth=100, width=150, anchor='w')
        self.tabla_libro.column('#3', minwidth=120, width=120, anchor='w')
        self.tabla_libro.column('#4', minwidth=200, width=200, anchor='w')
        self.tabla_libro.column('#5', minwidth=100, width=100, anchor='center')
        self.tabla_libro.column('#6', minwidth=100, width=100, anchor='center')
            
        self.tabla_libro.heading('#0', text='Nº', anchor='center')
        self.tabla_libro.heading('#1', text='Nivel Educativo', anchor='center')
        self.tabla_libro.heading('#2', text='Titulo', anchor='center')
        self.tabla_libro.heading('#3', text='Autor', anchor='center')
        self.tabla_libro.heading('#4', text='Editorial', anchor='center')
        self.tabla_libro.heading('#5', text='Año Edicion', anchor='center')
        self.tabla_libro.heading('#6', text='Cantidad', anchor='center')
        self.tabla_libro.bind("<<TreeviewSelect>>", self.obtener_fila2)
        
        
        frame_busqueda2 = ttk.LabelFrame(frame_seis, text='Opciones Alumno')
        frame_busqueda2.grid(column=0, row=2, padx=5, pady=5, sticky='ew')
        l_columna2 = ("USUARIO", "DNI")
        buscar_palabra = ttk.Combobox(frame_busqueda2, width=20, value=l_columna2, textvariable=self.nombre_columna2)
        buscar_palabra.current(0)
        buscar_palabra.grid(column=0, row=0, padx=5, pady=5)
        buscar_palabra.state(["readonly"])
        filtro_libroid = ttk.Entry(frame_busqueda2, textvariable=self.palabra2)
        filtro_libroid.grid(column=1, row=0, padx=5 ,pady=1 )
        buscar2_boton = ttk.Button(frame_busqueda2, text='buscar', width=20, command=self.buscador3)
        buscar2_boton.grid(column=2, row=0, padx=5, pady=5)

        frame_tabla2 = ttk.LabelFrame(frame_seis, text='Tabla Alumnos')
        frame_tabla2.grid(column=0, row=3, padx=5, pady=5 ,sticky='nsew')
        frame_tabla2.columnconfigure(1 , weight=10)
        frame_tabla2.rowconfigure(0 , weight=10)
        
        self.tabla_alumno = ttk.Treeview(frame_tabla2)
        self.tabla_alumno.grid(column=1, row=0, sticky='nsew',padx=5, pady=5)
        #! SCROLLBARS
        ladox2 = ttk.Scrollbar(frame_tabla2, orient='horizontal', command=self.tabla_alumno.xview)
        ladox2.grid(column=1, row=1, sticky='ew', padx=5)
        ladoy2 = ttk.Scrollbar(frame_tabla2, orient='vertical', command=self.tabla_alumno.yview)
        ladoy2.grid(column=0, row=0, sticky='ns', pady=5)
        self.tabla_alumno.configure(xscrollcommand=ladox2.set, yscrollcommand=ladoy2.set)
        #! COLUMNAS
        self.tabla_alumno['columns'] = ('Nivel', 'Usuario', 'Grado', 'Seccion')
        self.tabla_alumno.column('#0', minwidth=60, width=60, anchor='center')
        self.tabla_alumno.column('#1', minwidth=100, width=100, anchor='center')
        self.tabla_alumno.column('#2', minwidth=150, width=150, anchor='w')
        self.tabla_alumno.column('#3', minwidth=100, width=100, anchor='center')
        self.tabla_alumno.column('#4', minwidth=100, width=100, anchor='center')
            
        self.tabla_alumno.heading('#0', text='Nº', anchor='center')
        self.tabla_alumno.heading('#1', text='Nivel Educativo', anchor='center')
        self.tabla_alumno.heading('#2', text='Usuario', anchor='center')
        self.tabla_alumno.heading('#3', text='Grado', anchor='center')
        self.tabla_alumno.heading('#4', text='Seccion', anchor='center')
        self.tabla_alumno.bind("<<TreeviewSelect>>", self.obtener_fila3)
    
    
    def buscador2(self):
        # self.limpiar_campos()
        palabra = self.palabra.get()
        columna = self.nombre_columna.get()
        l_datos = self.bd.buscador2(columna, palabra)
        self.tabla_libro.delete(*self.tabla_libro.get_children())
        i = -1
        for fila in l_datos:
            i = i+1
            self.tabla_libro.insert('', i,text=fila[0], values=fila[1:11])
    
    def buscador3(self):
        # self.limpiar_campos()
        palabra = self.palabra2.get()
        columna = self.nombre_columna2.get()
        l_datos = self.bd.buscador3(columna, palabra)
        self.tabla_alumno.delete(*self.tabla_alumno.get_children())
        i = -1
        for fila in l_datos:
            i = i+1
            self.tabla_alumno.insert('', i,text=fila[0], values=fila[1:11])
    
    def obtener_fila2(self, event):
        item_selec = self.tabla_libro.focus()
        diccionario_fila = self.tabla_libro.item(item_selec)
        if 'values' in diccionario_fila and len(diccionario_fila['values']) >= 2:
            self.titulo.set(diccionario_fila['values'][1])
            self.autor.set(diccionario_fila['values'][2])
            self.editorial.set(diccionario_fila['values'][3])
            self.aedicion.set(diccionario_fila['values'][4])
        else:
            print('hola')
            
    def obtener_fila3(self, event):
        item_selec = self.tabla_alumno.focus()
        diccionario_fila = self.tabla_alumno.item(item_selec)
        if 'values' in diccionario_fila and len(diccionario_fila['values']) >= 2:
            self.usuario.set(diccionario_fila['values'][1])
            self.grado.set(diccionario_fila['values'][2])
            self.seccion.set(diccionario_fila['values'][3])
            self.nivel.set(diccionario_fila['values'][0])
        else:
            print('hola')