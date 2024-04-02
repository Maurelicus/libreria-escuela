from tkinter import messagebox
from datetime import date
import ttkbootstrap as ttk
import tkinter  as tk

from data.conexion_sqlite import Comunicacion

class PedidosLaminas():
    def __init__(self):
        self.titulo = tk.StringVar()
        self.codigo = tk.StringVar()
        self.categoria = tk.StringVar()
        self.usuario = tk.StringVar()
        self.numero = tk.StringVar()
        self.cantidad = tk.IntVar()
        self.palabra = tk.StringVar()
        self.palabra2 = tk.StringVar()
        self.nombre_columna = tk.StringVar()
        self.nombre_columna2 = tk.StringVar()
        self.temp_palabra = tk.StringVar()
        self.temp_columna = tk.StringVar()
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
        code_label = ttk.Label(frame_datos, text='Codigo:', bootstyle='dark')
        code_label.grid(column=0, row=3, padx=30, pady=5, sticky='w')
        total_label = ttk.Label(frame_datos, text='Cantidad:', bootstyle='dark')
        total_label.grid(column=0, row=4, padx=30, pady=5, sticky='w')
        
        ttk.Label(frame_datos, text='DATOS DEL USUARIO:', bootstyle='danger').grid(column=0, row=5, 
                padx=30, pady=10, sticky='w', columnspan=2)
        
        name_label = ttk.Label(frame_datos, text='Nombre:', bootstyle='dark')
        name_label.grid(column=0, row=6, padx=30, pady=5, sticky='w')
        number_label = ttk.Label(frame_datos, text='Numero:', bootstyle='dark')
        number_label.grid(column=0, row=7, padx=30, pady=5, sticky='w')
        #! ENTRADAS
        titulo_label = ttk.Label(frame_datos, textvariable=self.titulo, wraplength=160, bootstyle='primary')
        titulo_label.grid(column=1, row=1, padx=5, pady=5, sticky='w')
        categoria_label = ttk.Label(frame_datos, textvariable=self.categoria, wraplength=160, bootstyle='primary')
        categoria_label.grid(column=1, row=2, padx=5, pady=5, sticky='w')
        codigo_label = ttk.Label(frame_datos, textvariable=self.codigo, width=10, bootstyle='primary')
        codigo_label.grid(column=1, row=3, padx=5 ,pady=5, sticky='w')
        cantidad_entry = ttk.Spinbox(frame_datos, textvariable=self.cantidad, from_=0, to=100, width=5, bootstyle='primary')
        cantidad_entry.state(["readonly"])
        cantidad_entry.grid(column=1, row=4, padx=5 ,pady=5, sticky='w')

        nombre_label = ttk.Label(frame_datos, textvariable=self.usuario, wraplength=160, bootstyle='primary')
        nombre_label.grid(column=1, row=6, padx=5, pady=5, sticky='w')
        numero_label = ttk.Label(frame_datos, textvariable=self.numero, wraplength=160, bootstyle='primary')
        numero_label.grid(column=1, row=7, padx=5, pady=5, sticky='w')
        #! Botones
        pedido_boton = ttk.Button(frame_datos, text='Hacer Pedido', width=15, command=self.pedido, bootstyle='primary-outline')
        pedido_boton.grid(column=0, row=8, padx=30, pady=[5,10], sticky='w', columnspan=2)
    
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
        
        # White to Light Purple Color Palette
        self.tabla_lamina.tag_configure('Literatura', background='#e6e1f9')
        self.tabla_lamina.tag_configure('HyG', background='#d5cdf3')
        self.tabla_lamina.tag_configure('C.T.A', background='#cdc2f5')
        self.tabla_lamina.tag_configure('Matematica', background='#c6b7fe')
        self.tabla_lamina.tag_configure('Fisica', background='#bba8ff')
        
        # pastel blue owo Color Palette
        self.tabla_lamina.tag_configure('Biologia', background='#bbeaff')
        self.tabla_lamina.tag_configure('Quimica', background='#a9e5ff')
        self.tabla_lamina.tag_configure('Economia', background='#98ddfc')
        self.tabla_lamina.tag_configure('LyC', background='#84d9ff')
        self.tabla_lamina.tag_configure('ComLectora', background='#72d3fe')
        
        # shades of sea green 2 Color Palette
        self.tabla_lamina.tag_configure('Idioma', background='#c9f9de')
        self.tabla_lamina.tag_configure('P.F.C.C', background='#b8f8d4')
        self.tabla_lamina.tag_configure('Computacion', background='#a6f6c9')
        self.tabla_lamina.tag_configure('Gastronomia', background='#94f4be')
        self.tabla_lamina.tag_configure('Recreacion', background='#83f3b4')

        # OrangeCream1 Color Palette
        self.tabla_lamina.tag_configure('AyM', background='#ffedc9')
        self.tabla_lamina.tag_configure('Religion', background='#ffe7b6')
        self.tabla_lamina.tag_configure('EduFis', background='#ffd276')
        self.tabla_lamina.tag_configure('Diccionario', background='#ffbf3c')
        self.tabla_lamina.tag_configure('Compendio', background='#fffd8d')
        # kawaii pastel Color Palette
        self.tabla_lamina.tag_configure('Manual', background='#f9b428')
        self.tabla_lamina.tag_configure('Otros', background='#f2e2ff')
        self.tabla_lamina.tag_configure('Falta', background='#fdaaaa')
        self.tabla_lamina.tag_configure('Baja', background='#ddfffc')
        self.tabla_lamina.tag_configure('Repuesto', background='#d0d3d4')

        self.tabla_lamina.bind("<<TreeviewSelect>>", self.obtener_lamina)
        #* PROFESOR
        buscarprofesor_frame = ttk.Frame(frame_vista)
        buscarprofesor_frame.grid(column=0, row=2, padx=5, pady=[1,5], sticky='nsew')

        col_list = ("Profesor", "Codigo")
        buscar_palabra = ttk.Combobox(buscarprofesor_frame, width=15, value=col_list, 
                                      textvariable=self.nombre_columna2, bootstyle='info')
        buscar_palabra.current(0)
        buscar_palabra.state(["readonly"])
        buscar_palabra.pack(side='left', padx=4)

        palabra_entry = ttk.Entry(buscarprofesor_frame, textvariable=self.palabra2, width=40, bootstyle='info')
        palabra_entry.pack(side='left', padx=4)

        buscarprofesor_boton = ttk.Button(buscarprofesor_frame, text='Buscar', width=10, 
                                   command=self.buscar_profesor, bootstyle='info')
        buscarprofesor_boton.pack(side='left', padx=4)

        #! TABLA
        tablaprofesores_frame = ttk.LabelFrame(frame_vista, text='Tabla Profesores', bootstyle='info')
        tablaprofesores_frame.grid(column=0, row=3, padx=5, pady=[1,5] ,sticky='nsew')
        tablaprofesores_frame.columnconfigure(1 , weight=10)
        tablaprofesores_frame.rowconfigure(0 , weight=10)
        
        self.tabla_profesor = ttk.Treeview(tablaprofesores_frame, bootstyle='info')
        self.tabla_profesor.grid(column=1, row=0, sticky='nsew',padx=5, pady=5)
        #! SCROLLBARS
        ladox2 = ttk.Scrollbar(tablaprofesores_frame, orient='horizontal', command=self.tabla_profesor.xview, bootstyle='info-round')
        ladox2.grid(column=1, row=1, sticky='ew', padx=5)
        ladoy2 = ttk.Scrollbar(tablaprofesores_frame, orient='vertical', command=self.tabla_profesor.yview, bootstyle='info-round')
        ladoy2.grid(column=0, row=0, sticky='ns', pady=5)
        self.tabla_profesor.configure(xscrollcommand=ladox2.set, yscrollcommand=ladoy2.set)
        #! COLUMNAS
        self.tabla_profesor['columns'] = ('Profesor', 'Correo', 'Celular', 'Codigo')
        self.tabla_profesor.column('#0', minwidth=60, width=60, anchor='center')
        self.tabla_profesor.column('#1', minwidth=200, width=250, anchor='w')
        self.tabla_profesor.column('#2', minwidth=200, width=250, anchor='w')
        self.tabla_profesor.column('#3', minwidth=120, width=150, anchor='w')
        self.tabla_profesor.column('#4', minwidth=100, width=120, anchor='w')

        self.tabla_profesor.heading('#0', text='Nº', anchor='center')
        self.tabla_profesor.heading('#1', text='Profesor', anchor='center')
        self.tabla_profesor.heading('#2', text='Correo', anchor='center')
        self.tabla_profesor.heading('#3', text='Celular', anchor='center')
        self.tabla_profesor.heading('#4', text='Codigo', anchor='center')

        self.tabla_profesor.bind("<<TreeviewSelect>>", self.obtener_profesor)

    def buscar_lamina(self):
        self.limpiar_campos()
        palabra = self.palabra.get()
        columna = self.nombre_columna.get()
        self.temp_palabra.set(palabra)
        self.temp_columna.set(columna)

        if columna == "Año de recepcion":
            columna = "AñoRecepcion"
        elif columna == "Nivel educativo":
            columna = "NivelEducativo"
        elif columna == "Condicion de la Lamina":
            columna = "CondicionLamina"

        if palabra != '':
            l_datos = self.bd.search_laminas(columna, palabra)
            self.tabla_lamina.delete(*self.tabla_lamina.get_children())
            i = -1
            for fila in l_datos:
                i = i+1
                if fila[1] != 'Baja' and fila[1] != 'Repuesto' and fila[1] != 'Falta':
                    if fila[1] == 'Historia y Geografia':
                        self.tabla_lamina.insert('', i,text=i+1, values=fila[0:9], tags='HyG')
                    elif fila[1] == 'Lenguaje y Comunicacion':
                        self.tabla_lamina.insert('', i,text=i+1, values=fila[0:9], tags='LyC')
                    elif fila[1] == 'Comprension Lectora':
                        self.tabla_lamina.insert('', i,text=i+1, values=fila[0:9], tags='ComLectora')
                    elif fila[1] == 'Arte y Cultura':
                        self.tabla_lamina.insert('', i,text=i+1, values=fila[0:9], tags='AyM')
                    elif fila[1] == 'Educacion Fisica':
                        self.tabla_lamina.insert('', i,text=i+1, values=fila[0:9], tags='EduFis')
                    elif fila[1] == None:
                        self.tabla_lamina.insert('', i,text=i+1, values=fila[0:9], tags='Agregar')
                    else:
                        self.tabla_lamina.insert('', i,text=i+1, values=fila[0:9], tags=fila[1])
        else:
            messagebox.showerror('ERROR', 'No se agrego una busqueda')
    
    def buscar_profesor(self):
        self.limpiar_campos()
        palabra = self.palabra2.get()
        columna = self.nombre_columna2.get()
        if palabra != '':        
            l_datos = self.bd.search_profesores(columna, palabra)
            self.tabla_profesor.delete(*self.tabla_profesor.get_children())
            i = -1
            for fila in l_datos:
                i = i+1
                self.tabla_profesor.insert('', i,text=i+1, values=fila[0:5], tags=fila[4])
        else:
            messagebox.showerror('ERROR', 'No se agrego una busqueda')
    
    def obtener_lamina(self, event):
        item_selec = self.tabla_lamina.focus()
        diccionario_fila = self.tabla_lamina.item(item_selec)
        if 'values' in diccionario_fila and len(diccionario_fila['values']) >= 2:
            self.titulo.set(diccionario_fila['values'][0])
            self.categoria.set(diccionario_fila['values'][1])
            if self.categoria.get() == "Persona, Familia, Comunidad y Civismo":
                self.categoria.set("P.F.C.C")
            elif self.categoria.get() == "Manual para profesores":
                self.categoria.set("Manual")
            self.codigo.set(diccionario_fila['values'][2])
        else:
            self.limpiar_campos()
            
    def obtener_profesor(self, event):
        item_selec = self.tabla_profesor.focus()
        diccionario_fila = self.tabla_profesor.item(item_selec)
        if 'values' in diccionario_fila and len(diccionario_fila['values']) != 0:
            self.usuario.set(diccionario_fila['values'][0])
            self.numero.set(diccionario_fila['values'][2])
        else:
            self.limpiar_campos()
    
    def pedido(self):
        lamina_selec = self.tabla_lamina.focus()
        alumno_selec = self.tabla_profesor.focus()
        diccionario_lamina = self.tabla_lamina.item(lamina_selec)
        diccionario_profesor = self.tabla_profesor.item(alumno_selec)
        if len(diccionario_lamina['values']) != 0 and len(diccionario_profesor['values']) != 0:        
            cantidad_pedida = self.cantidad.get()

            if cantidad_pedida > 0:
                hoy = date.today()
                situacion = 'prestado'
                observacion = 'ninguna'
                tipo = 'lamina'
                fecha = ''
                laminaid = diccionario_lamina['values'][8]
                existentes = diccionario_lamina['values'][3]
                
                usuarioid = diccionario_profesor['values'][3]
                cantidad_restante=existentes-cantidad_pedida
                if existentes <= 0:
                    messagebox.showerror('Información', 'No hay existentes')
                elif cantidad_restante >=0:
                    self.bd.appendpro_pedidolam(laminaid, usuarioid, hoy, fecha,situacion, observacion, cantidad_pedida, tipo)
                    self.bd.update_lamina_cantidad(laminaid, cantidad_restante)
                    self.palabra.set(self.temp_palabra.get())
                    self.nombre_columna.set(self.temp_columna.get())
                    self.buscar_lamina()
                    messagebox.showinfo('Información', 'Pedido Existoso')
                    
                elif cantidad_restante < 0:
                    messagebox.showerror('Información', 'Cantidad excedida al total')
            else:
                messagebox.showerror('Información', 'Falta Rellenar')
        else:
            messagebox.showerror('ERROR', 'Selecciona el profesor y el alumno')

    def limpiar_campos(self):
        self.titulo.set('')
        self.categoria.set('')
        self.codigo.set('')
        self.cantidad.set(0)
        self.usuario.set('')
        self.numero.set('')
