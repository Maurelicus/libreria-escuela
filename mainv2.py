from tkinter import *
from tkinter import ttk, messagebox
from conexion_sqlite import Comunicacion

class Ventana(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        self.remitente = StringVar()
        self.año_recepcion = StringVar()
        self.nivel_educativo = StringVar()
        self.titulo = StringVar()
        self.autor = StringVar()
        self.editorial = StringVar()
        self.año_edicion = StringVar()
        self.condicion_libro = StringVar()
        self.cantidad = StringVar()
        self.bd = Comunicacion()        
        self.widgets()
        
        self.master.columnconfigure(0, weight=1, minsize=440)
        self.master.columnconfigure(1, weight=1)
        self.master.rowconfigure(0, weight=1)
        
    def widgets(self):
        #! Funciones label
        # height=altura/width=ancho
        self.frame_operaciones = ttk.LabelFrame(self.master,text='Funciones')
        self.frame_operaciones.grid(column=0, row=0, sticky='ns', padx=10)
        self.frame_operaciones.columnconfigure(0, weight=1)
        self.frame_operaciones.rowconfigure(0, weight=1)
        frame_uno = ttk.LabelFrame(self.frame_operaciones, text='Frame 1')
        frame_uno.grid(column=1, row=0, padx=5, pady=15)
        #! Tabla Label
        self.frame_tabla = ttk.LabelFrame(self.master, text='Tabla')
        self.frame_tabla.grid(column=1, row=0, sticky='nsew')
        self.frame_tabla.columnconfigure(0, weight=1)
        self.frame_tabla.rowconfigure(1, weight=1)
        #* Widgets de funciones
        #! TEXTO
        reminente_label = ttk.Label(frame_uno, text='Remitente')
        reminente_label.grid(column=0, row=1, padx=5, pady=[10,5])
        año_recepcion = ttk.Label(frame_uno, text='Año de Recepcion')
        año_recepcion.grid(column=0, row=2, padx=5, pady=5)
        nivel_educativo = ttk.Label(frame_uno, text='Nivel Educativo')
        nivel_educativo.grid(column=0, row=3, padx=5, pady=5)
        titulo = ttk.Label(frame_uno, text='Titulo')
        titulo.grid(column=0, row=4, padx=5, pady=5)
        autor = ttk.Label(frame_uno, text='Autor')
        autor.grid(column=0, row=5, padx=5, pady=5)
        editorial = ttk.Label(frame_uno, text='Editorial')
        editorial.grid(column=0, row=6, padx=5, pady=5)
        año_edicion = ttk.Label(frame_uno, text='Año de edicion')
        año_edicion.grid(column=0, row=7, padx=5, pady=5)
        condicion_libro = ttk.Label(frame_uno, text='Condicion')
        condicion_libro.grid(column=0, row=8, padx=5, pady=5)
        cantidad = ttk.Label(frame_uno, text='Cantidad')
        cantidad.grid(column=0, row=9, padx=5, pady=[5,10])
        #! ENTRADAS
        reminente_entry = ttk.Entry(frame_uno, textvariable=self.remitente)
        reminente_entry.grid(column=1, row=1, padx=5 ,pady=[10,5])
        añorecepcion_entry = ttk.Entry(frame_uno, textvariable=self.año_recepcion)
        añorecepcion_entry.grid(column=1, row=2, padx=5 ,pady=5)
        nied_list = ["Primaria", "Secundaria"]
        niveleducativo_combobox = ttk.Combobox(frame_uno, textvariable=self.nivel_educativo ,value=nied_list)
        niveleducativo_combobox.grid(column=1, row=3, padx=5 ,pady=5)
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
        cantidad_entry = ttk.Entry(frame_uno, textvariable=self.cantidad)
        cantidad_entry.grid(column=1, row=9, padx=5 ,pady=[5,10])
        #! BOTONES
        clear_boton = ttk.Button(frame_uno, text='Limpiar campos', width=20,
                                command=self.limpiar_campos)
        clear_boton.grid(column=1, row=10, padx=5, pady=[5,10])
        update_boton = ttk.Button(frame_uno, text='Actualizar fila', width=20,
                                command=self.actualizar_fila)
        update_boton.grid(column=0, row=10, padx=5, pady=[5,10])
        add_boton = ttk.Button(frame_uno, text='Añadir fila', width=20,
                            command=self.agregar_fila)
        add_boton.grid(column=0, row=11, padx=5, pady=[5,10])
        
        #! ESTILO
        estilo_tabla = ttk.Style(self.master)
        self.master.tk.call("source", "forest-dark.tcl")
        estilo_tabla.theme_use("forest-dark")
        #* Widgets de tabla
        show_boton = ttk.Button(self.frame_tabla, text='Refrescar',
                                command=self.actualizar_tabla)
        show_boton.grid(column=0, row=0, padx=5, pady=[10,5], sticky='e')
        #! TABLA
        self.tabla = ttk.Treeview(self.frame_tabla)
        self.tabla.grid(column=0, row=1, sticky='nsew',padx=5, pady=[1,5])
        #! SCROLLBARS
        ladox = ttk.Scrollbar(self.frame_tabla, orient='horizontal', command=self.tabla.xview)
        ladox.grid(column=0, row=2, sticky='ew', padx=5)
        ladoy = ttk.Scrollbar(self.frame_tabla, orient='vertical', command=self.tabla.yview)
        ladoy.grid(column=1, row=1, sticky='ns', pady=[10,5])
        self.tabla.configure(xscrollcommand=ladox.set, yscrollcommand=ladoy.set)
        #! COLUMNAS
        self.tabla['columns'] = ('Remitente', 'Añorecepcion', 'Niveleducativo', 'Titulo', 'Autor', 'Editorial', 'Añoedicion', 'Condicion', 'Cantidad')
        self.tabla.column('#0', minwidth=60, width=60, anchor='center')
        self.tabla.column('#1', minwidth=100, width=100, anchor='center')
        self.tabla.column('#2', minwidth=100, width=120, anchor='center')
        self.tabla.column('#3', minwidth=120, width=120, anchor='center')
        self.tabla.column('#4', minwidth=200, width=200, anchor='w')
        self.tabla.column('#5', minwidth=200, width=200, anchor='w')
        self.tabla.column('#6', minwidth=100, width=105, anchor='w')
        self.tabla.column('#7', minwidth=100, width=100, anchor='center')
        self.tabla.column('#8', minwidth=90, width=90, anchor='center')
        self.tabla.column('#9', minwidth=90, width=90, anchor='center')
        
        self.tabla.heading('#0', text='Nº', anchor='center')
        self.tabla.heading('#1', text='Remitente', anchor='center')
        self.tabla.heading('#2', text='Año recepcion', anchor='center')
        self.tabla.heading('#3', text='Nivel educativo', anchor='center')
        self.tabla.heading('#4', text='Titulo', anchor='center')
        self.tabla.heading('#5', text='Autor', anchor='center')
        self.tabla.heading('#6', text='Editorial', anchor='center')
        self.tabla.heading('#7', text='Año edicion', anchor='center')
        self.tabla.heading('#8', text='Condicion', anchor='center')
        self.tabla.heading('#9', text='Cantidad', anchor='center')

        self.tabla.bind("<<TreeviewSelect>>", self.obtener_fila)
        self.tabla.bind("<Double-1>", self.eliminar_datos)
        
    def obtener_fila(self, event):
        item_selec = self.tabla.focus()
        diccionario_fila = self.tabla.item(item_selec)
        if 'values' in diccionario_fila and len(diccionario_fila['values']) >= 4:
            self.remitente.set(diccionario_fila['values'][0])
            self.año_recepcion.set(diccionario_fila['values'][1])
            self.nivel_educativo.set(diccionario_fila['values'][2])
            self.titulo.set(diccionario_fila['values'][3])
            self.autor.set(diccionario_fila['values'][4])
            self.editorial.set(diccionario_fila['values'][5])
            self.año_edicion.set(diccionario_fila['values'][6])
            self.condicion_libro.set(diccionario_fila['values'][7])
            self.cantidad.set(diccionario_fila['values'][8])
        else:
            self.limpiar_campos()
            
    def actualizar_tabla(self):
        self.limpiar_campos()
        l_datos = self.bd.mostrar_datos()
        self.tabla.delete(*self.tabla.get_children())
        i = -1
        for fila in l_datos:
            i = i+1
            self.tabla.insert('', i,text=fila[0], values=fila[1:11])
            
    def limpiar_campos(self):
        self.remitente.set('')
        self.año_recepcion.set('')
        self.nivel_educativo.set('')
        self.titulo.set('')
        self.autor.set('')
        self.editorial.set('')
        self.año_edicion.set('')
        self.condicion_libro.set('')
        self.cantidad.set('')
    
    def actualizar_fila(self):
        item_l = self.tabla.focus()
        diccionario_fila = self.tabla.item(item_l)
        id = diccionario_fila['text']
        l_datos = self.bd.mostrar_datos()
        
        for fila in l_datos:
            id_bd = fila[0]
            if id_bd == id and id_bd != None:
                remitente = self.remitente.get()
                añorecepcion = self.año_recepcion.get()
                niveleducativo = self.nivel_educativo.get()
                titulo = self.titulo.get()
                autor = self.autor.get()
                editorial = self.editorial.get()
                añoedicion = self.año_edicion.get()
                condicionlibro = self.condicion_libro.get()
                cantidad = self.cantidad.get()
                pregunta_box = messagebox.askquestion('Informaciòn', '¿Estas seguro?')
                if remitente and niveleducativo and titulo and condicionlibro and cantidad != '' and pregunta_box == 'yes':
                    self.bd.actualizar_fila(id, remitente, añorecepcion, niveleducativo, titulo, autor, editorial, añoedicion, condicionlibro, cantidad)
                    self.actualizar_tabla()
    
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
            self.tabla.insert('', "end", values=datos)
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
            self.bd.eliminar_fila(diccionario_fila['text'])
    
if __name__ == "__main__":
    ventana = Tk()
    ventana.title('')
    ventana.minsize(width=1000, height=600)
    ventana.geometry('1200x650')
    app = Ventana(ventana)
    app.mainloop()
    