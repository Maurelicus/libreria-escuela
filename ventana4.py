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
        self.photo1 = ImageTk.PhotoImage(Image.open("images/reload.png"))
        self.photo2 = ImageTk.PhotoImage(Image.open("images/excel.png"))
        
        
    def seccion_uno(self, frame_uno):
        #! TEXTO
        situacion_label = ttk.Label(frame_uno, text='Situacion')
        situacion_label.grid(column=0, row=1, padx=30, pady=[10,5], sticky='w')
        observacion_label = ttk.Label(frame_uno, text='Observacion')
        observacion_label.grid(column=0, row=2, padx=30, pady=5, sticky='w')
        si_list = ["entregado", "no entregado"]
        situacion_combobox = ttk.Combobox(frame_uno, textvariable=self.situacion, value=si_list, width=20)
        situacion_combobox.current(0)
        situacion_combobox.state(["readonly"])
        situacion_combobox.grid(column=1, row=1, padx=5 ,pady=5, sticky='w')
        observacion_entry = ttk.Entry(frame_uno, textvariable=self.observacion, width=20)
        observacion_entry.grid(column=1, row=2, padx=5 ,pady=5, sticky='w')
        update_boton = ttk.Button(frame_uno, text='Aceptar', width=9, command=self.actualizar_fila)
        update_boton.grid(column=0, row=3, padx=30, pady=10, sticky='nsw')
    
    def seccion_dos(self, frame_dos):
        frame_busqueda = ttk.Frame(frame_dos)
        frame_busqueda.grid(column=0, row=0, padx=5, pady=[1,5], sticky='nsew')
        
        l_columna = ('Alumno', 'Libro', 'Fecha', 'Situacion',)
        columna_box = ttk.Combobox(frame_busqueda, width=15, value=l_columna, textvariable=self.nombre_columna)
        columna_box.current(0)
        columna_box.state(["readonly"])
        columna_box.grid(column=0, row=0, padx=5, pady=5, sticky='nswe')
        palabra_entry = ttk.Entry(frame_busqueda, textvariable=self.palabra, width=40)
        palabra_entry.grid(column=1, row=0, padx=5 ,pady=5, sticky='nswe')
        busc_boton = ttk.Button(frame_busqueda, text='buscar', width=10, 
                                command=self.buscador)
        busc_boton.grid(column=2, row=0, padx=5, pady=5, sticky='nswe')
        save_boton = ttk.Button(frame_busqueda, width=20, image=self.photo2)
        save_boton.grid(column=3, row=0, padx=5, pady=5, sticky='nswe')
        show_boton = ttk.Button(frame_busqueda, width=20, image=self.photo1,
                                command=self.actualizar_tabla)
        show_boton.grid(column=4, row=0, padx=5, pady=5, sticky='nswe')
        
        #! TABLA
        frame_tabla = ttk.LabelFrame(frame_dos, text='Tabla')
        frame_tabla.grid(column=0, row=1, padx=5, pady=[1,5], sticky='nsew')
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
        self.tabla['columns'] = ('Alumno', 'Libro', 'Observacion', 'FechaSalida','FechaEntrada', 'Situacion', 'Cantidad')
        self.tabla.column('#0', minwidth=50, width=60, anchor='center')
        self.tabla.column('#1', minwidth=200, width=220, anchor='w')
        self.tabla.column('#2', minwidth=200, width=220, anchor='w')
        self.tabla.column('#3', minwidth=150, width=170, anchor='w')
        self.tabla.column('#4', minwidth=100, width=110, anchor='center')
        self.tabla.column('#5', minwidth=100, width=110, anchor='center')
        self.tabla.column('#6', minwidth=100, width=100, anchor='center')
        self.tabla.column('#7', minwidth=50, width=60, anchor='center')
            
        self.tabla.heading('#0', text='Nº', anchor='center')
        self.tabla.heading('#1', text='Alumno', anchor='center')
        self.tabla.heading('#2', text='Libro', anchor='center')
        self.tabla.heading('#3', text='Observacion', anchor='center')
        self.tabla.heading('#4', text='Fecha Salida', anchor='center')
        self.tabla.heading('#5', text='Fecha Entrada', anchor='center')
        self.tabla.heading('#6', text='Situacion', anchor='center')
        self.tabla.heading('#7', text='Cantidad', anchor='center')
        self.tabla.bind("<<TreeviewSelect>>", self.obtener_fila)

    def obtener_fila(self, event):
        item_selec = self.tabla.focus()
        diccionario_fila = self.tabla.item(item_selec)
        if 'values' in diccionario_fila and len(diccionario_fila['values']) >= 2:
            self.situacion.set(diccionario_fila['values'][5])
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
            self.tabla.insert('', i, text=i+1, values=fila[0:8])
            
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
                self.tabla.insert('', i,text=i+1, values=fila[0:8])
        else:
            messagebox.showerror('ERROR', 'No se agrego una busqueda')
            
    def actualizar_fila(self):
        item_l = self.tabla.focus()
        diccionario_fila = self.tabla.item(item_l)
        id_pedido = diccionario_fila['values'][7]
        cantidad_devuelta = diccionario_fila['values'][6]
        info_libro = self.bd.obtener_librov4(id_pedido)
        id_libro = info_libro[0][0]
        cantidad_libro = info_libro[0][1]
        situacion = self.situacion.get()
        observacion = self.observacion.get()
        pregunta_box = messagebox.askokcancel('Información', 'Se modificará la fila seleccionada')
        
        if observacion != '' and situacion == 'entregado' and pregunta_box == True:
                cantidad = cantidad_devuelta + cantidad_libro
                hoy = date.today()
                self.bd.actualizar_filav3(id_libro, cantidad)
                self.bd.actualizar_filav4(id_pedido, hoy, situacion, observacion)
                self.limpiar_campos()
                messagebox.showinfo('Información', 'Fila modificada')
                self.actualizar_tabla()
                