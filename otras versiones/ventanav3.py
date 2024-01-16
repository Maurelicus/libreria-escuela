import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

from conexion_sqlite import Comunicacion
import g1_widgets as gw1

class Ventana(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.remitente = tk.StringVar()
        self.año_recepcion = tk.StringVar()
        self.nivel_educativo = tk.StringVar()
        self.titulo = tk.StringVar()
        self.autor = tk.StringVar()
        self.editorial = tk.StringVar()
        self.año_edicion = tk.StringVar()
        self.condicion_libro = tk.StringVar()
        self.cantidad = tk.StringVar()
        self.palabra = tk.StringVar()
        self.nombre_columna = tk.StringVar()
        self.bd = Comunicacion()
        self.v1 = gw1.Widgets1v()
        self.mytabcontrol = ttk.Notebook(self)
        self.widgets()
        
    def widgets(self):
        #! Funciones label
        
        mytab1 = ttk.LabelFrame(self.mytabcontrol, text='Libros') # L2
        mytab1.columnconfigure(0, weight=1, minsize=440)
        mytab1.columnconfigure(1, weight=1)
        mytab1.rowconfigure(0, weight=1)
        
        mytab2 = ttk.Frame(self.mytabcontrol)

        self.mytabcontrol.add(mytab1, text ='Libros')
        self.mytabcontrol.add(mytab2, text ='Laminas')
        self.mytabcontrol.grid(column=0, row=0,padx=10, pady=10, sticky='nswe')
        
        
        
        frame_uno = ttk.LabelFrame(mytab1, text='Funciones')
        frame_uno.grid(column=0, row=0, padx=5, pady=5, sticky='n')
        frame_uno.columnconfigure(0, weight=1)
        frame_uno.rowconfigure(0, weight=1)
        #* Widgets de funciones
        """ 
        lista_atributos1 = [self.remitente, self.año_recepcion, 
                        self.nivel_educativo, self.titulo, 
                        self.autor, self.editorial, self.año_edicion, 
                        self.condicion_libro, self.cantidad]
        lista_metodos1 = [self.limpiar_campos, self.actualizar_fila, 
                        self.agregar_fila]
        gw1.seccion_uno(frame_uno, lista_metodos1, lista_atributos1)
        """
        
        #* Widgets de tabla
        frame_dos = ttk.LabelFrame(mytab1, text='Visualizacion')
        frame_dos.grid(column=1, row=0, sticky='nsew')
        frame_dos.columnconfigure(0, weight=1)
        frame_dos.rowconfigure(0, weight=0)
        frame_dos.rowconfigure(1, weight=10)
        
        self.v1.widgets(frame_uno, frame_dos)
        """ 
        #! Tabla Label
        lista_atributos2 = [self.palabra, self.nombre_columna]
        lista_metodos2 = [self.actualizar_tabla, self.buscador, self.obtener_fila, self.eliminar_datos]
        self.photo1 = ImageTk.PhotoImage(Image.open("reload.png"))
        self.photo2 = ImageTk.PhotoImage(Image.open("excel.png"))
        #* Widgets de tabla
        #! TABLA
        """ 
        """
        frame_tabla = ttk.LabelFrame(frame_dos, text='Tabla')
        frame_tabla.grid(column=0, row=1, padx=5, pady=5 ,sticky='nsew')
        frame_tabla.columnconfigure(1 , weight=10)
        frame_tabla.rowconfigure(0 , weight=10)
        
        self.tabla = ttk.Treeview(frame_tabla)
        self.tabla.grid(column=1, row=0, sticky='nsew',padx=5, pady=5)
        gw1.seccion_dos(frame_dos, frame_tabla, lista_metodos2, lista_atributos2, self.photo1, self.photo2, self.tabla)
        """
        
    """ 
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
    
    def buscador(self):
        self.limpiar_campos()
        palabra = self.palabra.get()
        columna = self.nombre_columna.get()
        # print(columna)
        # print(palabra)
        l_datos = self.bd.buscador(columna, palabra)
        self.tabla.delete(*self.tabla.get_children())
        i = -1
        for fila in l_datos:
            i = i+1
            self.tabla.insert('', i,text=fila[0], values=fila[1:11])
    """