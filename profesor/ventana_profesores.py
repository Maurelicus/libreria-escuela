from PIL import Image, ImageTk
from tkinter import messagebox
import ttkbootstrap as ttk
import tkinter  as tk

from data.conexion_sqlite import Comunicacion
from data.informes import Informes

class VentanaProfesores():
    def __init__(self):
        self.profesor = tk.StringVar()
        self.correo = tk.StringVar()
        self.celular = tk.StringVar()
        self.codigo = tk.StringVar()
        self.palabra = tk.StringVar()
        self.nombre_columna = tk.StringVar()
        self.bd = Comunicacion()
        self.photo1 = ImageTk.PhotoImage(Image.open("images/reload.png"))
        self.photo2 = ImageTk.PhotoImage(Image.open("images/excel.png"))
        self.informe = Informes()
        
    def seccion_uno(self, frame_datos):
        #! TEXTO
        codigo_label = ttk.Label(frame_datos, text='Codigo', bootstyle='dark')
        codigo_label.grid(column=0, row=1, padx=30, pady=5, sticky='we')
        profesor_label = ttk.Label(frame_datos, text='Profesor', bootstyle='dark')
        profesor_label.grid(column=0, row=2, padx=30, pady=5, sticky='we')
        celular_label = ttk.Label(frame_datos, text='Celular', bootstyle='dark')
        celular_label.grid(column=0, row=3, padx=30, pady=5, sticky='we')
        correo_label = ttk.Label(frame_datos, text='Correo', bootstyle='dark')
        correo_label.grid(column=0, row=4, padx=30, pady=5, sticky='we')
        #! ENTRADAS
        codigo_entry = ttk.Entry(frame_datos, textvariable=self.codigo, width=20, bootstyle='primary')
        codigo_entry.grid(column=1, row=1, padx=5 ,pady=5, sticky='w')
        profesor_entry = ttk.Entry(frame_datos, textvariable=self.profesor, width=20, bootstyle='primary')
        profesor_entry.grid(column=1, row=2, padx=5 ,pady=5, sticky='w')
        celular_entry = ttk.Entry(frame_datos, textvariable=self.celular, width=20, bootstyle='primary')
        celular_entry.grid(column=1, row=3, padx=5 ,pady=5, sticky='w')
        correo_entry = ttk.Entry(frame_datos, textvariable=self.correo, width=20, bootstyle='primary')
        correo_entry.grid(column=1, row=4, padx=5 ,pady=5, sticky='w')
        #! Botones
        update_boton = ttk.Button(frame_datos, text='Modificar Profesor', width=15, 
                                  command=self.actualizar_profesor, bootstyle='primary-outline')
        update_boton.grid(column=0, row=5, padx=30, pady=10, sticky='w')
        clear_boton = ttk.Button(frame_datos, text='Limpiar Campos', width=15,
                                 command=self.limpiar_campos, bootstyle='primary-outline')
        clear_boton.grid(column=1, row=5, padx=5, pady=10, sticky='w')
        add_boton = ttk.Button(frame_datos, text='Añadir Profesor', width=15,
                               command=self.agregar_profesor, bootstyle='primary-outline')
        add_boton.grid(column=0, row=6, padx=30, pady=10, sticky='w')

    def seccion_dos(self, frame_vista):
        frame_busqueda = ttk.Frame(frame_vista)
        frame_busqueda.grid(column=0, row=0, padx=5, pady=1, sticky='nsew')
        
        l_columna = ("Codigo", "Profesor")
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
                                command=self.guardar_datos,bootstyle='success-link')
        save_boton.pack(side='left', padx=4)

        show_boton = ttk.Button(frame_busqueda, image=self.photo1,
                                command=self.mostrar_tabla, bootstyle='success-link')
        show_boton.pack(side='right', padx=4)
        
        #! TABLA
        frame_tabla = ttk.LabelFrame(frame_vista, text='Tabla', bootstyle='primary')
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
        self.tabla['columns'] = ('Profesor', 'Correo','Celular','Codigo')
        self.tabla.column('#0', minwidth=60, width=60, anchor='center')
        self.tabla.column('#1', minwidth=200, width=250, anchor='w')
        self.tabla.column('#2', minwidth=200, width=250, anchor='w')
        self.tabla.column('#3', minwidth=120, width=150, anchor='w')
        self.tabla.column('#4', minwidth=100, width=120, anchor='w')

        self.tabla.heading('#0', text='Nº', anchor='center')
        self.tabla.heading('#1', text='Profesor', anchor='center')
        self.tabla.heading('#2', text='Correo', anchor='center')
        self.tabla.heading('#3', text='Celular', anchor='center')
        self.tabla.heading('#4', text='Codigo', anchor='center')
        
        self.tabla.bind("<<TreeviewSelect>>", self.obtener_profesor)
        self.tabla.bind("<Double-1>", self.eliminar_profesor)

    def mostrar_tabla(self):
        self.limpiar_campos()
        l_datos = self.bd.show_profesores()
        self.tabla.delete(*self.tabla.get_children())
        i = -1
        for fila in l_datos:
            i = i+1
            self.tabla.insert('', i,text=i+1, values=fila[0:5], tags=fila[4])
            
    def obtener_profesor(self, event):
        item_selec = self.tabla.focus()
        diccionario_profesor = self.tabla.item(item_selec)
        if 'values' in diccionario_profesor and len(diccionario_profesor['values']) != 0:
            self.profesor.set(diccionario_profesor['values'][0])
            self.correo.set(diccionario_profesor['values'][1])
            self.celular.set(diccionario_profesor['values'][2])
            self.codigo.set(diccionario_profesor['values'][3])
                
        else:
            self.limpiar_campos()
            
    def limpiar_campos(self):
        self.codigo.set('')
        self.profesor.set('')
        self.correo.set('')
        self.celular.set('')

    def actualizar_profesor(self):
        #? ALUMNOID EN EL 5
        item_l = self.tabla.focus()
        diccionario_profesor = self.tabla.item(item_l)
        if len(diccionario_profesor['values']) >= 3:
            tabla_profesores = self.bd.show_profesores()
            lista_codigos = []
            for fila in tabla_profesores:
                lista_codigos.append(fila[3])
                
            idprfesor_tabla = diccionario_profesor['values'][3]
            for fila in tabla_profesores:
                profesorid_bd = fila[3]
                if profesorid_bd == idprfesor_tabla and idprfesor_tabla != '':
                    profesor = self.profesor.get()
                    correo = self.correo.get()
                    celular = self.celular.get()
                    codigo = self.codigo.get()
                    n_codigo = 'n'+str(codigo)
                    
                    confirmar_box = messagebox.askokcancel('Información', 'Se modificará la fila seleccionada')
                    if codigo and profesor and correo and celular != '' and confirmar_box == True:
                        # cuando no modifico el codigo
                        if str(idprfesor_tabla) == str(codigo):
                            self.bd.update_profesor(idprfesor_tabla, codigo, profesor, correo, celular)
                            messagebox.showinfo('Información', 'Fila modificada')
                            self.mostrar_tabla()
                        # cuando modifico el codigo
                        elif codigo not in lista_codigos:
                            # print(codigo)
                            indicador = 'u'
                            indicador2 = 'n'
                            if indicador in codigo and indicador2 not in codigo:
                                self.bd.update_profesor(idprfesor_tabla, codigo, profesor, correo, celular)
                                messagebox.showinfo('Información', 'Fila modificada')
                                self.mostrar_tabla()
                            elif indicador not in codigo and indicador2 in codigo:
                                self.bd.update_profesor(idprfesor_tabla, codigo, profesor, correo, celular)
                                messagebox.showinfo('Información', 'Fila modificada')
                                self.mostrar_tabla()
                            elif indicador2 not in codigo and indicador not in codigo:
                                self.bd.update_alumno(idprfesor_tabla, n_codigo, profesor, correo, celular)
                                messagebox.showinfo('Información', 'Fila modificada')
                                self.mostrar_tabla()
                            elif indicador2 in codigo and indicador in codigo:
                                self.bd.update_alumno(idprfesor_tabla, codigo, profesor, correo, celular)
                                messagebox.showinfo('Información', 'Fila modificada')
                                self.mostrar_tabla()
                        elif codigo in lista_codigos:
                            messagebox.showerror('ERROR', 'Codigo Existente')
                    else:
                        messagebox.showerror('ERROR', 'Falta Rellenar datos')
                
        elif len(diccionario_profesor['values']) == 0:
            messagebox.showerror('ERROR', 'Selecciona un profesor')
        else:
            messagebox.showerror('ERROR', 'Falta Rellenar')

    
    def eliminar_profesor(self, event):
        self.limpiar_campos()
        l_item = self.tabla.selection()[0]
        diccionario_fila = self.tabla.item(l_item)
        question_box = messagebox.askquestion('Información', '¿Desea eliminar la fila?')
        if question_box == 'yes':
            self.tabla.delete(l_item)
            self.limpiar_campos()
            self.bd.delete_profesor(diccionario_fila['values'][3])
            messagebox.showinfo('Información', 'Fila Eliminada')
    
    def agregar_profesor(self):
        # print('falta')
        profesor = self.profesor.get()
        correo = self.correo.get()
        celular = self.celular.get()
        codigo = self.codigo.get()
        if profesor and codigo != '':
            tabla_profesoresbd = self.bd.show_profesores()
            lista_codigos = []
            tipo = 'Profesor'
            n_codigo = 'n'+str(codigo)
            for fila in tabla_profesoresbd:
                lista_codigos.append(fila[3])
            
            question_box = messagebox.askquestion('Información', '¿Desea agregar la fila?')
            if codigo not in lista_codigos and question_box == 'yes':
                indicador = 'u'
                indicador2 = 'n'
                if indicador not in codigo and indicador2 not in codigo:
                    self.bd.append_profesor(n_codigo, profesor, correo, celular, tipo)
                    messagebox.showinfo('Información', 'Profesor agregado')
                    self.limpiar_campos()
                    self.mostrar_tabla()
                elif indicador in codigo and indicador2 not in codigo:
                    self.bd.append_profesor(n_codigo, profesor, correo, celular, tipo)
                    messagebox.showinfo('Información', 'Profesor agregado')
                    self.limpiar_campos()
                    self.mostrar_tabla()
                elif indicador2 in codigo:
                    self.bd.append_profesor(codigo, profesor, correo, celular, tipo)
                    messagebox.showinfo('Información', 'Profesor agregado')
                    self.limpiar_campos()
                    self.mostrar_tabla()

                else:
                    messagebox.showerror('ERROR', 'Codigo erroneo')
            elif codigo in lista_codigos:
                messagebox.showerror('ERROR', 'Codigo Existente')
        else:
            messagebox.showerror('ERROR', 'Falta Rellenar')
    def buscar(self):
        self.limpiar_campos()
        palabra = self.palabra.get()
        columna = self.nombre_columna.get()
        
        if palabra != '':
            l_datos = self.bd.search_profesores(columna, palabra)
            self.tabla.delete(*self.tabla.get_children())
            i = -1
            for fila in l_datos:
                i = i+1
                self.tabla.insert('', i,text=i+1, values=fila[0:5], tags=fila[4])

        else:
            messagebox.showerror('ERROR', 'No se agrego una busqueda')
            
    def guardar_datos(self):
        self.limpiar_campos()
        self.informe.save_profesores()
        messagebox.showinfo('Informacion', 'Datos guardados')
