from PIL import Image, ImageTk
from tkinter import messagebox
import tkinter  as tk
import ttkbootstrap as ttk

from data.conexion_sqlite import Comunicacion
from data.informes import Informes

class VentanaLibros():
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
        niv_list = ["Primaria", "Secundaria"]
        con_list = ["A", "B", "C"]
        cat_list = [
            "Literatura","Historia y Geografia","C.T.A","Matematica",
            "Fisica","Biologia","Quimica","Economia","Lenguaje y Comunicacion",
            "Comprension Lectora","Idioma","P.F.C.C","Computacion",
            "Gastronomia","Recreacion","Arte y Musica","Religion",
            "Educacion Fisica","Diccionario","Compendio","Manual","Otros","Falta"
            ]
        a = 1
        for categ in cat_list:
            self.cat_dic[categ] = a
            a = a+1
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
        añoedicion_label = ttk.Label(frame_datos, text='Año de edicion', bootstyle='dark')
        añoedicion_label.grid(column=0, row=5, padx=30, pady=5, sticky='we')
        categoria_label = ttk.Label(frame_datos, text='Categoria', bootstyle='dark')
        categoria_label.grid(column=0, row=6, padx=30, pady=[5,10], sticky='we')
        cantidad_label = ttk.Label(frame_datos, text='Cantidad', bootstyle='dark')
        cantidad_label.grid(column=0, row=7, padx=30, pady=5, sticky='we')

        ttk.Label(frame_datos, 
            text='OTROS DATOS:', 
            bootstyle='danger'
            ).grid(column=0, row=8, padx=30, pady=10, sticky='w', columnspan=2)

        reminente_label = ttk.Label(frame_datos, text='Remitente', bootstyle='dark') 
        reminente_label.grid(column=0, row=9, padx=30, pady=5, sticky='we')
        niveleducativo_label = ttk.Label(frame_datos, text='Nivel Educativo', bootstyle='dark')
        niveleducativo_label.grid(column=0, row=10, padx=30, pady=5, sticky='we')
        condicionlibro_label = ttk.Label(frame_datos, text='Condicion', bootstyle='dark')
        condicionlibro_label.grid(column=0, row=11, padx=30, pady=5, sticky='we')
        añorecepcion_label = ttk.Label(frame_datos, text='Año de Recepcion', bootstyle='dark')
        añorecepcion_label.grid(column=0, row=12, padx=30, pady=5, sticky='we')
        #! ENTRADAS
        titulo_entry = ttk.Entry(frame_datos, textvariable=self.titulo, width=20, bootstyle='primary')
        titulo_entry.grid(column=1, row=2, padx=5 ,pady=5, sticky='w')
        autor_entry = ttk.Entry(frame_datos, textvariable=self.autor, width=20, bootstyle='primary')
        autor_entry.grid(column=1, row=3, padx=5 ,pady=5, sticky='w')
        editorial_entry = ttk.Entry(frame_datos, textvariable=self.editorial, bootstyle='primary')
        editorial_entry.grid(column=1, row=4, padx=5 ,pady=5, sticky='w')
        añoedicion_entry = ttk.Entry(frame_datos, textvariable=self.año_edicion, width=7, bootstyle='primary')
        añoedicion_entry.grid(column=1, row=5, padx=5 ,pady=5, sticky='w')
        categoria_combobox = ttk.Combobox(frame_datos, textvariable=self.categoria,value=cat_list, width=20, bootstyle='primary')
        categoria_combobox.state(["readonly"])
        categoria_combobox.current(0)
        categoria_combobox.grid(column=1, row=6, padx=5 ,pady=5, sticky='w')
        cantidad_entry = ttk.Spinbox(frame_datos, textvariable=self.cantidad, from_=0, to=100, width=5, bootstyle='primary')
        cantidad_entry.state(["readonly"])
        cantidad_entry.grid(column=1, row=7, padx=5 ,pady=5, sticky='w')

        reminente_entry = ttk.Entry(frame_datos, textvariable=self.remitente, width=10, bootstyle='primary')
        reminente_entry.grid(column=1, row=9, padx=5 ,pady=5, sticky='w')
        niveleducativo_combobox = ttk.Combobox(frame_datos, textvariable=self.nivel_educativo ,value=niv_list, width=10, bootstyle='primary')
        niveleducativo_combobox.current(0)
        niveleducativo_combobox.state(["readonly"])
        niveleducativo_combobox.grid(column=1, row=10, padx=5 ,pady=5, sticky='w')
        condicionlibro_combobox = ttk.Combobox(frame_datos, textvariable=self.condicion_libro ,value=con_list, width=2, bootstyle='primary')
        condicionlibro_combobox.grid(column=1, row=11, padx=5 ,pady=5, sticky='w')
        condicionlibro_combobox.current(0)
        condicionlibro_combobox.state(["readonly"])
        añorecepcion_entry = ttk.Entry(frame_datos, textvariable=self.año_recepcion, width=7, bootstyle='primary')
        añorecepcion_entry.grid(column=1, row=12, padx=5 ,pady=5, sticky='w')
        #! Botones
        update_boton = ttk.Button(frame_datos, text='Modificar Libro', width=15, command=self.actualizar_libro, bootstyle='primary-outline')
        update_boton.grid(column=0, row=13, padx=20, pady=10, sticky='w')
        clear_boton = ttk.Button(frame_datos, text='Limpiar Campos', width=15, command=self.limpiar_campos, bootstyle='primary-outline')
        clear_boton.grid(column=1, row=13, padx=5, pady=10, sticky='w')
        add_boton = ttk.Button(frame_datos, text='Añadir Libro', width=15, command=self.agregar_libro, bootstyle='primary-outline')
        add_boton.grid(column=0, row=14, padx=20, pady=10, sticky='w')
        baja_boton = ttk.Button(frame_datos, text='Dar de Baja', width=15, command=self.dar_baja, bootstyle='primary-outline')
        baja_boton.grid(column=1, row=14, padx=5, pady=10, sticky='w')
    
    def seccion_dos(self, frame_vista):
        busqueda_frame = ttk.Frame(frame_vista)
        busqueda_frame.grid(column=0, row=0, padx=5, pady=1, sticky='nsew')

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
                                command=self.guardar_libros, bootstyle='success-link')
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
        # White to Light Purple Color Palette
        self.tabla.tag_configure('Literatura', background='#e6e1f9')
        self.tabla.tag_configure('HyG', background='#d5cdf3')
        self.tabla.tag_configure('C.T.A', background='#cdc2f5')
        self.tabla.tag_configure('Matematica', background='#c6b7fe')
        self.tabla.tag_configure('Fisica', background='#bba8ff')
        
        # pastel blue owo Color Palette
        self.tabla.tag_configure('Biologia', background='#bbeaff')
        self.tabla.tag_configure('Quimica', background='#a9e5ff')
        self.tabla.tag_configure('Economia', background='#98ddfc')
        self.tabla.tag_configure('LyC', background='#84d9ff')
        self.tabla.tag_configure('ComLectora', background='#72d3fe')
        
        # shades of sea green 2 Color Palette
        self.tabla.tag_configure('Idioma', background='#c9f9de')
        self.tabla.tag_configure('P.F.C.C', background='#b8f8d4')
        self.tabla.tag_configure('Computacion', background='#a6f6c9')
        self.tabla.tag_configure('Gastronomia', background='#94f4be')
        self.tabla.tag_configure('Recreacion', background='#83f3b4')

        # OrangeCream1 Color Palette
        self.tabla.tag_configure('AyM', background='#ffedc9')
        self.tabla.tag_configure('Religion', background='#ffe7b6')
        self.tabla.tag_configure('EduFis', background='#ffd276')
        self.tabla.tag_configure('Diccionario', background='#ffbf3c')
        self.tabla.tag_configure('Compendio', background='#fffd8d')
        # kawaii pastel Color Palette
        self.tabla.tag_configure('Manual', background='#f9b428')
        self.tabla.tag_configure('Otros', background='#f2e2ff')
        self.tabla.tag_configure('Falta', background='#fdaaaa')
        self.tabla.tag_configure('Baja', background='#ddfffc')
        self.tabla.tag_configure('Repuesto', background='#d0d3d4')
        
        self.tabla.bind("<<TreeviewSelect>>", self.obtener_libro)
        self.tabla.bind("<Double-1>", self.eliminar_libro)
        
    def mostrar_libros(self):
        self.limpiar_campos()
        self.tabla.delete(*self.tabla.get_children())
        l_datos = self.bd.show_libros()
        i = -1
        for fila in l_datos:
            i = i+1
            if fila[4] != 'Baja':
                if fila[4] == 'Historia y Geografia':
                    self.tabla.insert('', i,text=i+1, values=fila[0:11], tags='HyG')
                elif fila[4] == 'Lenguaje y Comunicacion':
                    self.tabla.insert('', i,text=i+1, values=fila[0:11], tags='LyC')
                elif fila[4] == 'Comprension Lectora':
                    self.tabla.insert('', i,text=i+1, values=fila[0:11], tags='ComLectora')
                elif fila[4] == 'Arte y Musica':
                    self.tabla.insert('', i,text=i+1, values=fila[0:11], tags='AyM')
                elif fila[4] == 'Educacion Fisica':
                    self.tabla.insert('', i,text=i+1, values=fila[0:11], tags='EduFis')
                elif fila[4] == None:
                    self.tabla.insert('', i,text=i+1, values=fila[0:11], tags='Agregar')
                else:
                    self.tabla.insert('', i,text=i+1, values=fila[0:11], tags=fila[4])

    def obtener_libro(self, event):
        item_selec = self.tabla.focus()
        diccionario_fila = self.tabla.item(item_selec)
        if 'values' in diccionario_fila and len(diccionario_fila['values']) != 0:
            self.titulo.set(diccionario_fila['values'][0])
            self.autor.set(diccionario_fila['values'][1])
            self.editorial.set(diccionario_fila['values'][2])
            self.año_edicion.set(diccionario_fila['values'][3])
            self.categoria.set(diccionario_fila['values'][4])
            # print(self.categoria.get())
            if self.categoria.get() == "Persona, Familia, Comunidad y Civismo":
                self.categoria.set("P.F.C.C")
            elif self.categoria.get() == "Manual para profesores":
                self.categoria.set("Manual")
            elif self.categoria.get() == "Repuesto":
                self.categoria.set("Otros")
            # print(self.categoria.get())
            self.cantidad.set(diccionario_fila['values'][5])
            self.remitente.set(diccionario_fila['values'][6])
            self.nivel_educativo.set(diccionario_fila['values'][7])
            self.condicion_libro.set(diccionario_fila['values'][8])
            self.año_recepcion.set(diccionario_fila['values'][9])
        else:
            self.limpiar_campos()
            
                    
    def limpiar_campos(self):
        self.titulo.set('')
        self.autor.set('')
        self.editorial.set('')
        self.año_edicion.set('')
        self.categoria.set('')
        self.cantidad.set(0)
        self.remitente.set('')
        self.nivel_educativo.set('')
        self.condicion_libro.set('')
        self.año_recepcion.set('')
    
    def actualizar_libro(self):
        #? LIBROID ES 10
        item_l = self.tabla.focus()
        diccionario_libro = self.tabla.item(item_l)
        if len(diccionario_libro['values']) >= 6:
            idlibro = diccionario_libro['values'][10]
            l_datos = self.bd.show_libros()
            for fila in l_datos:
                id_bd = fila[10]
                if id_bd == idlibro and id_bd != None:
                    titulo = self.titulo.get()
                    autor = self.autor.get()
                    editorial = self.editorial.get()
                    añoedicion = self.año_edicion.get()
                    categoria = self.categoria.get()
                    
                    cantidad = self.cantidad.get()
                    remitente = self.remitente.get()
                    niveleducativo = self.nivel_educativo.get()
                    condicionlibro = self.condicion_libro.get()
                    añorecepcion = self.año_recepcion.get()
                    question_box = messagebox.askquestion('Información', 'Desea actualizar el libro seleccionado')
                    if categoria and niveleducativo and titulo and condicionlibro and cantidad != 0 and question_box == 'yes':
                        categoriaid = self.cat_dic[categoria]
                        self.bd.update_libros(idlibro, remitente, añorecepcion, niveleducativo, titulo, autor, editorial, añoedicion, condicionlibro, cantidad, categoriaid)
                        messagebox.showinfo('Información', 'Fila modificada')
                        self.mostrar_libros()
                    else:
                        messagebox.showerror('ERROR', 'Falta Rellenar')
        elif len(diccionario_libro['values']) == 0:
            print(len(diccionario_libro['values']))
            messagebox.showerror('ERROR', 'Selecciona un libro')
        else:
            messagebox.showerror('ERROR', 'Falta Rellenar')

    def agregar_libro(self):
        titulo = self.titulo.get()
        autor = self.autor.get()
        editorial = self.editorial.get()
        añoedicion = self.año_edicion.get()
        categoria = self.categoria.get()
        cantidad = self.cantidad.get()
        remitente = self.remitente.get()
        niveleducativo = self.nivel_educativo.get()
        condicionlibro = self.condicion_libro.get()
        añorecepcion = self.año_recepcion.get()
        
        if categoria and niveleducativo and titulo and condicionlibro and cantidad != '':
            question_box = messagebox.askquestion('Información', '¿Desea agregar la fila?')
            if question_box == 'yes' and cantidad > 0:
                categoriaid = self.cat_dic[categoria]
                self.bd.append_libro(remitente, añorecepcion, niveleducativo, titulo, autor, editorial ,añoedicion, condicionlibro, cantidad, categoriaid)
                #? NO OBTIENE EL ID EN LA TABLA POSIBLE ERROR
                self.mostrar_libros()
                messagebox.showinfo('Información', 'Fila agregada')
                self.limpiar_campos()
            elif question_box == 'yes' and cantidad == 0:
                messagebox.showerror('ERROR', 'La Cantidad es 0')
        else:
            messagebox.showerror('ERROR', 'Falta Rellenar')
    
    def eliminar_libro(self, event):
        self.limpiar_campos()
        l_item = self.tabla.selection()[0]
        diccionario_fila = self.tabla.item(l_item)
        question_box = messagebox.askquestion('Información', '¿Desea eliminar la fila?')
        if question_box == 'yes':
            self.tabla.delete(l_item)
            self.limpiar_campos()
            self.bd.delete_libro(diccionario_fila['values'][10])
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
            l_datos = self.bd.search_libros(columna, palabra)
            self.tabla.delete(*self.tabla.get_children())
            i = -1
            for fila in l_datos:
                i = i+1
                if fila[4] != 'Baja':
                    if fila[4] == 'Historia y Geografia':
                        self.tabla.insert('', i,text=i+1, values=fila[0:11], tags='HyG')
                    elif fila[4] == 'Lenguaje y Comunicacion':
                        self.tabla.insert('', i,text=i+1, values=fila[0:11], tags='LyC')
                    elif fila[4] == 'Comprension Lectora':
                        self.tabla.insert('', i,text=i+1, values=fila[0:11], tags='ComLectora')
                    elif fila[4] == 'Arte y Musica':
                        self.tabla.insert('', i,text=i+1, values=fila[0:11], tags='AyM')
                    elif fila[4] == 'Educacion Fisica':
                        self.tabla.insert('', i,text=i+1, values=fila[0:11], tags='EduFis')
                    elif fila[4] == None:
                        self.tabla.insert('', i,text=i+1, values=fila[0:11], tags='Agregar')
                    else:
                        self.tabla.insert('', i,text=i+1, values=fila[0:11], tags=fila[4])
        else:
            messagebox.showerror('ERROR', 'No se agrego una busqueda')
    
    
    def dar_baja(self):
        # self.limpiar_campos()
        l_item = self.tabla.focus()
        diccionario_libro = self.tabla.item(l_item)
        cantidad_baja = self.cantidad.get()
        condicion = self.condicion_libro.get()
        if 'values' in diccionario_libro and len(diccionario_libro['values']) != 0:
            titulo = diccionario_libro['values'][0]
            autor = diccionario_libro['values'][1]
            editorial = diccionario_libro['values'][2]
            a_edicion = diccionario_libro['values'][3]
            categoria = 24
            cantidad_total = diccionario_libro['values'][5]
            remitente = diccionario_libro['values'][6]
            n_educativo = diccionario_libro['values'][7]
            a_recepcion = diccionario_libro['values'][9]
            libroid = diccionario_libro['values'][10]
            question_box = messagebox.askquestion('Información', '¿Desea dar de baja el libro seleccionado?')
            if question_box == 'yes' and cantidad_total > cantidad_baja and cantidad_baja > 0:
                self.bd.append_libro(remitente,a_recepcion,n_educativo,titulo,autor,editorial,a_edicion,condicion,cantidad_baja,categoria)
                cantidad_nueva = cantidad_total-cantidad_baja
                self.bd.update_libro_cantidad(libroid,cantidad_nueva)
                messagebox.showinfo('Información', 'Fila dada de baja')
                self.mostrar_libros()
            elif cantidad_total == cantidad_baja and question_box == 'yes' and cantidad_baja > 0:
                self.bd.update_libros(libroid,remitente,a_recepcion,n_educativo,titulo,autor,editorial,a_edicion,condicion,cantidad_baja,categoria)
                messagebox.showinfo('Información', 'Fila dada de baja')
                self.mostrar_libros()
            elif cantidad_total < cantidad_baja and question_box == 'yes':
                messagebox.showerror('Información', 'Cantidad erronea')
            else:
                messagebox.showerror('Información', 'Proceso erroneo')
        else:
            messagebox.showerror('ERROR', 'Selecciona un libro')
            
    def guardar_libros(self):
        self.limpiar_campos()
        self.informe.save_libros()
        messagebox.showinfo('Informacion', 'Datos guardados')
            