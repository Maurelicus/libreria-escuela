import tkinter  as tk
from tkinter import messagebox
import ttkbootstrap as ttk

from PIL import Image, ImageTk
from datetime import date

from conexion_sqlite import Comunicacion

class VentanaPedidos():
    def __init__(self):
        self.titulo = tk.StringVar()
        self.autor = tk.StringVar()
        self.editorial = tk.StringVar()
        self.aedicion = tk.StringVar()
        self.codigo_libro = tk.StringVar()
        self.usuario = tk.StringVar()
        self.grado = tk.StringVar()
        self.seccion = tk.StringVar()
        self.nivel = tk.StringVar()
        self.cantidad = tk.IntVar()
        self.palabra = tk.StringVar()
        self.palabra2 = tk.StringVar()
        self.temp_palabra = tk.StringVar()
        self.temp_columna = tk.StringVar()

        self.nombre_columna = tk.StringVar()
        self.nombre_columna2 = tk.StringVar()
        self.bd = Comunicacion()
        # self.photo1 = ImageTk.PhotoImage(Image.open("reload.png"))
        # self.photo2 = ImageTk.PhotoImage(Image.open("excel.png"))

    def seccion_uno(self, frame_cinco):
        #! TEXTO
        t_label = ttk.Label(frame_cinco, text='Titulo:', bootstyle='dark')
        t_label.grid(column=0, row=1, padx=30, pady=[10,5], sticky='w')
        a_label = ttk.Label(frame_cinco, text='Autor:', bootstyle='dark')
        a_label.grid(column=0, row=2, padx=30, pady=5, sticky='w')
        e_label = ttk.Label(frame_cinco, text='Editorial:', bootstyle='dark')
        e_label.grid(column=0, row=3, padx=30, pady=5, sticky='w')
        aed_label = ttk.Label(frame_cinco, text='Año de Edicion:', bootstyle='dark')
        aed_label.grid(column=0, row=4, padx=30, pady=5, sticky='w')
        cantidad_label = ttk.Label(frame_cinco, text='Cantidad:', bootstyle='dark')
        cantidad_label.grid(column=0, row=5, padx=30, pady=5, sticky='w')
        codigo_label = ttk.Label(frame_cinco, text='Codigo:', bootstyle='dark')
        codigo_label.grid(column=0, row=6, padx=30, pady=[5,10], sticky='w')
        
        ttk.Label(frame_cinco, text='DATOS DEL USUARIO:', bootstyle='danger').grid(column=0, row=7, 
                padx=30, pady=10, sticky='w', columnspan=2)
        
        n_label = ttk.Label(frame_cinco, text='Nombre:', bootstyle='dark')
        n_label.grid(column=0, row=8, padx=30, pady=[10,5], sticky='w')
        g_label = ttk.Label(frame_cinco, text='Grado:', bootstyle='dark')
        g_label.grid(column=0, row=9, padx=30, pady=5, sticky='w')
        s_label = ttk.Label(frame_cinco, text='Seccion:', bootstyle='dark')
        s_label.grid(column=0, row=10, padx=30, pady=5, sticky='w')
        ni_label = ttk.Label(frame_cinco, text='Nivel:', bootstyle='dark')
        ni_label.grid(column=0, row=11, padx=30, pady=[5,10], sticky='w')
        #! ENTRADAS
        titulo_label = ttk.Label(frame_cinco, textvariable=self.titulo, wraplength=160, bootstyle='primary')
        titulo_label.grid(column=1, row=1, padx=5, pady=[10,5], sticky='w')
        autor_label = ttk.Label(frame_cinco, textvariable=self.autor, wraplength=160, bootstyle='primary')
        autor_label.grid(column=1, row=2, padx=5, pady=5, sticky='w')
        editorial_label = ttk.Label(frame_cinco, textvariable=self.editorial, wraplength=160, bootstyle='primary')
        editorial_label.grid(column=1, row=3, padx=5, pady=5, sticky='w')
        aedicion_label = ttk.Label(frame_cinco, textvariable=self.aedicion, wraplength=160, bootstyle='primary')
        aedicion_label.grid(column=1, row=4, padx=5, pady=5, sticky='w')
        cantidad_entry = ttk.Spinbox(frame_cinco, textvariable=self.cantidad, from_=0, to=100,width=5, bootstyle='primary')
        cantidad_entry.state(["readonly"])
        cantidad_entry.grid(column=1, row=5, padx=5 ,pady=5, sticky='w')
        codigo_entry = ttk.Entry(frame_cinco, textvariable=self.codigo_libro, width=10, bootstyle='primary')
        codigo_entry.grid(column=1, row=6, padx=5 ,pady=5, sticky='w')
        nombre_label = ttk.Label(frame_cinco, textvariable=self.usuario, wraplength=160, bootstyle='primary')
        nombre_label.grid(column=1, row=8, padx=5, pady=[10,5], sticky='w')
        grado_label = ttk.Label(frame_cinco, textvariable=self.grado, wraplength=160, bootstyle='primary')
        grado_label.grid(column=1, row=9, padx=5, pady=5, sticky='w')
        seccion_label = ttk.Label(frame_cinco, textvariable=self.seccion, wraplength=160, bootstyle='primary')
        seccion_label.grid(column=1, row=10, padx=5, pady=5, sticky='w')
        nivel_label = ttk.Label(frame_cinco, textvariable=self.nivel, wraplength=160, bootstyle='primary')
        nivel_label.grid(column=1, row=11, padx=5, pady=[5,10], sticky='w')
        #! Botones
        pedido_boton = ttk.Button(frame_cinco, text='Hacer Pedido', width=15, command=self.pedido, bootstyle='primary-outline')
        pedido_boton.grid(column=0, row=12, padx=30, pady=[5,10], sticky='w')
    
    def seccion_dos(self, frame_seis):
        frame_busqueda1 = ttk.Frame(frame_seis)
        frame_busqueda1.grid(column=0, row=0, padx=5, pady=[1,5], sticky='nsew')
        l_columna = ("Titulo", "Editorial", "Autor")
        buscar_palabra = ttk.Combobox(frame_busqueda1, width=15, value=l_columna, 
                                      textvariable=self.nombre_columna, bootstyle='info')
        buscar_palabra.current(0)
        buscar_palabra.state(["readonly"])
        buscar_palabra.grid(column=0, row=0, padx=5, pady=5, sticky='nswe')
        filtro_libroid = ttk.Entry(frame_busqueda1, textvariable=self.palabra, width=40, bootstyle='info')
        filtro_libroid.grid(column=1, row=0, padx=5 ,pady=5, sticky='nswe')
        buscar_boton = ttk.Button(frame_busqueda1, text='Buscar', width=10, 
                                  command=self.buscador1, bootstyle='info')
        buscar_boton.grid(column=2, row=0, padx=5, pady=5, sticky='nswe')      
        #! TABLA
        frame_tabla1 = ttk.LabelFrame(frame_seis, text='Tabla Libros', bootstyle='info')
        frame_tabla1.grid(column=0, row=1, padx=5, pady=[1,5] ,sticky='nsew')
        frame_tabla1.columnconfigure(1 , weight=10)
        frame_tabla1.rowconfigure(0 , weight=10)
        self.tabla_libro = ttk.Treeview(frame_tabla1, bootstyle='info')
        self.tabla_libro.grid(column=1, row=0, sticky='nsew',padx=5, pady=5)
        #! SCROLLBARS
        ladox1 = ttk.Scrollbar(frame_tabla1, orient='horizontal', command=self.tabla_libro.xview, bootstyle='info-round')
        ladox1.grid(column=1, row=1, sticky='ew', padx=5)
        ladoy1 = ttk.Scrollbar(frame_tabla1, orient='vertical', command=self.tabla_libro.yview, bootstyle='info-round')
        ladoy1.grid(column=0, row=0, sticky='ns', pady=5)
        self.tabla_libro.configure(xscrollcommand=ladox1.set, yscrollcommand=ladoy1.set)
        #! COLUMNAS
        self.tabla_libro['columns'] = ('NivelEducativo', 'Titulo', 'Autor', 'Editorial', 'Año Edicion', 'Condicion Libro', 'Cantidad')
        self.tabla_libro.column('#0', minwidth=60, width=60, anchor='center')
        self.tabla_libro.column('#1', minwidth=130, width=140, anchor='center')
        self.tabla_libro.column('#2', minwidth=150, width=160, anchor='w')
        self.tabla_libro.column('#3', minwidth=130, width=140, anchor='w')
        self.tabla_libro.column('#4', minwidth=120, width=120, anchor='w')
        self.tabla_libro.column('#5', minwidth=100, width=100, anchor='center')
        self.tabla_libro.column('#6', minwidth=100, width=100, anchor='center')
        self.tabla_libro.column('#7', minwidth=80, width=80, anchor='center')
            
        self.tabla_libro.heading('#0', text='Nº', anchor='center')
        self.tabla_libro.heading('#1', text='Nivel Educativo', anchor='center')
        self.tabla_libro.heading('#2', text='Titulo', anchor='center')
        self.tabla_libro.heading('#3', text='Autor', anchor='center')
        self.tabla_libro.heading('#4', text='Editorial', anchor='center')
        self.tabla_libro.heading('#5', text='Año Edicion', anchor='center')
        self.tabla_libro.heading('#6', text='Condicion Libro', anchor='center')
        self.tabla_libro.heading('#7', text='Cantidad', anchor='center')
        self.tabla_libro.bind("<<TreeviewSelect>>", self.obtener_fila1)
        
        frame_busqueda2 = ttk.Frame(frame_seis)
        frame_busqueda2.grid(column=0, row=2, padx=5, pady=[1,5], sticky='nsew')
        l_columna2 = ("Usuario", "Codigo")
        buscar_palabra = ttk.Combobox(frame_busqueda2, width=15, value=l_columna2, 
                                      textvariable=self.nombre_columna2, bootstyle='info')
        buscar_palabra.current(0)
        buscar_palabra.state(["readonly"])
        buscar_palabra.grid(column=0, row=0, padx=5, pady=5, sticky='nsew')
        filtro_libroid = ttk.Entry(frame_busqueda2, textvariable=self.palabra2, width=40, bootstyle='info')
        filtro_libroid.grid(column=1, row=0, padx=5 ,pady=5, sticky='nsew')
        buscar2_boton = ttk.Button(frame_busqueda2, text='Buscar', width=10, 
                                   command=self.buscador2, bootstyle='info')
        buscar2_boton.grid(column=2, row=0, padx=5, pady=5, sticky='nswe')

        frame_tabla2 = ttk.LabelFrame(frame_seis, text='Tabla Alumnos', bootstyle='info')
        frame_tabla2.grid(column=0, row=3, padx=5, pady=[1,5] ,sticky='nsew')
        frame_tabla2.columnconfigure(1 , weight=10)
        frame_tabla2.rowconfigure(0 , weight=10)
        
        self.tabla_alumno = ttk.Treeview(frame_tabla2, bootstyle='info')
        self.tabla_alumno.grid(column=1, row=0, sticky='nsew',padx=5, pady=5)
        #! SCROLLBARS
        ladox2 = ttk.Scrollbar(frame_tabla2, orient='horizontal', command=self.tabla_alumno.xview, bootstyle='info-round')
        ladox2.grid(column=1, row=1, sticky='ew', padx=5)
        ladoy2 = ttk.Scrollbar(frame_tabla2, orient='vertical', command=self.tabla_alumno.yview, bootstyle='info-round')
        ladoy2.grid(column=0, row=0, sticky='ns', pady=5)
        self.tabla_alumno.configure(xscrollcommand=ladox2.set, yscrollcommand=ladoy2.set)
        #! COLUMNAS
        self.tabla_alumno['columns'] = ('Nivel', 'Usuario', 'Grado', 'Seccion')
        self.tabla_alumno.column('#0', minwidth=80, width=80, anchor='center')
        self.tabla_alumno.column('#1', minwidth=80, width=80, anchor='center')
        self.tabla_alumno.column('#2', minwidth=220, width=230, anchor='w')
        self.tabla_alumno.column('#3', minwidth=80, width=80, anchor='center')
        self.tabla_alumno.column('#4', minwidth=80, width=80, anchor='center')
            
        self.tabla_alumno.heading('#0', text='Codigo del Estudiante', anchor='center')
        self.tabla_alumno.heading('#1', text='Nivel Educativo', anchor='center')
        self.tabla_alumno.heading('#2', text='Usuario', anchor='center')
        self.tabla_alumno.heading('#3', text='Grado', anchor='center')
        self.tabla_alumno.heading('#4', text='Seccion', anchor='center')
        self.tabla_alumno.bind("<<TreeviewSelect>>", self.obtener_fila2)
    
    def buscador1(self):
        self.limpiar_campos()
        palabra = self.palabra.get()
        columna = self.nombre_columna.get()
        self.temp_palabra.set(palabra)
        self.temp_columna.set(columna)
        if palabra != '':
            # l_datos = self.bd.buscar_libromal(columna, palabra)
            l_datos = self.bd.buscar_libros(columna, palabra)
            # print(l2_datos)
            self.tabla_libro.delete(*self.tabla_libro.get_children())
            i = -1
            
            for fila in l_datos:
                i = i+1
                self.tabla_libro.insert('', i,text=i+1, values=fila[2:10])
        else:
            messagebox.showerror('ERROR', 'No se agrego una busqueda')

    
    def buscador2(self):
        self.limpiar_campos2()
        palabra = self.palabra2.get()
        columna = self.nombre_columna2.get()
        if palabra != '':        
            l_datos = self.bd.buscar_usuarios(columna, palabra)
            self.tabla_alumno.delete(*self.tabla_alumno.get_children())
            i = -1
            for fila in l_datos:
                i = i+1
                self.tabla_alumno.insert('', i,text=fila[0], values=fila[1:6])
        else:
            messagebox.showerror('ERROR', 'No se agrego una busqueda')
    
    def obtener_fila1(self, event):
        item_selec = self.tabla_libro.focus()
        diccionario_fila = self.tabla_libro.item(item_selec)
        if 'values' in diccionario_fila and len(diccionario_fila['values']) >= 2:
            self.titulo.set(diccionario_fila['values'][1])
            self.autor.set(diccionario_fila['values'][2])
            self.editorial.set(diccionario_fila['values'][3])
            self.aedicion.set(diccionario_fila['values'][4])
        else:
            self.limpiar_campos()
            
    def obtener_fila2(self, event):
        item_selec = self.tabla_alumno.focus()
        diccionario_fila = self.tabla_alumno.item(item_selec)
        if 'values' in diccionario_fila and len(diccionario_fila['values']) >= 2:
            self.usuario.set(diccionario_fila['values'][1])
            self.grado.set(diccionario_fila['values'][2])
            self.seccion.set(diccionario_fila['values'][3])
            self.nivel.set(diccionario_fila['values'][0])
        else:
            self.limpiar_campos2()
            
    def pedido(self):
        libro_selec = self.tabla_libro.focus()
        diccionario_libro = self.tabla_libro.item(libro_selec)
        alumno_selec = self.tabla_alumno.focus()
        diccionario_alumno = self.tabla_alumno.item(alumno_selec)
        cantidad_pedida = self.cantidad.get()
        codigo = self.codigo_libro.get()
        if cantidad_pedida != '' and codigo != '' and len(diccionario_libro['values']) >= 2 and diccionario_alumno['text'] != '':
            hoy = date.today()
            situacion = 'falta'
            observacion = 'ninguna'
            libroid = diccionario_libro['values'][7]
            existentes = diccionario_libro['values'][6]
            usuarioid = diccionario_alumno['text']
            cantidad_restante=existentes-cantidad_pedida
            #! Me quede aqui
            if existentes == 0:
                messagebox.showerror('Información', 'No hay existentes')
            elif cantidad_restante < 0:
                messagebox.showerror('Información', 'Cantidad excedida al total')
            else:
                self.bd.agregar_libro(codigo, libroid, usuarioid, hoy, situacion, observacion, cantidad_pedida)
                self.bd.update_libro_cantidad(libroid, cantidad_restante)
                self.limpiar_campos()
                self.limpiar_campos2()
                palabra = self.temp_palabra.get()
                columna = self.temp_columna.get()
                l_datos = self.bd.buscar_libromal(columna, palabra)
                self.tabla_libro.delete(*self.tabla_libro.get_children())
                i = -1
                for fila in l_datos:
                    i = i+1
                    self.tabla_libro.insert('', i,text=i+1, values=fila[0:7])
                messagebox.showinfo('Información', 'Pedido Existoso')
        else:
            messagebox.showerror('Información', 'Falta Rellenar')
    
    def limpiar_campos(self):
        self.titulo.set('')
        self.autor.set('')
        self.editorial.set('')
        self.aedicion.set('')

        self.codigo_libro.set('')
        self.cantidad.set(0)

    def limpiar_campos2(self):
        self.codigo_libro.set('')
        self.cantidad.set(0)
        
        self.usuario.set('')
        self.grado.set('')
        self.seccion.set('')
        self.nivel.set('')