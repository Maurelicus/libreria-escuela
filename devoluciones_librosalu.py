import tkinter  as tk
from tkinter import messagebox
import ttkbootstrap as ttk

from PIL import Image, ImageTk
from datetime import date

from conexion_sqlite import Comunicacion
from ventana_libros import VentanaLibros

class DevolucionesLibros():
    def __init__(self):
        self.alumno = tk.StringVar()
        self.material = tk.StringVar()
        self.situacion = tk.StringVar()
        self.observacion = tk.StringVar()
        self.tipo = tk.StringVar()
        self.cantidad = tk.IntVar()
        self.palabra = tk.StringVar()
        self.nombre_columna = tk.StringVar()
        self.bd = Comunicacion()
        self.photo1 = ImageTk.PhotoImage(Image.open("images/reload.png"))
        self.photo2 = ImageTk.PhotoImage(Image.open("images/excel.png"))
        
        
    def seccion_uno(self, frame_uno):
        #! TEXTO
        alumno_label = ttk.Label(frame_uno, text='Alumno:', bootstyle='dark')
        alumno_label.grid(column=0, row=1, padx=30, pady=[10,5], sticky='w')
        material_label = ttk.Label(frame_uno, text='Material:', bootstyle='dark')
        material_label.grid(column=0, row=2, padx=30, pady=5, sticky='w')
        situacion_label = ttk.Label(frame_uno, text='Situacion', bootstyle='dark')
        situacion_label.grid(column=0, row=3, padx=30, pady=5, sticky='w')
        observacion_label = ttk.Label(frame_uno, text='Observacion', bootstyle='dark')
        observacion_label.grid(column=0, row=4, padx=30, pady=5, sticky='w')
        cantidad_label = ttk.Label(frame_uno, text='Cantidad', bootstyle='dark')
        cantidad_label.grid(column=0, row=5, padx=30, pady=[5,10], sticky='w')


        a_label = ttk.Label(frame_uno, textvariable=self.alumno, wraplength=160, bootstyle='dark')
        a_label.grid(column=1, row=1, padx=5, pady=[10,5], sticky='w')
        ma_label = ttk.Label(frame_uno, textvariable=self.material, wraplength=160, bootstyle='dark')
        ma_label.grid(column=1, row=2, padx=5, pady=5, sticky='w')
        si_list = ["devuelto", "prestado"]
        situacion_combobox = ttk.Combobox(frame_uno, textvariable=self.situacion, value=si_list, width=20, bootstyle='primary')
        situacion_combobox.current(0)
        situacion_combobox.state(["readonly"])
        situacion_combobox.grid(column=1, row=3, padx=5 ,pady=5, sticky='w')
        observacion_entry = ttk.Entry(frame_uno, textvariable=self.observacion, width=20, bootstyle='primary')
        observacion_entry.grid(column=1, row=4, padx=5 ,pady=5, sticky='w')
        cantidad_entry = ttk.Spinbox(frame_uno, textvariable=self.cantidad, from_=0, to=100, width=5, bootstyle='primary')
        cantidad_entry.state(["readonly"])
        cantidad_entry.grid(column=1, row=5, padx=5 ,pady=[5,10], sticky='w')

        return_boton = ttk.Button(frame_uno, text='Aceptar', width=9, command=self.devolver, bootstyle='primary-outline')
        return_boton.grid(column=0, row=6, padx=30, pady=10, sticky='nsw')
    
    def seccion_dos(self, frame_dos):
        frame_busqueda = ttk.Frame(frame_dos)
        frame_busqueda.grid(column=0, row=0, padx=5, pady=[1,5], sticky='nsew')
        
        l_columna = ('Alumno', 'Libro', 'Fecha', 'Situacion',)
        columna_box = ttk.Combobox(frame_busqueda, width=15, value=l_columna, 
                                   textvariable=self.nombre_columna, bootstyle='success')
        columna_box.current(0)
        columna_box.state(["readonly"])
        columna_box.pack(side='left', padx=4)

        palabra_entry = ttk.Entry(frame_busqueda, textvariable=self.palabra, width=40, bootstyle='success')
        palabra_entry.pack(side='left', padx=4)

        busc_boton = ttk.Button(frame_busqueda, text='buscar', width=10, 
                                command=self.buscador, bootstyle='success')
        busc_boton.pack(side='left', padx=4)
        
        save_boton = ttk.Button(frame_busqueda, width=20, image=self.photo2, bootstyle='success-link')
        save_boton.pack(side='left', padx=4)

        show_boton = ttk.Button(frame_busqueda, width=20, image=self.photo1,
                                command=self.mostrar_pedidoslib, bootstyle='success-link')
        show_boton.pack(side='right', padx=4)

        #! TABLA
        frame_tabla = ttk.LabelFrame(frame_dos, text='Lista de Pedidos', bootstyle='info')
        frame_tabla.grid(column=0, row=1, padx=5, pady=[1,5], sticky='nsew')
        frame_tabla.columnconfigure(1 , weight=10)
        frame_tabla.rowconfigure(0 , weight=10)
        
        self.tabla = ttk.Treeview(frame_tabla, bootstyle='info')
        self.tabla.grid(column=1, row=0, sticky='nsew',padx=5, pady=5)
        #! SCROLLBARS
        ladox = ttk.Scrollbar(frame_tabla, orient='horizontal', command=self.tabla.xview, bootstyle='info-round')
        ladox.grid(column=1, row=1, sticky='ew', padx=5)
        ladoy = ttk.Scrollbar(frame_tabla, orient='vertical', command=self.tabla.yview, bootstyle='info-round')
        ladoy.grid(column=0, row=0, sticky='ns', pady=5)
        self.tabla.configure(xscrollcommand=ladox.set, yscrollcommand=ladoy.set)
        #! COLUMNAS
        self.tabla['columns'] = ('Libro','Alumno','FechaSalida', 'FechaEntrada' ,'Cantidad','Situacion', 'Observacion', 'Codigo')
        self.tabla.column('#0', minwidth=50, width=60, anchor='center')
        self.tabla.column('#1', minwidth=150, width=200, anchor='w')
        self.tabla.column('#2', minwidth=150, width=200, anchor='w')
        self.tabla.column('#3', minwidth=100, width=110, anchor='center')
        self.tabla.column('#4', minwidth=100, width=110, anchor='center')
        self.tabla.column('#5', minwidth=50, width=60, anchor='center')
        self.tabla.column('#6', minwidth=100, width=110, anchor='center')
        self.tabla.column('#7', minwidth=100, width=110, anchor='w')
        self.tabla.column('#8', minwidth=80, width=100, anchor='center')
            
        self.tabla.heading('#0', text='Nº', anchor='center')
        self.tabla.heading('#1', text='Libro', anchor='center')
        self.tabla.heading('#2', text='Alumno', anchor='center')
        self.tabla.heading('#3', text='Fecha Salida', anchor='center')
        self.tabla.heading('#4', text='Fecha Entrada', anchor='center')
        self.tabla.heading('#5', text='Cantidad', anchor='center')
        self.tabla.heading('#6', text='Situacion', anchor='center')
        self.tabla.heading('#7', text='Observacion', anchor='center')
        self.tabla.heading('#8', text='Codigo', anchor='center')

        self.tabla.tag_configure('devuelto', background='#bbead7')
        self.tabla.tag_configure('prestado', background='#ffd6ca')
        self.tabla.bind("<<TreeviewSelect>>", self.obtener_pedido)

    def obtener_pedido(self, event):
        item_selec = self.tabla.focus()
        diccionario_pedido = self.tabla.item(item_selec)
        if 'values' in diccionario_pedido and len(diccionario_pedido['values']) != 0:
            self.material.set(diccionario_pedido['values'][0])
            self.alumno.set(diccionario_pedido['values'][1])
            self.situacion.set(diccionario_pedido['values'][5])
            self.observacion.set(diccionario_pedido['values'][6])
            self.cantidad.set(diccionario_pedido['values'][4])
        else:
            self.limpiar_campos()
            
    def mostrar_pedidoslib(self):
        self.limpiar_campos()
        l_datos = self.bd.showalu_pedidoslib()
        self.tabla.delete(*self.tabla.get_children())
        i = -1
        for fila in l_datos:
            i = i+1
            if fila[5] == 'devuelto':
                self.tabla.insert('', i, text=i+1, values=fila[0:12], tags=fila[5])
            elif fila[5] == 'prestado':
                self.tabla.insert('', i, text=i+1, values=fila[0:12], tags=fila[5])

    def limpiar_campos(self):
        self.alumno.set('')
        self.material.set('')
        self.observacion.set('')
        self.situacion.set('')
        self.cantidad.set(0)
    
    def buscador(self):
        self.limpiar_campos()
        palabra = self.palabra.get()
        columna = self.nombre_columna.get()
        if palabra != '':
            l_datos = self.bd.buscarpro_pedidoslib(columna, palabra)
            self.tabla.delete(*self.tabla.get_children())
            i = -1
            for fila in l_datos:
                i = i+1
                if fila[5] == 'devuelto':
                    self.tabla.insert('', i, text=i+1, values=fila[0:12], tags=fila[5])
                elif fila[5] == 'prestado':
                    self.tabla.insert('', i, text=i+1, values=fila[0:12], tags=fila[5])
        else:
            messagebox.showerror('ERROR', 'No se agrego una busqueda')
            
    def devolver(self):
        item_l = self.tabla.focus()
        diccionario_pedido = self.tabla.item(item_l)
        situacion = self.situacion.get()
        observacion = self.observacion.get()
        cantidad_devuelta = self.cantidad.get()
        
        if 'values' in diccionario_pedido and len(diccionario_pedido['values']) != 0:

            f_salida = diccionario_pedido['values'][2]
            f_entrada = diccionario_pedido['values'][3]
            cantidad_total = diccionario_pedido['values'][4]
            situacion_a = diccionario_pedido['values'][5]
            observacion_a = diccionario_pedido['values'][6]
            codigo = diccionario_pedido['values'][7]
            id_pedido = diccionario_pedido['values'][8]
            libroid = diccionario_pedido['values'][9]
            alumnoid = diccionario_pedido['values'][10]
            tipo = diccionario_pedido['values'][11]
            info_libro = self.bd.info_pedidolib(id_pedido)
            id_libro = info_libro[0][0]
            cantidad_libro = info_libro[0][1]
            # alumnoid = info_libro[0][2]
            fecha_salida = info_libro[0][3]
            
            if situacion_a != 'devuelto':     
                pregunta_box = messagebox.askokcancel('Información', 'Se modificará la fila seleccionada')
                if cantidad_total > cantidad_devuelta and situacion == 'devuelto' and observacion != '' and pregunta_box == True:
                    hoy = date.today()
                    self.bd.appendalu_pedidolib(codigo, libroid, alumnoid, f_salida, hoy, situacion, observacion, cantidad_devuelta, tipo)
                    cantidad_nueva = cantidad_libro + cantidad_devuelta
                    self.bd.update_libro_cantidad(libroid, cantidad_nueva)
                    cantidad_faltante = cantidad_total - cantidad_devuelta
                    self.bd.updatealu_pedidolib(id_pedido,f_entrada, situacion_a, observacion_a, cantidad_faltante)
                    self.limpiar_campos()
                    messagebox.showinfo('Información', 'Fila modificada')
                    self.mostrar_pedidoslib()
                elif cantidad_total == cantidad_devuelta and observacion != '' and situacion == 'devuelto' and pregunta_box == True:
                    hoy = date.today()
                    self.bd.updatealu_pedidolib(id_pedido, hoy, situacion, observacion, cantidad_devuelta)
                    cantidad_nueva = cantidad_devuelta + cantidad_libro
                    self.bd.update_libro_cantidad(libroid, cantidad_nueva)
                    self.limpiar_campos()
                    messagebox.showinfo('Información', 'Fila modificada')
                    self.mostrar_pedidoslib()
                elif cantidad_total < cantidad_devuelta:
                    messagebox.showerror('Información', 'Cantidad excedida al total pedido')
                else:
                    messagebox.showerror('Información', 'Proceso erroneo')
            else:
                messagebox.showerror('Información', 'Libro ya entregado')
        else:
            messagebox.showerror('Información', 'Falta Rellenar')
