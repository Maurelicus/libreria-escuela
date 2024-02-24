from PIL import Image, ImageTk
from tkinter import messagebox
import ttkbootstrap as ttk
import tkinter  as tk

from data.conexion_sqlite import Comunicacion
from data.informes import Informes

class BajaLamina():
    def __init__(self):
        self.titulo = tk.StringVar()
        self.condicion_lamina = tk.StringVar()
        self.cantidad = tk.IntVar()
        self.palabra = tk.StringVar()
        self.nombre_columna = tk.StringVar()
        self.bd = Comunicacion()
        self.photo1 = ImageTk.PhotoImage(Image.open("images/reload.png"))
        self.photo2 = ImageTk.PhotoImage(Image.open("images/excel.png"))
        self.informe = Informes()
        
    def seccion_uno(self, frame_datos):
        #! TEXTO
        ttk.Label(frame_datos, 
            text='DATOS DE LA LAMINA:', 
            bootstyle='danger'
            ).grid(column=0, row=1, padx=30, pady=10, sticky='w', columnspan=2)

        titulo_label = ttk.Label(frame_datos, text='Titulo', bootstyle='dark')
        titulo_label.grid(column=0, row=2, padx=30, pady=5, sticky='we')
        cantidad_label = ttk.Label(frame_datos, text='Cantidad', bootstyle='dark')
        cantidad_label.grid(column=0, row=5, padx=30, pady=5, sticky='we')
        condicionlamina_label = ttk.Label(frame_datos, text='Condicion', bootstyle='dark')
        condicionlamina_label.grid(column=0, row=6, padx=30, pady=5, sticky='we')

        #! ENTRADAS
        dtitulo_label = ttk.Label(frame_datos, textvariable=self.titulo, wraplength=160, bootstyle='primary')
        dtitulo_label.grid(column=1, row=2, padx=5, pady=5, sticky='w')
        dcantidad_label = ttk.Label(frame_datos, textvariable=self.cantidad, wraplength=160, bootstyle='primary')
        dcantidad_label.grid(column=1, row=5, padx=5 ,pady=5, sticky='w')
        dcondicion_label = ttk.Label(frame_datos, textvariable=self.condicion_lamina, wraplength=160, bootstyle='primary')
        dcondicion_label.grid(column=1, row=6, padx=5, pady=5, sticky='w')

        #! Botones
        reponer_boton = ttk.Button(frame_datos, text='Reponer', width=20, command=self.reponer_libro, bootstyle='primary-outline')
        reponer_boton.grid(column=0, row=7, padx=30, pady=10, sticky='w', columnspan=2)
        
    def seccion_dos(self, frame_vista):
        busqueda_frame = ttk.Frame(frame_vista)
        busqueda_frame.grid(column=0, row=0, padx=5, pady=1, sticky='nsew')
        
        l_columna = ("Titulo", "Año de recepcion", "Remitente", "Nivel educativo", "Condicion de la Lamina", "Cantidad")
        buscar_palabra = ttk.Combobox(busqueda_frame, width=15, value=l_columna, 
                                      textvariable=self.nombre_columna, bootstyle='success')
        buscar_palabra.current(0)
        buscar_palabra.state(["readonly"])
        buscar_palabra.pack(side='left', padx=4)

        palabra_entry = ttk.Entry(busqueda_frame, textvariable=self.palabra, width=40, bootstyle='success')
        palabra_entry.pack(side='left', padx=4)

        busc_boton = ttk.Button(busqueda_frame, text='Buscar', width=10,
                                command=self.buscar, bootstyle='success')
        busc_boton.pack(side='left', padx=4)

        save_boton = ttk.Button(busqueda_frame, width=20, image=self.photo2, 
                                command=self.guardar_datos, bootstyle='success-link')
        save_boton.pack(side='left', padx=4)

        show_boton = ttk.Button(busqueda_frame, width=20, image=self.photo1,
                                command=self.mostrar_laminas, bootstyle='success-link')
        show_boton.pack(side='right', padx=4)
        #! TABLA
        tabla_frame = ttk.LabelFrame(frame_vista, text='Tabla', bootstyle='primary')
        tabla_frame.grid(column=0, row=1, padx=5, pady=5 ,sticky='nsew')
        tabla_frame.columnconfigure(1 , weight=10)
        tabla_frame.rowconfigure(0 , weight=10)
        
        self.tabla = ttk.Treeview(tabla_frame, bootstyle='primary')
        self.tabla.grid(column=1, row=0, sticky='nsew',padx=5, pady=5)
        #! SCROLLBARS
        ladox = ttk.Scrollbar(tabla_frame, orient='horizontal', command=self.tabla.xview, bootstyle='primary-round')
        ladox.grid(column=1, row=1, sticky='ew', padx=5)
        ladoy = ttk.Scrollbar(tabla_frame, orient='vertical', command=self.tabla.yview, bootstyle='primary-round')
        ladoy.grid(column=0, row=0, sticky='ns', pady=5)
        self.tabla.configure(xscrollcommand=ladox.set, yscrollcommand=ladoy.set)
        #! COLUMNAS
        self.tabla['columns'] = ('Titulo','Tipo','Codigo', 'Cantidad','Remitente', 'Niveleducativo', 'Condicion','Añorecepcion')
        self.tabla.column('#0', minwidth=60, width=60, anchor='center')
        self.tabla.column('#1', minwidth=160, width=240, anchor='w')
        self.tabla.column('#2', minwidth=100, width=120, anchor='center')
        self.tabla.column('#3', minwidth=120, width=160, anchor='center')
        self.tabla.column('#4', minwidth=80, width=100, anchor='center')
        self.tabla.column('#5', minwidth=100, width=150, anchor='w')
        self.tabla.column('#6', minwidth=80, width=100, anchor='center')
        self.tabla.column('#7', minwidth=120, width=150, anchor='center')
        self.tabla.column('#8', minwidth=100, width=150, anchor='center')
            
        self.tabla.heading('#0', text='Nº', anchor='center')
        self.tabla.heading('#1', text='Titulo', anchor='center')
        self.tabla.heading('#2', text='Tipo', anchor='center')
        self.tabla.heading('#3', text='Codigo', anchor='center')
        self.tabla.heading('#4', text='Cantidad', anchor='center')
        self.tabla.heading('#5', text='Remitente', anchor='center')
        self.tabla.heading('#6', text='Condicion', anchor='center')
        self.tabla.heading('#7', text='Nivel educativo', anchor='center')
        self.tabla.heading('#8', text='Año recepcion', anchor='center')
        self.tabla.tag_configure('Baja', background='#bfc9ca')

        self.tabla.bind("<<TreeviewSelect>>", self.obtener_lamina)

    def mostrar_laminas(self):
        self.limpiar_campos()
        l_datos = self.bd.show_laminas()
        # print(l_datos)
        self.tabla.delete(*self.tabla.get_children())
        i = -1
        for fila in l_datos:
            i = i+1
            if fila[1] == 'Baja':
                self.tabla.insert('', i,text=i+1, values=fila[0:9], tags=fila[1])

    def obtener_lamina(self, event):
        item_selec = self.tabla.focus()
        diccionario_fila = self.tabla.item(item_selec)
        # print(diccionario_fila)
        if 'values' in diccionario_fila and len(diccionario_fila['values']) != 0:
            self.titulo.set(diccionario_fila['values'][0])
            self.cantidad.set(diccionario_fila['values'][3])
            self.condicion_lamina.set(diccionario_fila['values'][5])
        else:
            self.limpiar_campos()
        
            
    def limpiar_campos(self):
        self.titulo.set('')
        self.cantidad.set(0)
        self.condicion_lamina.set('')
    
    
    def buscar(self):
        self.limpiar_campos()
        palabra = self.palabra.get()
        columna = self.nombre_columna.get()
        
        if columna == "Año de recepcion":
            columna = "AñoRecepcion"
        elif columna == "Nivel educativo":
            columna = "NivelEducativo"
        elif columna == "Condicion de la Lamina":
            columna = "CondicionLamina"
            
        if palabra != '':
            l_datos = self.bd.search_laminas(columna, palabra)
            self.tabla.delete(*self.tabla.get_children())
            i = -1
            for fila in l_datos:
                i = i+1
                if fila[1] == 'Baja':
                    self.tabla.insert('', i,text=i+1, values=fila[0:9], tags=fila[1])
        else:
            messagebox.showerror('ERROR', 'No se agrego una busqueda')
            
    def reponer_libro(self):
        l_item = self.tabla.focus()
        diccionario_lamina = self.tabla.item(l_item)
        if 'values' in diccionario_lamina and len(diccionario_lamina['values']) != 0:
            titulo = diccionario_lamina['values'][0]
            categoria = 25
            codigo = diccionario_lamina['values'][2]
            cantidad_repuesta = diccionario_lamina['values'][3]
            remitente = diccionario_lamina['values'][4]
            c_lamina = diccionario_lamina['values'][5]
            n_educativo = diccionario_lamina['values'][6]
            a_recepcion = diccionario_lamina['values'][7]
            laminaid = diccionario_lamina['values'][8]
            question_box = messagebox.askquestion('Información', '¿Desea reponer el libro seleccionado?')
            if question_box == 'yes':
                self.bd.update_lamina(laminaid,codigo,remitente,a_recepcion,n_educativo,titulo,c_lamina,cantidad_repuesta,categoria)
                messagebox.showinfo('Información', 'Libro(s) repuestos')
                self.mostrar_laminas()
            else:
                messagebox.showerror('Información', 'Proceso erroneo')
        else:
            messagebox.showerror('ERROR', 'Selecciona un libro')
    
    def guardar_datos(self):
        self.limpiar_campos()
        self.informe.save_bajalaminas()
        messagebox.showinfo('Informacion', 'Datos guardados')
