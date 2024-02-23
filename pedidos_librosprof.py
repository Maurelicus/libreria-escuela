import tkinter  as tk
from tkinter import messagebox
import ttkbootstrap as ttk

from PIL import Image, ImageTk
from datetime import date

from conexion_sqlite import Comunicacion

class PedidosLibros():
    def __init__(self):
        self.titulo = tk.StringVar()
        self.autor = tk.StringVar()
        self.editorial = tk.StringVar()
        self.aedicion = tk.StringVar()
        self.categoria = tk.StringVar()
        self.codigo_libro = tk.StringVar()
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
            text='DATOS DEL LIBRO:', 
            bootstyle='danger'
            ).grid(column=0, row=0, padx=30, pady=10, sticky='w', columnspan=2)

        title_label = ttk.Label(frame_datos, text='Titulo:', bootstyle='dark')
        title_label.grid(column=0, row=1, padx=30, pady=5, sticky='w')
        author_label = ttk.Label(frame_datos, text='Autor:', bootstyle='dark')
        author_label.grid(column=0, row=2, padx=30, pady=5, sticky='w')
        editorial_label = ttk.Label(frame_datos, text='Editorial:', bootstyle='dark')
        editorial_label.grid(column=0, row=3, padx=30, pady=5, sticky='w')
        yearedit_label = ttk.Label(frame_datos, text='Año de Edicion:', bootstyle='dark')
        yearedit_label.grid(column=0, row=4, padx=30, pady=5, sticky='w')
        categoria_label = ttk.Label(frame_datos, text='Categoria', bootstyle='dark')
        categoria_label.grid(column=0, row=5, padx=30, pady=5, sticky='we')
        cantidad_label = ttk.Label(frame_datos, text='Cantidad:', bootstyle='dark')
        cantidad_label.grid(column=0, row=6, padx=30, pady=5, sticky='w')
        codigo_label = ttk.Label(frame_datos, text='Codigo:', bootstyle='dark')
        codigo_label.grid(column=0, row=7, padx=30, pady=5, sticky='w')
        
        ttk.Label(frame_datos, text='DATOS DEL USUARIO:', bootstyle='danger').grid(column=0, row=8, 
                padx=30, pady=10, sticky='w', columnspan=2)
        
        name_label = ttk.Label(frame_datos, text='Nombre:', bootstyle='dark')
        name_label.grid(column=0, row=9, padx=30, pady=5, sticky='w')
        number_label = ttk.Label(frame_datos, text='Numero:', bootstyle='dark')
        number_label.grid(column=0, row=10, padx=30, pady=5, sticky='w')
        #! ENTRADAS
        titulo_label = ttk.Label(frame_datos, textvariable=self.titulo, wraplength=160, bootstyle='primary')
        titulo_label.grid(column=1, row=1, padx=5, pady=5, sticky='w')
        autor_label = ttk.Label(frame_datos, textvariable=self.autor, wraplength=160, bootstyle='primary')
        autor_label.grid(column=1, row=2, padx=5, pady=5, sticky='w')
        editorial_label2 = ttk.Label(frame_datos, textvariable=self.editorial, wraplength=160, bootstyle='primary')
        editorial_label2.grid(column=1, row=3, padx=5, pady=5, sticky='w')
        aedicion_label = ttk.Label(frame_datos, textvariable=self.aedicion, wraplength=160, bootstyle='primary')
        aedicion_label.grid(column=1, row=4, padx=5, pady=5, sticky='w')
        category_label = ttk.Label(frame_datos, textvariable=self.categoria, wraplength=160, bootstyle='primary')
        category_label.grid(column=1, row=5, padx=5, pady=5, sticky='w')
        cantidad_entry = ttk.Spinbox(frame_datos, textvariable=self.cantidad, from_=0, to=100,width=5, bootstyle='primary')
        cantidad_entry.state(["readonly"])
        cantidad_entry.grid(column=1, row=6, padx=5 ,pady=5, sticky='w')
        codigo_entry = ttk.Entry(frame_datos, textvariable=self.codigo_libro, width=10, bootstyle='primary')
        codigo_entry.grid(column=1, row=7, padx=5 ,pady=5, sticky='w')

        nombre_label = ttk.Label(frame_datos, textvariable=self.usuario, wraplength=160, bootstyle='primary')
        nombre_label.grid(column=1, row=9, padx=5, pady=5, sticky='w')
        numero_label = ttk.Label(frame_datos, textvariable=self.numero, wraplength=160, bootstyle='primary')
        numero_label.grid(column=1, row=10, padx=5, pady=5, sticky='w')

        #! Botones
        pedido_boton = ttk.Button(frame_datos, text='Hacer Pedido', width=15, command=self.pedido, bootstyle='primary-outline')
        pedido_boton.grid(column=0, row=11, padx=30, pady=[5,10], sticky='w')
    
    def seccion_dos(self, frame_vista):
        buscarbook_frame = ttk.Frame(frame_vista)
        buscarbook_frame.grid(column=0, row=0, padx=5, pady=1, sticky='nsew')
        colu_list = ("Titulo", "Editorial", "Autor","Nivel educativo", "Año de edicion")
        buscarpalabra_combobox = ttk.Combobox(buscarbook_frame, width=15, value=colu_list, 
                                      textvariable=self.nombre_columna, bootstyle='info')
        buscarpalabra_combobox.current(0)
        buscarpalabra_combobox.state(["readonly"])
        buscarpalabra_combobox.pack(side='left', padx=4)

        palabralib_entry = ttk.Entry(buscarbook_frame, textvariable=self.palabra, width=40, bootstyle='info')
        palabralib_entry.pack(side='left', padx=4)

        searchbook = ttk.Button(buscarbook_frame, text='Buscar', width=10, 
                                  command=self.buscar_libro, bootstyle='info')
        searchbook.pack(side='left', padx=4)

        #! TABLA
        tablalibros_frame = ttk.LabelFrame(frame_vista, text='Tabla de Libros', bootstyle='info')
        tablalibros_frame.grid(column=0, row=1, padx=5, pady=[1,5] ,sticky='nsew')
        tablalibros_frame.columnconfigure(1 , weight=10)
        tablalibros_frame.rowconfigure(0 , weight=10)
        
        self.tabla_libro = ttk.Treeview(tablalibros_frame, bootstyle='info')
        self.tabla_libro.grid(column=1, row=0, sticky='nsew',padx=5, pady=5)
        #! SCROLLBARS
        ladox1 = ttk.Scrollbar(tablalibros_frame, orient='horizontal', command=self.tabla_libro.xview, bootstyle='info-round')
        ladox1.grid(column=1, row=1, sticky='ew', padx=5)
        ladoy1 = ttk.Scrollbar(tablalibros_frame, orient='vertical', command=self.tabla_libro.yview, bootstyle='info-round')
        ladoy1.grid(column=0, row=0, sticky='ns', pady=5)
        self.tabla_libro.configure(xscrollcommand=ladox1.set, yscrollcommand=ladoy1.set)
        #! COLUMNAS
        self.tabla_libro['columns'] = ('Titulo','Autor','Editorial','Añoedicion','Categoria','Cantidad','Remitente','Niveleducativo', 'Condicion', 'Añorecepcion')
        self.tabla_libro.column('#0', minwidth=60, width=60, anchor='center')
        self.tabla_libro.column('#1', minwidth=150, width=200, anchor='w')
        self.tabla_libro.column('#2', minwidth=100, width=150, anchor='w')
        self.tabla_libro.column('#3', minwidth=80, width=120, anchor='w')
        self.tabla_libro.column('#4', minwidth=50, width=100, anchor='center')
        self.tabla_libro.column('#5', minwidth=80, width=140, anchor='center')
        self.tabla_libro.column('#6', minwidth=50, width=100, anchor='center')
        self.tabla_libro.column('#7', minwidth=80, width=120, anchor='w')
        self.tabla_libro.column('#8', minwidth=80, width=120, anchor='center')
        self.tabla_libro.column('#9', minwidth=50, width=100, anchor='center')
        self.tabla_libro.column('#10', minwidth=50, width=100, anchor='center')
            
        self.tabla_libro.heading('#0', text='Nº', anchor='center')
        self.tabla_libro.heading('#1', text='Titulo', anchor='center')
        self.tabla_libro.heading('#2', text='Autor', anchor='center')
        self.tabla_libro.heading('#3', text='Editorial', anchor='center')
        self.tabla_libro.heading('#4', text='Año Edicion', anchor='center')
        self.tabla_libro.heading('#5', text='Tipo', anchor='center')
        self.tabla_libro.heading('#6', text='Cantidad', anchor='center')
        self.tabla_libro.heading('#7', text='Remitente', anchor='center')
        self.tabla_libro.heading('#8', text='Nivel Educativo', anchor='center')
        self.tabla_libro.heading('#9', text='Condicion', anchor='center')
        self.tabla_libro.heading('#10', text='Año Recepcion', anchor='center')
        
        # White to Light Purple Color Palette
        self.tabla_libro.tag_configure('Literatura', background='#e6e1f9')
        self.tabla_libro.tag_configure('HyG', background='#d5cdf3')
        self.tabla_libro.tag_configure('C.T.A', background='#cdc2f5')
        self.tabla_libro.tag_configure('Matematica', background='#c6b7fe')
        self.tabla_libro.tag_configure('Fisica', background='#bba8ff')
        
        # pastel blue owo Color Palette
        self.tabla_libro.tag_configure('Biologia', background='#bbeaff')
        self.tabla_libro.tag_configure('Quimica', background='#a9e5ff')
        self.tabla_libro.tag_configure('Economia', background='#98ddfc')
        self.tabla_libro.tag_configure('LyC', background='#84d9ff')
        self.tabla_libro.tag_configure('ComLectora', background='#72d3fe')
        
        # shades of sea green 2 Color Palette
        self.tabla_libro.tag_configure('Idioma', background='#c9f9de')
        self.tabla_libro.tag_configure('P.F.C.C', background='#b8f8d4')
        self.tabla_libro.tag_configure('Computacion', background='#a6f6c9')
        self.tabla_libro.tag_configure('Gastronomia', background='#94f4be')
        self.tabla_libro.tag_configure('Recreacion', background='#83f3b4')

        # OrangeCream1 Color Palette
        self.tabla_libro.tag_configure('AyM', background='#ffedc9')
        self.tabla_libro.tag_configure('Religion', background='#ffe7b6')
        self.tabla_libro.tag_configure('EduFis', background='#ffd276')
        self.tabla_libro.tag_configure('Diccionario', background='#ffbf3c')
        self.tabla_libro.tag_configure('Compendio', background='#fffd8d')
        # kawaii pastel Color Palette
        self.tabla_libro.tag_configure('Manual', background='#f9b428')
        self.tabla_libro.tag_configure('Otros', background='#f2e2ff')
        self.tabla_libro.tag_configure('Falta', background='#fdaaaa')
        self.tabla_libro.tag_configure('Baja', background='#ddfffc')
        self.tabla_libro.tag_configure('Repuesto', background='#d0d3d4')

        self.tabla_libro.bind("<<TreeviewSelect>>", self.obtener_libro)
        
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
    
    def buscar_libro(self):
        self.limpiar_campos()
        palabra = self.palabra.get()
        columna = self.nombre_columna.get()
        self.temp_palabra.set(palabra)
        self.temp_columna.set(columna)

        if columna == "Nivel educativo":
            columna = "NivelEducativo"
        elif columna == "Año de edicion":
            columna = "AñoEdicion"
            
        if palabra != '':
            l_datos = self.bd.search_libros(columna, palabra)
            self.tabla_libro.delete(*self.tabla_libro.get_children())
            i = -1
            for fila in l_datos:
                i = i+1
                if fila[4] != 'Baja' and fila[4] != 'Repuesto' and fila[4] != 'Falta':
                    if fila[4] == 'Historia y Geografia':
                        self.tabla_libro.insert('', i,text=i+1, values=fila[0:11], tags='HyG')
                    elif fila[4] == 'Lenguaje y Comunicacion':
                        self.tabla_libro.insert('', i,text=i+1, values=fila[0:11], tags='LyC')
                    elif fila[4] == 'Comprension Lectora':
                        self.tabla_libro.insert('', i,text=i+1, values=fila[0:11], tags='ComLectora')
                    elif fila[4] == 'Arte y Musica':
                        self.tabla_libro.insert('', i,text=i+1, values=fila[0:11], tags='AyM')
                    elif fila[4] == 'Educacion Fisica':
                        self.tabla_libro.insert('', i,text=i+1, values=fila[0:11], tags='EduFis')
                    elif fila[4] == None:
                        self.tabla_libro.insert('', i,text=i+1, values=fila[0:11], tags='Agregar')
                    else:
                        self.tabla_libro.insert('', i,text=i+1, values=fila[0:11], tags=fila[4])
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
    
    def obtener_libro(self, event):
        item_selec = self.tabla_libro.focus()
        diccionario_fila = self.tabla_libro.item(item_selec)
        if 'values' in diccionario_fila and len(diccionario_fila['values']) != 0:
            self.titulo.set(diccionario_fila['values'][0])
            self.autor.set(diccionario_fila['values'][1])
            self.editorial.set(diccionario_fila['values'][2])
            self.aedicion.set(diccionario_fila['values'][3])
            self.categoria.set(diccionario_fila['values'][4])
            if self.categoria.get() == "Persona, Familia, Comunidad y Civismo":
                self.categoria.set("P.F.C.C")
            elif self.categoria.get() == "Manual para profesores":
                self.categoria.set("Manual")

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
        libro_selec = self.tabla_libro.focus()
        profesor_selec = self.tabla_profesor.focus()
        diccionario_libro = self.tabla_libro.item(libro_selec)
        diccionario_profesor = self.tabla_profesor.item(profesor_selec)
        if len(diccionario_libro['values']) != 0 and len(diccionario_profesor['values']) != 0:
            cantidad_pedida = self.cantidad.get()
            codigo = self.codigo_libro.get()
            if cantidad_pedida > 0 and codigo != '':
                hoy = date.today()
                situacion = 'prestado'
                observacion = 'ninguna'
                tipo = 'libro'
                fecha = ''
                libroid = diccionario_libro['values'][10]
                existentes = diccionario_libro['values'][5]
                
                usuarioid = diccionario_profesor['values'][3]
                cantidad_restante=existentes-cantidad_pedida
                if existentes <= 0:
                    messagebox.showerror('Información', 'No hay existentes')
                elif cantidad_restante >= 0:
                    self.bd.appendpro_pedidolib(codigo, libroid, usuarioid, hoy, fecha,situacion, observacion, cantidad_pedida, tipo)
                    self.bd.update_libro_cantidad(libroid, cantidad_restante)
                    self.palabra.set(self.temp_palabra.get())
                    self.nombre_columna.set(self.temp_columna.get())
                    self.buscar_libro()
                    messagebox.showinfo('Información', 'Pedido Existoso')
                    
                elif cantidad_restante < 0:
                    messagebox.showerror('Información', 'Cantidad excedida al total')
            else:
                messagebox.showerror('Información', 'Falta Rellenar')
        else:
            messagebox.showerror('ERROR', 'Selecciona el profesor y el alumno')
    
    def limpiar_campos(self):
        self.titulo.set('')
        self.autor.set('')
        self.editorial.set('')
        self.aedicion.set('')
        self.categoria.set('')
        self.codigo_libro.set('')
        self.cantidad.set(0)
        self.usuario.set('')
        self.numero.set('')
        
