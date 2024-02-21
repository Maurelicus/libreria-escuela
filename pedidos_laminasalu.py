import tkinter  as tk
from tkinter import messagebox
import ttkbootstrap as ttk

from PIL import Image, ImageTk
from datetime import date

from conexion_sqlite import Comunicacion

class PedidosLaminas():
    def __init__(self):
        self.titulo = tk.StringVar()
        self.autor = tk.StringVar()
        self.editorial = tk.StringVar()
        self.aedicion = tk.StringVar()
        self.codigo = tk.StringVar()
        self.categoria = tk.StringVar()
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

    def seccion_uno(self, frame_datos):
        #! TEXTO
        ttk.Label(frame_datos, 
            text='DATOS DE LAMINA:', 
            bootstyle='danger'
            ).grid(column=0, row=0, padx=30, pady=10, sticky='w', columnspan=2)

        title_label = ttk.Label(frame_datos, text='Titulo:', bootstyle='dark')
        title_label.grid(column=0, row=1, padx=30, pady=5, sticky='w')
        category_label = ttk.Label(frame_datos, text='Categoria', bootstyle='dark')
        category_label.grid(column=0, row=2, padx=30, pady=5, sticky='we')
        codigo_label = ttk.Label(frame_datos, text='Codigo:', bootstyle='dark')
        codigo_label.grid(column=0, row=3, padx=30, pady=5, sticky='w')
        cantidad_label = ttk.Label(frame_datos, text='Cantidad:', bootstyle='dark')
        cantidad_label.grid(column=0, row=4, padx=30, pady=5, sticky='w')
        
        ttk.Label(frame_datos, text='DATOS DEL USUARIO:', bootstyle='danger').grid(column=0, row=5, 
                padx=30, pady=10, sticky='w', columnspan=2)
        
        name_label = ttk.Label(frame_datos, text='Nombre:', bootstyle='dark')
        name_label.grid(column=0, row=6, padx=30, pady=5, sticky='w')
        grade_label = ttk.Label(frame_datos, text='Grado:', bootstyle='dark')
        grade_label.grid(column=0, row=7, padx=30, pady=5, sticky='w')
        section_label = ttk.Label(frame_datos, text='Seccion:', bootstyle='dark')
        section_label.grid(column=0, row=8, padx=30, pady=5, sticky='w')
        level_label = ttk.Label(frame_datos, text='Nivel:', bootstyle='dark')
        level_label.grid(column=0, row=9, padx=30, pady=5, sticky='w')
        #! ENTRADAS
        titulo_label = ttk.Label(frame_datos, textvariable=self.titulo, wraplength=160, bootstyle='primary')
        titulo_label.grid(column=1, row=1, padx=5, pady=5, sticky='w')
        category_label = ttk.Label(frame_datos, textvariable=self.categoria, wraplength=160, bootstyle='primary')
        category_label.grid(column=1, row=2, padx=5, pady=5, sticky='w')
        codigo_label = ttk.Label(frame_datos, textvariable=self.codigo, width=10, bootstyle='primary')
        codigo_label.grid(column=1, row=3, padx=5 ,pady=5, sticky='w')
        cantidad_entry = ttk.Spinbox(frame_datos, textvariable=self.cantidad, from_=0, to=100, width=5, bootstyle='primary')
        cantidad_entry.state(["readonly"])
        cantidad_entry.grid(column=1, row=4, padx=5 ,pady=5, sticky='w')
        nombre_label = ttk.Label(frame_datos, textvariable=self.usuario, wraplength=160, bootstyle='primary')
        nombre_label.grid(column=1, row=6, padx=5, pady=5, sticky='w')
        grado_label = ttk.Label(frame_datos, textvariable=self.grado, wraplength=160, bootstyle='primary')
        grado_label.grid(column=1, row=7, padx=5, pady=5, sticky='w')
        seccion_label = ttk.Label(frame_datos, textvariable=self.seccion, wraplength=160, bootstyle='primary')
        seccion_label.grid(column=1, row=8, padx=5, pady=5, sticky='w')
        nivel_label = ttk.Label(frame_datos, textvariable=self.nivel, wraplength=160, bootstyle='primary')
        nivel_label.grid(column=1, row=9, padx=5, pady=5, sticky='w')
        #! Botones
        pedido_boton = ttk.Button(frame_datos, text='Hacer Pedido', width=15, command=self.pedido, bootstyle='primary-outline')
        pedido_boton.grid(column=0, row=10, padx=30, pady=[5,10], sticky='w')
    
    def seccion_dos(self, frame_vista):
        buscarlamina_frame = ttk.Frame(frame_vista)
        buscarlamina_frame.grid(column=0, row=0, padx=5, pady=1, sticky='nsew')
        colu_list = ("Titulo", "Nivel educativo", "Año de recepcion")
        buscar_palabra = ttk.Combobox(buscarlamina_frame, width=15, value=colu_list, 
                                      textvariable=self.nombre_columna, bootstyle='info')
        buscar_palabra.current(0)
        buscar_palabra.state(["readonly"])
        buscar_palabra.pack(side='left', padx=4)
        
        palabralam_entry = ttk.Entry(buscarlamina_frame, textvariable=self.palabra, width=40, bootstyle='info')
        palabralam_entry.pack(side='left', padx=4)
        
        buscarlamina_boton = ttk.Button(buscarlamina_frame, text='Buscar', width=10, 
                                  command=self.buscar_lamina, bootstyle='info')
        buscarlamina_boton.pack(side='left', padx=4)

        #! TABLA
        tablalamina_frame = ttk.LabelFrame(frame_vista, text='Tabla de Laminas', bootstyle='info')
        tablalamina_frame.grid(column=0, row=1, padx=5, pady=[1,5] ,sticky='nsew')
        tablalamina_frame.columnconfigure(1 , weight=10)
        tablalamina_frame.rowconfigure(0 , weight=10)
        
        self.tabla_lamina = ttk.Treeview(tablalamina_frame, bootstyle='info')
        self.tabla_lamina.grid(column=1, row=0, sticky='nsew',padx=5, pady=5)
        #! SCROLLBARS
        ladox1 = ttk.Scrollbar(tablalamina_frame, orient='horizontal', command=self.tabla_lamina.xview, bootstyle='info-round')
        ladox1.grid(column=1, row=1, sticky='ew', padx=5)
        ladoy1 = ttk.Scrollbar(tablalamina_frame, orient='vertical', command=self.tabla_lamina.yview, bootstyle='info-round')
        ladoy1.grid(column=0, row=0, sticky='ns', pady=5)
        self.tabla_lamina.configure(xscrollcommand=ladox1.set, yscrollcommand=ladoy1.set)
        #! COLUMNAS
        self.tabla_lamina['columns'] = ('Titulo','Tipo','Codigo', 'Cantidad','Remitente', 'Niveleducativo', 'Condicion','Añorecepcion')
        self.tabla_lamina.column('#0', minwidth=60, width=60, anchor='center')
        self.tabla_lamina.column('#1', minwidth=160, width=240, anchor='w')
        self.tabla_lamina.column('#2', minwidth=100, width=120, anchor='center')
        self.tabla_lamina.column('#3', minwidth=120, width=160, anchor='center')
        self.tabla_lamina.column('#4', minwidth=80, width=100, anchor='center')
        self.tabla_lamina.column('#5', minwidth=100, width=150, anchor='w')
        self.tabla_lamina.column('#6', minwidth=80, width=100, anchor='center')
        self.tabla_lamina.column('#7', minwidth=120, width=150, anchor='center')
        self.tabla_lamina.column('#8', minwidth=100, width=150, anchor='center')
            
        self.tabla_lamina.heading('#0', text='Nº', anchor='center')
        self.tabla_lamina.heading('#1', text='Titulo', anchor='center')
        self.tabla_lamina.heading('#2', text='Tipo', anchor='center')
        self.tabla_lamina.heading('#3', text='Codigo', anchor='center')
        self.tabla_lamina.heading('#4', text='Cantidad', anchor='center')
        self.tabla_lamina.heading('#5', text='Remitente', anchor='center')
        self.tabla_lamina.heading('#6', text='Condicion', anchor='center')
        self.tabla_lamina.heading('#7', text='Nivel educativo', anchor='center')
        self.tabla_lamina.heading('#8', text='Año recepcion', anchor='center')
        
        self.tabla_lamina.tag_configure('Literatura', background='#d4ffea')
        self.tabla_lamina.tag_configure('HyG', background='#bae1ff')
        self.tabla_lamina.tag_configure('CTA', background='#ffffba')
        self.tabla_lamina.tag_configure('Matematica', background='#d5dbdb')
        self.tabla_lamina.tag_configure('Fisica', background='#559e83')
        self.tabla_lamina.tag_configure('Biologia', background='#ae5a41')
        self.tabla_lamina.tag_configure('Quimica', background='#c3cb71')
        self.tabla_lamina.tag_configure('EC', background='#dbdcff')
        self.tabla_lamina.tag_configure('AyC', background='#f8c583')
        self.tabla_lamina.tag_configure('Agregar', background='#608c83')
        self.tabla_lamina.tag_configure('Falta', background='#ffb3ba')
            
        self.tabla_lamina.bind("<<TreeviewSelect>>", self.obtener_lamina)
        #* ALUMNOS
        buscaralumno_frame = ttk.Frame(frame_vista)
        buscaralumno_frame.grid(column=0, row=2, padx=5, pady=[1,5], sticky='nsew')

        col_list = ("Alumno", "Codigo")
        buscar_palabra = ttk.Combobox(buscaralumno_frame, width=15, value=col_list, 
                                      textvariable=self.nombre_columna2, bootstyle='info')
        buscar_palabra.current(0)
        buscar_palabra.state(["readonly"])
        buscar_palabra.pack(side='left', padx=4)

        palabra_entry = ttk.Entry(buscaralumno_frame, textvariable=self.palabra2, width=40, bootstyle='info')
        palabra_entry.pack(side='left', padx=4)

        buscaralumno_boton = ttk.Button(buscaralumno_frame, text='Buscar', width=10, 
                                   command=self.buscar_alumno, bootstyle='info')
        buscaralumno_boton.pack(side='left', padx=4)
        
        #* TABLA
        tablaalumnos_frame = ttk.LabelFrame(frame_vista, text='Tabla Alumnos', bootstyle='info')
        tablaalumnos_frame.grid(column=0, row=3, padx=5, pady=[1,5] ,sticky='nsew')
        tablaalumnos_frame.columnconfigure(1 , weight=10)
        tablaalumnos_frame.rowconfigure(0 , weight=10)
        
        self.tabla_alumno = ttk.Treeview(tablaalumnos_frame, bootstyle='info')
        self.tabla_alumno.grid(column=1, row=0, sticky='nsew',padx=5, pady=5)
        #! SCROLLBARS
        ladox2 = ttk.Scrollbar(tablaalumnos_frame, orient='horizontal', command=self.tabla_alumno.xview, bootstyle='info-round')
        ladox2.grid(column=1, row=1, sticky='ew', padx=5)
        ladoy2 = ttk.Scrollbar(tablaalumnos_frame, orient='vertical', command=self.tabla_alumno.yview, bootstyle='info-round')
        ladoy2.grid(column=0, row=0, sticky='ns', pady=5)
        self.tabla_alumno.configure(xscrollcommand=ladox2.set, yscrollcommand=ladoy2.set)
        #! COLUMNAS
        self.tabla_alumno['columns'] = ('Alumno', 'Sexo', 'Nivel', 'Grado', 'Seccion', 'Codigo')
        self.tabla_alumno.column('#0', minwidth=60, width=60, anchor='center')
        self.tabla_alumno.column('#1', minwidth=200, width=250, anchor='w')
        self.tabla_alumno.column('#2', minwidth=90, width=100, anchor='center')
        self.tabla_alumno.column('#3', minwidth=100, width=100, anchor='center')
        self.tabla_alumno.column('#4', minwidth=100, width=100, anchor='center')
        self.tabla_alumno.column('#5', minwidth=100, width=100, anchor='center')
        self.tabla_alumno.column('#6', minwidth=100, width=120, anchor='w')

        self.tabla_alumno.heading('#0', text='Nº', anchor='center')
        self.tabla_alumno.heading('#1', text='Alumno', anchor='center')
        self.tabla_alumno.heading('#2', text='Sexo', anchor='center')
        self.tabla_alumno.heading('#3', text='Nivel', anchor='center')
        self.tabla_alumno.heading('#4', text='Grado', anchor='center')
        self.tabla_alumno.heading('#5', text='Seccion', anchor='center')
        self.tabla_alumno.heading('#6', text='Codigo', anchor='center')

        self.tabla_alumno.bind("<<TreeviewSelect>>", self.obtener_alumno)

    def buscar_lamina(self):
        self.limpiar_campos()
        palabra = self.palabra.get()
        columna = self.nombre_columna.get()

        if columna == "Año de recepcion":
            columna = "AñoRecepcion"
        elif columna == "Nivel educativo":
            columna = "NivelEducativo"

        if palabra != '':
            l_datos = self.bd.search_laminas(columna, palabra)
            self.tabla_lamina.delete(*self.tabla_lamina.get_children())
            i = -1
            for fila in l_datos:
                i = i+1
                if fila[1] == 'Historia y Geografia':
                    self.tabla_lamina.insert('', i,text=i+1, values=fila[0:9], tags='HyG')
                elif fila[1] == 'C.T.A':
                    self.tabla_lamina.insert('', i,text=i+1, values=fila[0:9], tags='CTA')
                elif fila[1] == 'Educacion Civica':
                    self.tabla_lamina.insert('', i,text=i+1, values=fila[0:9], tags='EC')
                elif fila[1] == 'Arte y Cultura':
                    self.tabla_lamina.insert('', i,text=i+1, values=fila[0:9], tags='AyC')
                elif fila[1] == None:
                    self.tabla_lamina.insert('', i,text=i+1, values=fila[0:9], tags='Agregar')
                else:
                    self.tabla_lamina.insert('', i,text=i+1, values=fila[0:9], tags=fila[1])

        else:
            messagebox.showerror('ERROR', 'No se agrego una busqueda')
    
    def buscar_alumno(self):
        self.limpiar_campos()
        palabra = self.palabra2.get()
        columna = self.nombre_columna2.get()
        if palabra != '':        
            l_datos = self.bd.search_alumnos(columna, palabra)
            self.tabla_alumno.delete(*self.tabla_alumno.get_children())
            i = -1
            for fila in l_datos:
                i = i+1
                self.tabla_alumno.insert('', i,text=i+1, values=fila[0:7], tags=fila[6])

        else:
            messagebox.showerror('ERROR', 'No se agrego una busqueda')
    
    def obtener_lamina(self, event):
        item_selec = self.tabla_lamina.focus()
        diccionario_fila = self.tabla_lamina.item(item_selec)
        if 'values' in diccionario_fila and len(diccionario_fila['values']) >= 2:
            self.titulo.set(diccionario_fila['values'][0])
            self.categoria.set(diccionario_fila['values'][1])
            self.codigo.set(diccionario_fila['values'][2])
        else:
            self.limpiar_campos()
            
    def obtener_alumno(self, event):
        item_selec = self.tabla_alumno.focus()
        diccionario_fila = self.tabla_alumno.item(item_selec)
        if 'values' in diccionario_fila and len(diccionario_fila['values']) != 0:
            self.usuario.set(diccionario_fila['values'][0])
            self.nivel.set(diccionario_fila['values'][2])
            self.grado.set(diccionario_fila['values'][3])
            self.seccion.set(diccionario_fila['values'][4])
        else:
            self.limpiar_campos()
    
    def pedido(self):
        lamina_selec = self.tabla_lamina.focus()
        alumno_selec = self.tabla_alumno.focus()
        diccionario_lamina = self.tabla_lamina.item(lamina_selec)
        diccionario_alumno = self.tabla_alumno.item(alumno_selec)
        cantidad_pedida = self.cantidad.get()
        if cantidad_pedida > 0 and len(diccionario_lamina['values']) != 0 and len(diccionario_alumno['values']) != 0:
            hoy = date.today()
            situacion = 'prestado'
            observacion = 'ninguna'
            tipo = 'lamina'
            fecha = ''
            laminaid = diccionario_lamina['values'][8]
            existentes = diccionario_lamina['values'][3]
            
            usuarioid = diccionario_alumno['values'][5]
            cantidad_restante=existentes-cantidad_pedida
            if existentes <= 0:
                messagebox.showerror('Información', 'No hay existentes')
            elif cantidad_restante >=0:
                self.bd.append_pedidolam(laminaid, usuarioid, hoy, fecha,situacion, observacion, cantidad_pedida, tipo)
                self.bd.update_lamina_cantidad(laminaid, cantidad_restante)
                self.limpiar_campos()
                palabra = self.palabra.get()
                columna = self.nombre_columna.get()
                l_datos = self.bd.search_laminas(columna, palabra)
                self.tabla_lamina.delete(*self.tabla_lamina.get_children())
                i = -1
                for fila in l_datos:
                    i = i+1
                    if fila[1] == 'Historia y Geografia':
                        self.tabla_lamina.insert('', i,text=i+1, values=fila[0:9], tags='HyG')
                    elif fila[1] == 'C.T.A':
                        self.tabla_lamina.insert('', i,text=i+1, values=fila[0:9], tags='CTA')
                    elif fila[1] == 'Educacion Civica':
                        self.tabla_lamina.insert('', i,text=i+1, values=fila[0:9], tags='EC')
                    elif fila[1] == 'Arte y Cultura':
                        self.tabla_lamina.insert('', i,text=i+1, values=fila[0:9], tags='AyC')
                    elif fila[1] == None:
                        self.tabla_lamina.insert('', i,text=i+1, values=fila[0:9], tags='Agregar')
                    else:
                        self.tabla_lamina.insert('', i,text=i+1, values=fila[0:9], tags=fila[1])
                messagebox.showinfo('Información', 'Pedido Existoso')
            elif cantidad_restante < 0:
                messagebox.showerror('Información', 'Cantidad excedida al total')
        else:
            messagebox.showerror('Información', 'Falta Rellenar')
    
    def limpiar_campos(self):
        self.titulo.set('')
        self.categoria.set('')
        self.codigo.set('')
        self.cantidad.set(0)
        self.usuario.set('')
        self.grado.set('')
        self.seccion.set('')
        self.nivel.set('')
