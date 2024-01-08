from tkinter import *
from tkinter import ttk
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
        
        self.master.columnconfigure(1, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.bd = Comunicacion()        
        self.widgets()
        
    def widgets(self):
        self.frame_uno = ttk.LabelFrame(self.master,text='Funciones', height=300, width=800)
        self.frame_uno.grid(column=0, row=0, sticky='nsew')
        self.frame_dos = ttk.LabelFrame(self.master, text='Tabla', height=300, width=8)
        self.frame_dos.grid(column=1, row=0, sticky='nsew')
        #! CONFIGURACIONES
        self.frame_uno.columnconfigure([0,1], weight=2)
        self.frame_uno.rowconfigure([0,1], weight=2)
        self.frame_dos.columnconfigure(0, weight=1)
        self.frame_dos.rowconfigure(0, weight=1)
        #! CONTENEDORES
        datos_frame = ttk.LabelFrame(self.frame_uno, text='Datos')
        datos_frame.grid(column=1, row=0, padx=20, pady=[10,20])
        # opciones_frame = ttk.LabelFrame(self.frame_uno, text='Acciones')
        # opciones_frame.grid(column=1, row=1, padx=20, pady=[20,10])
        #! TEXTO
        reminente_label = ttk.Label(datos_frame, text='Reminente')
        reminente_label.grid(column=0, row=1, padx=5, pady=[10,5])
        año_recepcion = ttk.Label(datos_frame, text='Año de recepcion')
        año_recepcion.grid(column=0, row=2, padx=5, pady=5)
        nivel_educativo = ttk.Label(datos_frame, text='Nivel educativo')
        nivel_educativo.grid(column=0, row=3, padx=5, pady=5)
        titulo = ttk.Label(datos_frame, text='Titulo')
        titulo.grid(column=0, row=4, padx=5, pady=5)
        autor = ttk.Label(datos_frame, text='Autor')
        autor.grid(column=0, row=5, padx=5, pady=5)
        editorial = ttk.Label(datos_frame, text='Editorial')
        editorial.grid(column=0, row=6, padx=5, pady=5)
        año_edicion = ttk.Label(datos_frame, text='Año de edicion')
        año_edicion.grid(column=0, row=7, padx=5, pady=5)
        condicion_libro = ttk.Label(datos_frame, text='Condicion')
        condicion_libro.grid(column=0, row=8, padx=5, pady=5)
        cantidad = ttk.Label(datos_frame, text='Cantidad')
        cantidad.grid(column=0, row=9, padx=5, pady=[5,10])
        #! ENTRADAS
        reminente_entry = ttk.Entry(datos_frame, textvariable=self.remitente)
        reminente_entry.grid(column=1, row=1, padx=5 ,pady=[10,5])
        añorecepcion_entry = ttk.Entry(datos_frame, textvariable=self.año_recepcion)
        añorecepcion_entry.grid(column=1, row=2, padx=5 ,pady=5)
        niveleducativo_entry = ttk.Entry(datos_frame, textvariable=self.nivel_educativo)
        niveleducativo_entry.grid(column=1, row=3, padx=5 ,pady=5)
        titulo_entry = ttk.Entry(datos_frame, textvariable=self.titulo)
        titulo_entry.grid(column=1, row=4, padx=5 ,pady=5)
        autor_entry = ttk.Entry(datos_frame, textvariable=self.autor)
        autor_entry.grid(column=1, row=5, padx=5 ,pady=5)
        editorial_entry = ttk.Entry(datos_frame, textvariable=self.editorial)
        editorial_entry.grid(column=1, row=6, padx=5 ,pady=5)
        añoedicion_entry = ttk.Entry(datos_frame, textvariable=self.año_edicion)
        añoedicion_entry.grid(column=1, row=7, padx=5 ,pady=5)
        condicionlibro_entry = ttk.Entry(datos_frame, textvariable=self.condicion_libro)
        condicionlibro_entry.grid(column=1, row=8, padx=5 ,pady=5)
        cantidad_entry = ttk.Entry(datos_frame, textvariable=self.cantidad)
        cantidad_entry.grid(column=1, row=9, padx=5 ,pady=[5,10])
        #! BOTONES
        show_boton = ttk.Button(datos_frame, text='Refrescar', width=20,
                                command=self.actualizar_tabla)
        show_boton.grid(column=0, row=10, padx=5, pady=[10,5])
        clear_boton = ttk.Button(datos_frame, text='Limpiar campos', width=20,
                                command=self.limpiar_campos)
        clear_boton.grid(column=1, row=10, padx=5, pady=[10,5])
        update_boton = ttk.Button(datos_frame, text='Actualizar fila', width=20,
                                command=self.actualizar_fila)
        update_boton.grid(column=0, row=12, padx=5, pady=[5,10])
        #! ESTILO
        estilo_tabla = ttk.Style(self.master)
        self.master.tk.call("source", "forest-dark.tcl")
        estilo_tabla.theme_use("forest-dark")
        #! TABLA
        self.tabla = ttk.Treeview(self.frame_dos)
        self.tabla.grid(column=0, row=0, sticky='nsew',padx=5, pady=[10,5])
        #! SCROLLBARS
        ladox = ttk.Scrollbar(self.frame_dos, orient='horizontal', command=self.tabla.xview)
        ladox.grid(column=0, row=1, sticky='ew', padx=5)
        ladoy = ttk.Scrollbar(self.frame_dos, orient='vertical', command=self.tabla.yview)
        ladoy.grid(column=1, row=0, sticky='ns', pady=[10,5])
        self.tabla.configure(xscrollcommand=ladox.set, yscrollcommand=ladoy.set)
        #! COLUMNAS
        self.tabla['columns'] = ('Remitente', 'Añorecepcion', 'Niveleducativo', 'Titulo', 'Autor', 'Editorial', 'Añoedicion', 'Condicion', 'Cantidad')
        self.tabla.column('#0', minwidth=40, width=40, anchor='center')
        self.tabla.column('#1', minwidth=100, width=100, anchor='center')
        self.tabla.column('#2', minwidth=100, width=120, anchor='center')
        self.tabla.column('#3', minwidth=100, width=125, anchor='center')
        self.tabla.column('#4', minwidth=100, width=105, anchor='center')
        self.tabla.column('#5', minwidth=100, width=105, anchor='center')
        self.tabla.column('#6', minwidth=100, width=105, anchor='center')
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
            # print(fila[0])
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
                if remitente and añorecepcion and niveleducativo and titulo and autor and editorial and añoedicion and condicionlibro and cantidad!='':
                    self.bd.actualizar_fila(id, remitente, añorecepcion, niveleducativo, titulo, autor, editorial, añoedicion, condicionlibro, cantidad)
                    self.actualizar_tabla()
        
if __name__ == "__main__":
    ventana = Tk()
    ventana.title('')
    ventana.minsize(width=1000, height=600)
    ventana.geometry('1200x620')
    app = Ventana(ventana)
    app.mainloop()
    