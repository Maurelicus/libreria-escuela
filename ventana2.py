import tkinter  as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

from conexion_sqlite import Comunicacion

class Widgets2v():
    def __init__(self):
        self.codigo = tk.StringVar()
        self.remitente = tk.StringVar()
        self.año_recepcion = tk.StringVar()
        self.nivel_educativo = tk.StringVar()
        self.titulo = tk.StringVar()
        self.condicion_lamina = tk.StringVar()
        self.cantidad = tk.IntVar()
        self.palabra = tk.StringVar()
        self.nombre_columna = tk.StringVar()
        self.bd = Comunicacion()
        self.photo1 = ImageTk.PhotoImage(Image.open("images/reload.png"))
        self.photo2 = ImageTk.PhotoImage(Image.open("images/excel.png"))
        
        
    def seccion_uno(self, frame_uno):
        #! TEXTO
        codigo_label = ttk.Label(frame_uno, text='Codigo')
        codigo_label.grid(column=0, row=1, padx=30, pady=[10,5], sticky='w')
        reminente_label = ttk.Label(frame_uno, text='Remitente')
        reminente_label.grid(column=0, row=2, padx=30, pady=5, sticky='w')
        año_recepcion = ttk.Label(frame_uno, text='Año de Recepcion')
        año_recepcion.grid(column=0, row=3, padx=30, pady=5, sticky='w')
        nivel_educativo = ttk.Label(frame_uno, text='Nivel Educativo')
        nivel_educativo.grid(column=0, row=4, padx=30, pady=5, sticky='w')
        titulo = ttk.Label(frame_uno, text='Titulo')
        titulo.grid(column=0, row=5, padx=30, pady=5, sticky='w')
        condicion_lamina = ttk.Label(frame_uno, text='Condicion')
        condicion_lamina.grid(column=0, row=6, padx=30, pady=5, sticky='w')
        cantidad = ttk.Label(frame_uno, text='Cantidad')
        cantidad.grid(column=0, row=7, padx=30, pady=[5,10], sticky='w')
        #! ENTRADAS
        codigo_entry = ttk.Entry(frame_uno, textvariable=self.codigo, width=10)
        codigo_entry.grid(column=1, row=1, padx=5 ,pady=[10,5], sticky='w')
        reminente_entry = ttk.Entry(frame_uno, textvariable=self.remitente, width=10)
        reminente_entry.grid(column=1, row=2, padx=5, pady=5, sticky='w')
        añorecepcion_entry = ttk.Entry(frame_uno, textvariable=self.año_recepcion, width=7)
        añorecepcion_entry.grid(column=1, row=3, padx=5, pady=5, sticky='w')
        nied_list = ["Primaria", "Secundaria"]
        niveleducativo_combobox = ttk.Combobox(frame_uno, textvariable=self.nivel_educativo ,value=nied_list, width=10)
        niveleducativo_combobox.grid(column=1, row=4, padx=5 ,pady=5, sticky='w')
        niveleducativo_combobox.current(0)
        niveleducativo_combobox.state(["readonly"])
        titulo_entry = ttk.Entry(frame_uno, textvariable=self.titulo, width=20)
        titulo_entry.grid(column=1, row=5, padx=5, pady=5, sticky='w')
        coli_list = ["A", "B", "C"]
        condicionlibro_combobox = ttk.Combobox(frame_uno, textvariable=self.condicion_lamina ,value=coli_list, width=2)
        condicionlibro_combobox.grid(column=1, row=6, padx=5, pady=5, sticky='w')
        condicionlibro_combobox.current(0)
        condicionlibro_combobox.state(["readonly"])
        cantidad_entry = ttk.Spinbox(frame_uno, textvariable=self.cantidad, from_=0, to=100, width=5)
        cantidad_entry.grid(column=1, row=7, padx=5 ,pady=[5,10], sticky='w')
        #! Botones
        update_boton = ttk.Button(frame_uno, text='Actualizar fila', width=15, command=self.actualizar_fila)
        update_boton.grid(column=0, row=8, padx=30, pady=10, sticky='w')
        clear_boton = ttk.Button(frame_uno, text='Limpiar campos', width=15, command=self.limpiar_campos)
        clear_boton.grid(column=1, row=8, padx=5, pady=10, sticky='w')
        add_boton = ttk.Button(frame_uno, text='Añadir fila', width=15, command=self.agregar_fila)
        add_boton.grid(column=0, row=9, padx=30, pady=10, sticky='w')
    
    def seccion_dos(self, frame_dos):
        frame_busqueda = ttk.Frame(frame_dos)
        frame_busqueda.grid(column=0, row=0, padx=5, pady=[1,5], sticky='nsew')
        
        l_columna = ("Titulo", "AñoRecepcion", "Remitente", "NivelEducativo", "CondicionLamina", "Cantidad")
        buscar_palabra = ttk.Combobox(frame_busqueda, width=15, value=l_columna, textvariable=self.nombre_columna)
        buscar_palabra.current(0)
        buscar_palabra.grid(column=0, row=0, padx=5, pady=5, sticky='nsew')
        buscar_palabra.state(["readonly"])
        filtro_libroid = ttk.Entry(frame_busqueda, textvariable=self.palabra, width=40)
        filtro_libroid.grid(column=1, row=0, padx=5 ,pady=5, sticky='nsew')
        busc_boton = ttk.Button(frame_busqueda, text='Buscar', width=10, command=self.buscador)
        busc_boton.grid(column=2, row=0, padx=5, pady=5, sticky='nsew')
        save_boton = ttk.Button(frame_busqueda, width=20, image=self.photo2)
        save_boton.grid(column=3, row=0, padx=5, pady=5, sticky='nsew')
        show_boton = ttk.Button(frame_busqueda, width=20, image=self.photo1,command=self.actualizar_tabla)
        show_boton.grid(column=4, row=0, padx=5, pady=5, sticky='nsew')
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
        self.tabla['columns'] = ('Codigo', 'Remitente', 'Añorecepcion', 'Niveleducativo', 'Titulo', 'Condicion', 'Cantidad')
        self.tabla.column('#0', minwidth=60, width=60, anchor='center')
        self.tabla.column('#1', minwidth=100, width=100, anchor='center')
        self.tabla.column('#2', minwidth=100, width=120, anchor='center')
        self.tabla.column('#3', minwidth=90, width=110, anchor='center')
        self.tabla.column('#4', minwidth=120, width=120, anchor='center')
        self.tabla.column('#5', minwidth=200, width=200, anchor='w')
        self.tabla.column('#6', minwidth=90, width=90, anchor='center')
        self.tabla.column('#7', minwidth=90, width=90, anchor='center')
            
        self.tabla.heading('#0', text='Nº', anchor='center')
        self.tabla.heading('#1', text='Codigo', anchor='center')
        self.tabla.heading('#2', text='Remitente', anchor='center')
        self.tabla.heading('#3', text='Año recepcion', anchor='center')
        self.tabla.heading('#4', text='Nivel educativo', anchor='center')
        self.tabla.heading('#5', text='Titulo', anchor='center')
        self.tabla.heading('#6', text='Condicion', anchor='center')
        self.tabla.heading('#7', text='Cantidad', anchor='center')
        
        self.tabla.bind("<<TreeviewSelect>>", self.obtener_fila)
        self.tabla.bind("<Double-1>", self.eliminar_datos)

    def obtener_fila(self, event):
        item_selec = self.tabla.focus()
        diccionario_fila = self.tabla.item(item_selec)
        if 'values' in diccionario_fila and len(diccionario_fila['values']) >= 4:
            self.codigo.set(diccionario_fila['values'][0])
            self.remitente.set(diccionario_fila['values'][1])
            self.año_recepcion.set(diccionario_fila['values'][2])
            self.nivel_educativo.set(diccionario_fila['values'][3])
            self.titulo.set(diccionario_fila['values'][4])
            self.condicion_lamina.set(diccionario_fila['values'][5])
            self.cantidad.set(diccionario_fila['values'][6])
        else:
            self.limpiar_campos()
            
    def actualizar_tabla(self):
        self.limpiar_campos()
        l_datos = self.bd.mostrar_datosv2()
        self.tabla.delete(*self.tabla.get_children())
        i = -1
        for fila in l_datos:
            i = i+1
            self.tabla.insert('', i,text=i+1, values=fila[0:8])
            
    def limpiar_campos(self):
        self.codigo.set('')
        self.remitente.set('')
        self.año_recepcion.set('')
        self.nivel_educativo.set('')
        self.titulo.set('')
        self.condicion_lamina.set('')
        self.cantidad.set('')
    
    def actualizar_fila(self):
        item_l = self.tabla.focus()
        diccionario_fila = self.tabla.item(item_l)
        id = diccionario_fila['values'][7]
        l_datos = self.bd.mostrar_datosv2()
        
        for fila in l_datos:
            id_bd = fila[7]
            if id_bd == id and id_bd != None:
                codigo = self.codigo.get()
                remitente = self.remitente.get()
                añorecepcion = self.año_recepcion.get()
                niveleducativo = self.nivel_educativo.get()
                titulo = self.titulo.get()
                condicionlamina = self.condicion_lamina.get()
                cantidad = self.cantidad.get()
                confirmar_box = messagebox.askokcancel('Información', 'Se modificará la fila seleccionada')
                if remitente and niveleducativo and titulo and codigo and cantidad != '' and confirmar_box == True:
                    self.bd.actualizar_filav2(id, codigo, remitente, añorecepcion, niveleducativo, titulo, condicionlamina, cantidad)
                    messagebox.showinfo('Información', 'Fila modificada')
                    self.actualizar_tabla()
    
    def agregar_fila(self):
        codigo = self.codigo.get()
        remitente = self.remitente.get()
        añorecepcion = self.año_recepcion.get()
        niveleducativo = self.nivel_educativo.get()
        titulo = self.titulo.get()
        condicionlamina = self.condicion_lamina.get()
        cantidad = self.cantidad.get()
        l_datos = self.bd.mostrar_datosv2()
        codigos = []
        for fila in l_datos:
            codigos.append(fila[0])
        palabra = codigo
        if palabra in codigos:
            messagebox.showerror('ERROR', 'Codigo Existente')

        else:
            c_filas = len(self.tabla.get_children())
            datos = (codigo, remitente, añorecepcion, niveleducativo, titulo, condicionlamina, cantidad)
            if codigo and remitente and niveleducativo and titulo and condicionlamina and cantidad != '':
                self.bd.insertar_filav2(codigo, remitente, añorecepcion, niveleducativo, titulo, condicionlamina, cantidad)
                self.tabla.insert('', "end", text=c_filas+1, values=datos)
                self.limpiar_campos()
            else:
                messagebox.showerror('ERROR', 'Falta Rellenar datos')
                
    
    def eliminar_datos(self, event):
        self.limpiar_campos()
        l_item = self.tabla.selection()[0]
        diccionario_fila = self.tabla.item(l_item)
        question_box = messagebox.askquestion('Información', '¿Desea eliminar la fila?')

        if question_box == 'yes':
            self.tabla.delete(l_item)
            self.bd.eliminar_filav2(diccionario_fila['values'][7])
            messagebox.showinfo('Información', 'Fila Eliminada')

    
    def buscador(self):
        self.limpiar_campos()
        palabra = self.palabra.get()
        columna = self.nombre_columna.get()
        if palabra != '':
            l_datos = self.bd.buscadorv2(columna, palabra)
            self.tabla.delete(*self.tabla.get_children())
            i = -1
            for fila in l_datos:
                i = i+1
                self.tabla.insert('', i,text=i+1, values=fila[0:8])
        else:
            messagebox.showerror('ERROR', 'No se agrego una busqueda')

