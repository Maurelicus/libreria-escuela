import tkinter  as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from PIL import Image, ImageTk
from time import strftime
import pandas as pd
import openpyxl
from random import randint


from conexion_sqlite import Comunicacion
from informes import Informes

class VentanaAlumnos():
    def __init__(self):
        self.alumnoid = tk.StringVar()
        self.alumno = tk.StringVar()
        self.sexo = tk.StringVar()
        self.nivel = tk.StringVar()
        self.grado = tk.StringVar()
        self.seccion = tk.StringVar()
        self.tipo = tk.StringVar()
        self.palabra = tk.StringVar()
        self.nombre_columna = tk.StringVar()
        self.cont = tk.IntVar()
        # self.cont = 0
        self.bd = Comunicacion()
        self.photo1 = ImageTk.PhotoImage(Image.open("images/reload.png"))
        self.photo2 = ImageTk.PhotoImage(Image.open("images/excel.png"))
        self.informe = Informes()
        
    def seccion_uno(self, frame_uno):
        # self.profesor = ttk.Radiobutton(frame_uno, text='Profesor', variable=self.tipo, value='Profesor', bootstyle='dark') 
        # self.profesor.grid(column=0, row=0, padx=30, pady=[10,5], sticky='we')
        # self.alumno = ttk.Radiobutton(frame_uno, text='Alumno', variable=self.tipo, value='Alumno', bootstyle='dark') 
        # self.alumno.grid(column=1, row=0, padx=30, pady=[10,5], sticky='we')
        #! TEXTO
        # self.usuarioid_label = ttk.Label(frame_uno, text='Codigo', bootstyle='dark')
        # self.usuarioid_label.grid(column=0, row=1, padx=30, pady=5, sticky='we')
        alumno_label = ttk.Label(frame_uno, text='Alumno', bootstyle='dark')
        alumno_label.grid(column=0, row=2, padx=30, pady=5, sticky='we')
        sexo_label = ttk.Label(frame_uno, text='Sexo', bootstyle='dark')
        sexo_label.grid(column=0, row=3, padx=30, pady=5, sticky='we')
        nivel_label = ttk.Label(frame_uno, text='Nivel', bootstyle='dark')
        nivel_label.grid(column=0, row=4, padx=30, pady=5, sticky='we')
        grado_label = ttk.Label(frame_uno, text='Grado', bootstyle='dark')
        grado_label.grid(column=0, row=5, padx=30, pady=5, sticky='we')
        seccion_label = ttk.Label(frame_uno, text='Seccion', bootstyle='dark')
        seccion_label.grid(column=0, row=6, padx=30, pady=[5,10], sticky='we')
        #! ENTRADAS
        # self.usuarioid_entry = ttk.Entry(frame_uno, textvariable=self.alumnoid, width=20, bootstyle='primary')
        # self.usuarioid_entry.grid(column=1, row=1, padx=5 ,pady=5, sticky='w')
        alumno_entry = ttk.Entry(frame_uno, textvariable=self.alumno, width=20, bootstyle='primary')
        alumno_entry.grid(column=1, row=2, padx=5 ,pady=5, sticky='w')
        se_list = ["Hombre", "Mujer"]
        sexo_combobox = ttk.Combobox(frame_uno, textvariable=self.sexo ,value=se_list, width=10, bootstyle='primary')
        sexo_combobox.current(1)
        sexo_combobox.state(["readonly"])
        sexo_combobox.grid(column=1, row=3, padx=5 ,pady=5, sticky='w')
        ni_list = ["Primaria", "Secundaria"]
        nivel_combobox = ttk.Combobox(frame_uno, textvariable=self.nivel ,value=ni_list, width=10, bootstyle='primary')
        nivel_combobox.current(0)
        nivel_combobox.state(["readonly"])
        nivel_combobox.grid(column=1, row=4, padx=5 ,pady=5, sticky='w')
        gra_list = ["PRIMERO", "SEGUNDO", "TERCERO", "CUARTO", "QUINTO", "SEXTO"]
        grado_combobox = ttk.Combobox(frame_uno, textvariable=self.grado ,value=gra_list, width=10, bootstyle='primary')
        grado_combobox.current(0)
        grado_combobox.state(["readonly"])
        grado_combobox.grid(column=1, row=5, padx=5 ,pady=5, sticky='w')
        sec_list = ["A", "B", "C", "D", "E"]
        seccion_combobox = ttk.Combobox(frame_uno, textvariable=self.seccion ,value=sec_list, width=10, bootstyle='primary')
        seccion_combobox.current(0)
        seccion_combobox.state(["readonly"])
        seccion_combobox.grid(column=1, row=6, padx=5 ,pady=[5,10], sticky='w')
        #! Botones
        update_boton = ttk.Button(frame_uno, text='Actualizar Fila', width=15, 
                                  command=self.actualizar_fila, bootstyle='primary-outline')
        update_boton.grid(column=0, row=7, padx=30, pady=10, sticky='w')
        clear_boton = ttk.Button(frame_uno, text='Limpiar Campos', width=15, command=self.limpiar_campos, bootstyle='primary-outline')
        clear_boton.grid(column=1, row=7, padx=5, pady=10, sticky='w')
            
    def seccion_dos(self, frame_dos):
        frame_busqueda = ttk.Frame(frame_dos)
        frame_busqueda.grid(column=0, row=0, padx=5, pady=1, sticky='nsew')
        
        l_columna = ("Codigo", "Alumno", "Sexo", "Nivel", "Grado", "Seccion")
        buscar_palabra = ttk.Combobox(frame_busqueda, width=15, value=l_columna, 
                                      textvariable=self.nombre_columna, bootstyle='success')
        buscar_palabra.current(0)
        buscar_palabra.state(["readonly"])
        buscar_palabra.pack(side='left', padx=4)
        
        palaba_entry = ttk.Entry(frame_busqueda, textvariable=self.palabra, width=40, bootstyle='success')
        palaba_entry.pack(side='left', padx=4)

        busc_boton = ttk.Button(frame_busqueda, text='Buscar', width=10, 
                                command=self.buscar, bootstyle='success')
        busc_boton.pack(side='left', padx=4)

        save_boton = ttk.Button(frame_busqueda, width=20, image=self.photo2, 
                                bootstyle='success-link')
        save_boton.pack(side='left', padx=4)

        show_boton = ttk.Button(frame_busqueda, image=self.photo1,
                                command=self.mostrar_tabla, bootstyle='success-link')
        show_boton.pack(side='right', padx=4)
        
        #! TABLA
        frame_tabla = ttk.LabelFrame(frame_dos, text='Tabla', bootstyle='primary')
        frame_tabla.grid(column=0, row=1, padx=5, pady=[1,5] ,sticky='nsew')
        frame_tabla.columnconfigure(1 , weight=15)
        frame_tabla.rowconfigure(0 , weight=15)
        
        self.tabla = ttk.Treeview(frame_tabla, bootstyle='primary')
        self.tabla.grid(column=1, row=0, sticky='nsew',padx=5, pady=5)
        #! SCROLLBARS
        ladox = ttk.Scrollbar(frame_tabla, orient='horizontal', command=self.tabla.xview, bootstyle='primary-round')
        ladox.grid(column=1, row=1, sticky='ew', padx=5)
        ladoy = ttk.Scrollbar(frame_tabla, orient='vertical', command=self.tabla.yview, bootstyle='primary-round')
        ladoy.grid(column=0, row=0, sticky='ns', pady=5)
        self.tabla.configure(xscrollcommand=ladox.set, yscrollcommand=ladoy.set)
        #! COLUMNAS
        self.tabla['columns'] = ('AlumnoId', 'Alumno', 'Sexo', 'Nivel', 'Grado', 'Seccion')
        self.tabla.column('#0', minwidth=60, width=60, anchor='center')
        self.tabla.column('#1', minwidth=100, width=100, anchor='center')
        self.tabla.column('#2', minwidth=90, width=110, anchor='center')
        self.tabla.column('#3', minwidth=120, width=120, anchor='center')
        self.tabla.column('#4', minwidth=200, width=200, anchor='w')
        self.tabla.column('#5', minwidth=200, width=200, anchor='w')
        self.tabla.column('#6', minwidth=100, width=105, anchor='w')

        self.tabla.heading('#0', text='Nº', anchor='center')
        self.tabla.heading('#1', text='Codigo', anchor='center')
        self.tabla.heading('#2', text='Alumno', anchor='center')
        self.tabla.heading('#3', text='Sexo', anchor='center')
        self.tabla.heading('#4', text='Nivel', anchor='center')
        self.tabla.heading('#5', text='Grado', anchor='center')
        self.tabla.heading('#6', text='Seccion', anchor='center')
        
        self.tabla.bind("<<TreeviewSelect>>", self.obtener_alumno)
        self.tabla.bind("<Double-1>", self.eliminar_alumno)

    def mostrar_tabla(self):
        self.limpiar_campos()
        l_datos = self.bd.show_alumnos()
        self.tabla.delete(*self.tabla.get_children())
        i = -1
        for fila in l_datos:
            i = i+1
            self.tabla.insert('', i,text=i+1, values=fila[0:7])
            
    def obtener_alumno(self, event):
        item_selec = self.tabla.focus()
        diccionario_alumno = self.tabla.item(item_selec)
        if 'values' in diccionario_alumno and len(diccionario_alumno['values']) >= 2:
            if diccionario_alumno['values'][6] == 'Alumno':
                self.alumno.set(diccionario_alumno['values'][1])
                self.sexo.set(diccionario_alumno['values'][2])
                self.nivel.set(diccionario_alumno['values'][3])
                self.grado.set(diccionario_alumno['values'][4])
                self.seccion.set(diccionario_alumno['values'][5])
                
            elif diccionario_alumno['values'][6] != 'Alumno':
                messagebox.showerror('ERROR', 'Error al Seleccionar')
                """ 
                self.alumnoid.set(diccionario_alumno['values'][0])
                self.alumno.set(diccionario_alumno['values'][1])
                self.sexo.set(diccionario_alumno['values'][2])
                self.nivel.set(diccionario_alumno['values'][3])
                self.grado.set(diccionario_alumno['values'][4])
                self.seccion.set(diccionario_alumno['values'][5])
                """
        else:
            self.limpiar_campos()            
            
    def limpiar_campos(self):
        # self.alumnoid.set('')
        self.alumno.set('')
        self.sexo.set('')
        self.nivel.set('')
        self.grado.set('')
        self.seccion.set('')
        # self.seccion_uno(self.frame1)

    def actualizar_fila(self):
        item_l = self.tabla.focus()
        diccionario_alumno = self.tabla.item(item_l)
        if len(diccionario_alumno['values']) != 0:
            codigo = diccionario_alumno['values'][0]
            l_datos = self.bd.show_alumnos()
            for fila in l_datos:
                id_alumno = fila[0]
                if id_alumno == codigo and codigo != None:
                    alumno = self.alumno.get()
                    sexo = self.sexo.get()
                    nivel = self.nivel.get()
                    grado = self.grado.get()
                    seccion = self.seccion.get()
                    confirmar_box = messagebox.askokcancel('Información', 'Se modificará la fila seleccionada')
                    if alumno and sexo and nivel and grado and seccion != '' and confirmar_box == True:
                        self.bd.update_alumno(alumno, sexo, nivel, grado, seccion, codigo)
                        messagebox.showinfo('Información', 'Fila modificada')
                        self.mostrar_tabla()
        else:
            messagebox.showerror('ERROR', 'Falta Rellenar')

    
    def eliminar_alumno(self, event):
        self.limpiar_campos()
        l_item = self.tabla.selection()[0]
        diccionario_fila = self.tabla.item(l_item)
        question_box = messagebox.askquestion('Información', '¿Desea eliminar la fila?')
        if question_box == 'yes':
            self.tabla.delete(l_item)
            self.limpiar_campos()
            self.bd.delete_alumno(diccionario_fila['values'][0])
            messagebox.showinfo('Información', 'Fila Eliminada')
    
    def buscar(self):
        self.limpiar_campos()
        palabra = self.palabra.get()
        columna = self.nombre_columna.get()
        if palabra != '':
            l_datos = self.bd.show_alumnos(columna, palabra)
            self.tabla.delete(*self.tabla.get_children())
            i = -1
            for fila in l_datos:
                i = i+1
                self.tabla.insert('', i,text=i+1, values=fila[0:7])
        else:
            messagebox.showerror('ERROR', 'No se agrego una busqueda')
    
    def guardar_datos(self):
        self.limpiar_campos()
        self.informe.save_libros()
        messagebox.showinfo('Informacion', 'Datos guardados')