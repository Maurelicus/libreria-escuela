import tkinter  as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from datetime import date

from conexion_sqlite import Comunicacion

class Widgets4v():
    def __init__(self):
        self.situacion = tk.StringVar()
        self.observacion = tk.StringVar()
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

    def obtener_fila(self, event):
        item_selec = self.tabla.focus()
        diccionario_fila = self.tabla.item(item_selec)
        if 'values' in diccionario_fila and len(diccionario_fila['values']) >= 2:
            self.situacion.set(diccionario_fila['values'][4])
            self.observacion.set(diccionario_fila['values'][2])
        else:
            self.limpiar_campos()
            
    def actualizar_tabla(self):
        self.limpiar_campos()
        l_datos = self.bd.mostrar_datosv4()
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
            l_datos = self.bd.buscadorv4(columna, palabra)
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
        # print(diccionario_fila)
        id_pedido = diccionario_fila['values'][6]
        # print(id_pedido)
        cantidad_devuelta = diccionario_fila['values'][5]
        # print(cantidad_devuelta)
        info_libro = self.bd.obtener_librov4(id_pedido)
        # print(info_libro)
        id_libro = info_libro[0][0]
        # print(id_libro)
        cantidad_libro = info_libro[0][1]
        # print(cantidad_libro)
        situacion = self.situacion.get()
        # print(situacion)
        observacion = self.observacion.get()
        # print(observacion)
        pregunta_box = messagebox.askquestion('Información', '¿Estas seguro?')
        
        if observacion != '' and situacion == 'entregado' and pregunta_box == 'yes':
                cantidad = cantidad_devuelta + cantidad_libro
                # print(cantidad)
                hoy = date.today()
                # print(hoy)
                self.bd.actualizar_filav3(id_libro, cantidad)
                self.bd.actualizar_filav4(id_pedido, hoy, situacion, observacion)
                self.limpiar_campos()
                self.actualizar_tabla()
                