import tkinter  as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

from conexion_sqlite import Comunicacion

class Widgets4v():
    def __init__(self):
        self.codigo = tk.StringVar()
        self.libroid = tk.StringVar()
        self.usuarioid = tk.StringVar()
        self.fecha = tk.StringVar()
        self.situacion = tk.StringVar()
        self.observacion = tk.StringVar()
        self.cantidad = tk.StringVar()
        self.palabra = tk.StringVar()
        self.nombre_columna = tk.StringVar()
        self.bd = Comunicacion()
        self.photo1 = ImageTk.PhotoImage(Image.open("reload.png"))
        self.photo2 = ImageTk.PhotoImage(Image.open("excel.png"))
        
        
    def seccion_uno(self, frame_uno):
        #! TEXTO
        situacion_label = ttk.Label(frame_uno, text='Situacion')
        situacion_label.grid(column=0, row=1, padx=5, pady=[10,5])
        observacion_label = ttk.Label(frame_uno, text='Observacion')
        observacion_label.grid(column=0, row=2, padx=5, pady=5)
        situacion_entry = ttk.Entry(frame_uno, textvariable=self.situacion)
        situacion_entry.grid(column=1, row=1, padx=5 ,pady=5)
        observacion_entry = ttk.Entry(frame_uno, textvariable=self.observacion)
        observacion_entry.grid(column=1, row=2, padx=5 ,pady=5)
        update_boton = ttk.Button(frame_uno, text='Aceptar', width=20, command=self.actualizar_fila)
        update_boton.grid(column=0, row=3, padx=5, pady=[5,10])
        """
        nied_list = ["Primaria", "Secundaria"]
        niveleducativo_combobox = ttk.Combobox(frame_uno, textvariable=self.nivel_educativo ,value=nied_list)
        niveleducativo_combobox.grid(column=1, row=3, padx=5 ,pady=5)
        niveleducativo_combobox.current(0)
        niveleducativo_combobox.state(["readonly"])
        titulo_entry = ttk.Entry(frame_uno, textvariable=self.titulo)
        titulo_entry.grid(column=1, row=4, padx=5 ,pady=5)
        autor_entry = ttk.Entry(frame_uno, textvariable=self.autor)
        autor_entry.grid(column=1, row=5, padx=5 ,pady=5)
        editorial_entry = ttk.Entry(frame_uno, textvariable=self.editorial)
        editorial_entry.grid(column=1, row=6, padx=5 ,pady=5)
        añoedicion_entry = ttk.Entry(frame_uno, textvariable=self.año_edicion)
        añoedicion_entry.grid(column=1, row=7, padx=5 ,pady=5)
        coli_list = ["B", "R"]
        condicionlibro_combobox = ttk.Combobox(frame_uno, textvariable=self.condicion_libro ,value=coli_list)
        condicionlibro_combobox.grid(column=1, row=8, padx=5 ,pady=5)
        condicionlibro_combobox.current(0)
        condicionlibro_combobox.state(["readonly"])
        cantidad_entry = ttk.Entry(frame_uno, textvariable=self.cantidad)
        cantidad_entry.grid(column=1, row=9, padx=5 ,pady=[5,10])
        #! Botones
        clear_boton = ttk.Button(frame_uno, text='Limpiar campos', width=20, command=self.limpiar_campos)
        clear_boton.grid(column=1, row=10, padx=5, pady=[5,10])
        add_boton = ttk.Button(frame_uno, text='Añadir fila', width=20, command=self.agregar_fila)
        add_boton.grid(column=0, row=11, padx=5, pady=[5,10])
        """ 
    
    def seccion_dos(self, frame_dos):
        frame_busqueda = ttk.LabelFrame(frame_dos, text='Opciones')
        frame_busqueda.grid(column=0, row=0, padx=5, pady=5, sticky='ew')
        
        l_columna = ('Alumno', 'Libro', 'Fecha', 'Situacion',)
        columna_box = ttk.Combobox(frame_busqueda, width=20, value=l_columna, textvariable=self.nombre_columna)
        columna_box.current(0)
        columna_box.grid(column=0, row=0, padx=5, pady=5)
        columna_box.state(["readonly"])
        palabra_entry = ttk.Entry(frame_busqueda, textvariable=self.palabra)
        palabra_entry.grid(column=1, row=0, padx=5 ,pady=1 )
        busc_boton = ttk.Button(frame_busqueda, text='buscar', width=20, 
                                command=self.buscador)
        busc_boton.grid(column=2, row=0, padx=5, pady=5)
        save_boton = ttk.Button(frame_busqueda, width=20, image=self.photo2)
        save_boton.grid(column=3, row=0, padx=5, pady=5)
        show_boton = ttk.Button(frame_busqueda, width=20, image=self.photo1,
                                command=self.actualizar_tabla)
        show_boton.grid(column=4, row=0, padx=5, pady=5, sticky='w')
        
        #! TABLA
        frame_tabla = ttk.LabelFrame(frame_dos, text='Tabla')
        frame_tabla.grid(column=0, row=1, padx=5, pady=5 ,sticky='nsew')
        frame_tabla.columnconfigure(1 , weight=10)
        frame_tabla.rowconfigure(0 , weight=10)
        
        self.tabla = ttk.Treeview(frame_tabla)
        self.tabla.grid(column=1, row=0, sticky='nsew',padx=5, pady=5)
        #! SCROLLBARS
        ladox = ttk.Scrollbar(frame_tabla, orient='horizontal', command=self.tabla.xview)
        ladox.grid(column=1, row=1, sticky='ew', padx=5)
        ladoy = ttk.Scrollbar(frame_tabla, orient='vertical', command=self.tabla.yview)
        ladoy.grid(column=0, row=0, sticky='ns', pady=5)
        self.tabla.configure(xscrollcommand=ladox.set, yscrollcommand=ladoy.set)
        #! COLUMNAS
        self.tabla['columns'] = ('Alumno', 'Libro', 'Observacion', 'Fecha', 'Situacion', 'Cantidad')
        self.tabla.column('#0', minwidth=50, width=60, anchor='center')
        self.tabla.column('#1', minwidth=150, width=160, anchor='w')
        self.tabla.column('#2', minwidth=150, width=160, anchor='w')
        self.tabla.column('#3', minwidth=120, width=120, anchor='center')
        self.tabla.column('#4', minwidth=120, width=130, anchor='center')
        self.tabla.column('#5', minwidth=120, width=130, anchor='center')
        self.tabla.column('#6', minwidth=50, width=60, anchor='center')
            
        self.tabla.heading('#0', text='Nº', anchor='center')
        self.tabla.heading('#1', text='Alumno', anchor='center')
        self.tabla.heading('#2', text='Libro', anchor='center')
        self.tabla.heading('#3', text='Observacion', anchor='center')
        self.tabla.heading('#4', text='Fecha', anchor='center')
        self.tabla.heading('#5', text='Situacion', anchor='center')
        self.tabla.heading('#6', text='Cantidad', anchor='center')
        self.tabla.bind("<<TreeviewSelect>>", self.obtener_fila)
        """ 
        self.tabla.bind("<Double-1>", self.eliminar_datos)
        """

    def obtener_fila(self, event):
        item_selec = self.tabla.focus()
        diccionario_fila = self.tabla.item(item_selec)
        if 'values' in diccionario_fila and len(diccionario_fila['values']) >= 0:
            self.situacion.set(diccionario_fila['values'][4])
            self.observacion.set(diccionario_fila['values'][2])
        else:
            self.limpiar_campos()
            
    def actualizar_tabla(self):
        self.limpiar_campos()
        l_datos = self.bd.mostrar_datos3()
        self.tabla.delete(*self.tabla.get_children())
        i = -1
        for fila in l_datos:
            i = i+1
            self.tabla.insert('', i,text=i+1, values=fila[0:7])
            
    def limpiar_campos(self):
        self.observacion.set('')
        self.situacion.set('')
    
    def buscador(self):
        self.limpiar_campos()
        palabra = self.palabra.get()
        columna = self.nombre_columna.get()
        if palabra != '':
            l_datos = self.bd.buscador5(columna, palabra)
            self.tabla.delete(*self.tabla.get_children())
            i = -1
            for fila in l_datos:
                i = i+1
                self.tabla.insert('', i,text=i+1, values=fila[0:7])
        else:
            messagebox.showerror('Información', 'No se agrego una busqueda')
            
    def actualizar_fila(self):
        item_l = self.tabla.focus()
        diccionario_fila = self.tabla.item(item_l)
        id_pedido = diccionario_fila['values'][6]
        # situacion_actual = diccionario_fila['values'][4]
        l_datos = self.bd.mostrar_datos3()
        libro = self.bd.obtener_libro(id_pedido)
        
        for fila in l_datos:
            id_bdpedido = fila[6]
            cantidad_devuelta = fila[5]
            situacion_actual = fila[4]
            if id_bdpedido == id_pedido and id_bdpedido != None and self.situacion == 'entregado':
                situacion = self.situacion.get()
                observacion = self.observacion.get()
                pregunta_box = messagebox.askquestion('Información', '¿Estas seguro?')
                if situacion and observacion != '' and pregunta_box == 'yes':
                    cantidad = cantidad_devuelta + libro[0][1]
                    self.bd.actualizar_fila4(libro[0][0], cantidad, situacion)
                    self.actualizar_tabla()
    
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
        if remitente and niveleducativo and titulo and condicionlibro and cantidad != '':
            self.bd.insertar_fila(remitente, añorecepcion, niveleducativo, titulo, autor, editorial ,añoedicion, condicionlibro, cantidad)
            # falta mejorar
            self.tabla.insert('',"end",text=c_filas+1, values=datos)
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
            self.bd.eliminar_fila(diccionario_fila['values'][9])
    """
    
