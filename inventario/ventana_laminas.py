from tkinter import messagebox
from PIL import Image, ImageTk
import ttkbootstrap as ttk
import tkinter  as tk

from data.conexion_sqlite import Comunicacion
from data.informes import Informes

class VentanaLaminas():
    def __init__(self):
        self.codigo = tk.StringVar()
        self.remitente = tk.StringVar()
        self.año_recepcion = tk.StringVar()
        self.nivel_educativo = tk.StringVar()
        self.titulo = tk.StringVar()
        self.condicion_lamina = tk.StringVar()
        self.cantidad = tk.IntVar()
        self.categoria = tk.StringVar()
        self.palabra = tk.StringVar()
        self.nombre_columna = tk.StringVar()
        self.bd = Comunicacion()
        self.photo1 = ImageTk.PhotoImage(Image.open("images/reload.png"))
        self.photo2 = ImageTk.PhotoImage(Image.open("images/excel.png"))
        self.informe = Informes()
        self.cat_dic = {}
        
    def seccion_uno(self, frame_datos):
        cond_list = ["A", "B", "C"]
        niv_list = ["Primaria", "Secundaria"]
        cat_list = [
            "Literatura", "Historia y Geografia","C.T.A","Matematica",
            "Fisica","Biologia","Quimica","Economia","Lenguage y Comunicacion",
            "Comprension Lectora","Idioma","P.F.C.C","Computacion",
            "Gastronomia","Recreacion","Arte y Musica","Religion",
            "Educacion Fisica","Diccionario","Compendio","Manual","Otros","Falta"
            ]
        a = 1
        for categ in cat_list:
            self.cat_dic[categ] = a
            a = a+1

        #! TEXTO
        ttk.Label(frame_datos, 
            text='DATOS DE LAMINA:', 
            bootstyle='danger'
            ).grid(column=0, row=1, padx=30, pady=10, sticky='w', columnspan=2)

        titulo_label = ttk.Label(frame_datos, text='Titulo', bootstyle='dark')
        titulo_label.grid(column=0, row=2, padx=30, pady=5, sticky='we')
        categoria_label = ttk.Label(frame_datos, text='Categoria', bootstyle='dark')
        categoria_label.grid(column=0, row=3, padx=30, pady=5, sticky='we')
        codigo_label = ttk.Label(frame_datos, text='Codigo', bootstyle='dark')
        codigo_label.grid(column=0, row=4, padx=30, pady=5, sticky='we')
        cantidad_label = ttk.Label(frame_datos, text='Cantidad', bootstyle='dark')
        cantidad_label.grid(column=0, row=5, padx=30, pady=5, sticky='we')

        ttk.Label(frame_datos, 
            text='OTROS DATOS:', 
            bootstyle='danger'
            ).grid(column=0, row=6, padx=30, pady=10, sticky='w', columnspan=2)

        reminente_label = ttk.Label(frame_datos, text='Remitente', bootstyle='dark')
        reminente_label.grid(column=0, row=7, padx=30, pady=5, sticky='we')
        condicionlamina_label = ttk.Label(frame_datos, text='Condicion', bootstyle='dark')
        condicionlamina_label.grid(column=0, row=8, padx=30, pady=5, sticky='we')
        niveleducativo_label = ttk.Label(frame_datos, text='Nivel Educativo', bootstyle='dark')
        niveleducativo_label.grid(column=0, row=9, padx=30, pady=5, sticky='we')
        añorecepcion_label = ttk.Label(frame_datos, text='Año de Recepcion', bootstyle='dark')
        añorecepcion_label.grid(column=0, row=10, padx=30, pady=5, sticky='we')
        #! ENTRADAS
        titulo_entry = ttk.Entry(frame_datos, textvariable=self.titulo, width=20, bootstyle='primary')
        titulo_entry.grid(column=1, row=2, padx=5, pady=5, sticky='w')
        categoria_combobox = ttk.Combobox(frame_datos, textvariable=self.categoria,value=cat_list, width=20, bootstyle='primary')
        categoria_combobox.current(0)
        categoria_combobox.state(["readonly"])
        categoria_combobox.grid(column=1, row=3, padx=5 ,pady=5, sticky='w')
        codigo_entry = ttk.Entry(frame_datos, textvariable=self.codigo, width=10, bootstyle='primary')
        codigo_entry.grid(column=1, row=4, padx=5 ,pady=5, sticky='w')
        cantidad_entry = ttk.Spinbox(frame_datos, textvariable=self.cantidad, from_=0, to=100, width=5, bootstyle='primary')
        cantidad_entry.state(["readonly"])
        cantidad_entry.grid(column=1, row=5, padx=5 ,pady=5, sticky='w')
        
        reminente_entry = ttk.Entry(frame_datos, textvariable=self.remitente, width=10, bootstyle='primary')
        reminente_entry.grid(column=1, row=7, padx=5, pady=5, sticky='w')
        condicionlibro_combobox = ttk.Combobox(frame_datos, textvariable=self.condicion_lamina ,value=cond_list, width=2, bootstyle='primary')
        condicionlibro_combobox.current(0)
        condicionlibro_combobox.state(["readonly"])
        condicionlibro_combobox.grid(column=1, row=8, padx=5, pady=5, sticky='w')
        niveleducativo_combobox = ttk.Combobox(frame_datos, textvariable=self.nivel_educativo ,value=niv_list, width=10, bootstyle='primary')
        niveleducativo_combobox.current(0)
        niveleducativo_combobox.state(["readonly"])
        niveleducativo_combobox.grid(column=1, row=9, padx=5 ,pady=5, sticky='w')
        añorecepcion_entry = ttk.Entry(frame_datos, textvariable=self.año_recepcion, width=7, bootstyle='primary')
        añorecepcion_entry.grid(column=1, row=10, padx=5, pady=5, sticky='w')
        
        #! Botones
        update_boton = ttk.Button(frame_datos, text='Modificar Lamina', width=15, command=self.actualizar_lamina, bootstyle='primary-outline')
        update_boton.grid(column=0, row=11, padx=20, pady=10, sticky='w')
        clear_boton = ttk.Button(frame_datos, text='Limpiar campos', width=15, command=self.limpiar_campos, bootstyle='primary-outline')
        clear_boton.grid(column=1, row=11, padx=5, pady=10, sticky='w')
        add_boton = ttk.Button(frame_datos, text='Añadir Lamina', width=15, command=self.agregar_lamina, bootstyle='primary-outline')
        add_boton.grid(column=0, row=12, padx=20, pady=10, sticky='w')
        baja_boton = ttk.Button(frame_datos, text='Dar de Baja', width=15, command=self.dar_baja, bootstyle='primary-outline')
        baja_boton.grid(column=1, row=12, padx=5, pady=10, sticky='w')

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
                                command=self.buscar_laminas, bootstyle='success')
        busc_boton.pack(side='left', padx=4)
        
        save_boton = ttk.Button(busqueda_frame, width=20, image=self.photo2, 
                                command=self.guardar_laminas, bootstyle='success-link')
        save_boton.pack(side='left', padx=4)

        show_boton = ttk.Button(busqueda_frame, width=20, image=self.photo1,
                                command=self.mostrar_laminas, bootstyle='success-link')
        show_boton.pack(side='right', padx=4)
        #! TABLA
        tabla_frame = ttk.LabelFrame(frame_vista, text='Lista de Laminas', bootstyle='primary')
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

        # White to Light Purple Color Palette
        self.tabla.tag_configure('Literatura', background='#e6e1f9')
        self.tabla.tag_configure('HyG', background='#d5cdf3')
        self.tabla.tag_configure('C.T.A', background='#cdc2f5')
        self.tabla.tag_configure('Matematica', background='#c6b7fe')
        self.tabla.tag_configure('Fisica', background='#bba8ff')
        
        # pastel blue owo Color Palette
        self.tabla.tag_configure('Biologia', background='#bbeaff')
        self.tabla.tag_configure('Quimica', background='#a9e5ff')
        self.tabla.tag_configure('Economia', background='#98ddfc')
        self.tabla.tag_configure('LyC', background='#84d9ff')
        self.tabla.tag_configure('ComLectora', background='#72d3fe')
        
        # shades of sea green 2 Color Palette
        self.tabla.tag_configure('Idioma', background='#c9f9de')
        self.tabla.tag_configure('P.F.C.C', background='#b8f8d4')
        self.tabla.tag_configure('Computacion', background='#a6f6c9')
        self.tabla.tag_configure('Gastronomia', background='#94f4be')
        self.tabla.tag_configure('Recreacion', background='#83f3b4')

        # OrangeCream1 Color Palette
        self.tabla.tag_configure('AyM', background='#ffedc9')
        self.tabla.tag_configure('Religion', background='#ffe7b6')
        self.tabla.tag_configure('EduFis', background='#ffd276')
        self.tabla.tag_configure('Diccionario', background='#ffbf3c')
        self.tabla.tag_configure('Compendio', background='#fffd8d')
        # kawaii pastel Color Palette
        self.tabla.tag_configure('Manual', background='#f9b428')
        self.tabla.tag_configure('Otros', background='#f2e2ff')
        self.tabla.tag_configure('Falta', background='#fdaaaa')
        self.tabla.tag_configure('Baja', background='#ddfffc')
        self.tabla.tag_configure('Repuesto', background='#d0d3d4')


        self.tabla.bind("<<TreeviewSelect>>", self.obtener_lamina)
        self.tabla.bind("<Double-1>", self.eliminar_lamina)

    def mostrar_laminas(self):
        self.limpiar_campos()
        l_datos = self.bd.show_laminas()
        self.tabla.delete(*self.tabla.get_children())
        i = -1
        for fila in l_datos:
            i = i+1
            if fila[1] != 'Baja':
                if fila[1] == 'Historia y Geografia':
                    self.tabla.insert('', i,text=i+1, values=fila[0:9], tags='HyG')
                elif fila[1] == 'Lenguaje y Comunicacion':
                    self.tabla.insert('', i,text=i+1, values=fila[0:9], tags='LyC')
                elif fila[1] == 'Comprension Lectora':
                    self.tabla.insert('', i,text=i+1, values=fila[0:9], tags='ComLectora')
                elif fila[1] == 'Arte y Musica':
                    self.tabla.insert('', i,text=i+1, values=fila[0:9], tags='AyM')
                elif fila[1] == 'Educacion Fisica':
                    self.tabla.insert('', i,text=i+1, values=fila[0:9], tags='EduFis')
                elif fila[1] == None:
                    self.tabla.insert('', i,text=i+1, values=fila[0:9], tags='Agregar')
                else:
                    self.tabla.insert('', i,text=i+1, values=fila[0:9], tags=fila[1])
        
    def obtener_lamina(self, event):
        item_selec = self.tabla.focus()
        diccionario_fila = self.tabla.item(item_selec)
        if 'values' in diccionario_fila and len(diccionario_fila['values']) >= 4:
            self.titulo.set(diccionario_fila['values'][0])
            self.categoria.set(diccionario_fila['values'][1])
            if self.categoria.get() == "Persona, Familia, Comunidad y Civismo":
                self.categoria.set("P.F.C.C")
            elif self.categoria.get() == "Manual para profesores":
                self.categoria.set("Manual")
            elif self.categoria.get() == "Repuesto":
                self.categoria.set("Otros")
            self.codigo.set(diccionario_fila['values'][2])
            self.cantidad.set(diccionario_fila['values'][3])
            self.remitente.set(diccionario_fila['values'][4])
            self.condicion_lamina.set(diccionario_fila['values'][5])
            self.nivel_educativo.set(diccionario_fila['values'][6])
            self.año_recepcion.set(diccionario_fila['values'][7])
        else:
            self.limpiar_campos()
            
            
    def limpiar_campos(self):
        self.titulo.set('')
        self.categoria.set('')
        self.codigo.set('')
        self.cantidad.set(0)
        self.remitente.set('')
        self.condicion_lamina.set('')
        self.nivel_educativo.set('')
        self.año_recepcion.set('')
    
    def actualizar_lamina(self):
        #? LAMINAID ES 8
        item_l = self.tabla.focus()
        diccionario_lamina = self.tabla.item(item_l)
        if len(diccionario_lamina['values']) >= 6:
            tabla_laminas = self.bd.show_laminas()
            lista_codigos = []
            for fila in tabla_laminas:
                lista_codigos.append(fila[2])
                
            # print(codigo_lamina)
            idlamina_tabla = diccionario_lamina['values'][8]
            for fila in tabla_laminas:
                laminasid_bd = fila[8]
                # print(laminasid_bd)
                if laminasid_bd == idlamina_tabla and idlamina_tabla != '':
                    titulo = self.titulo.get()
                    categoria = self.categoria.get()
                    codigo = self.codigo.get()
                    cantidad = self.cantidad.get()
                    remitente = self.remitente.get()
                    condicionlamina = self.condicion_lamina.get()
                    niveleducativo = self.nivel_educativo.get()
                    añorecepcion = self.año_recepcion.get()
                    
                    confirmar_box = messagebox.askokcancel('Información', 'Se modificará la fila seleccionada')
                    #! FALLO
                    if categoria and niveleducativo and titulo and cantidad and condicionlamina and codigo != '' and confirmar_box == True:
                        codigo_lamina = diccionario_lamina['values'][2]
                        if (str(codigo_lamina) == str(codigo)) or (codigo not in lista_codigos):
                            categoriaid = self.cat_dic[categoria]
                            self.bd.update_lamina(idlamina_tabla, codigo, remitente, añorecepcion, niveleducativo, titulo, condicionlamina, cantidad, categoriaid)
                            messagebox.showinfo('Información', 'Fila modificada')
                            self.mostrar_laminas()
                        elif codigo in lista_codigos:
                            messagebox.showerror('ERROR', 'Codigo Existente')
                    else:
                        messagebox.showerror('ERROR', 'Falta Rellenar')
        elif len(diccionario_lamina['values']) == 0:
            # print(len(diccionario_lamina['values']))
            messagebox.showerror('ERROR', 'Selecciona una lamina')
        else:
            messagebox.showerror('ERROR', 'Falta Rellenar')
            
    def agregar_lamina(self):
        titulo = self.titulo.get()
        categoria = self.categoria.get()
        codigo = self.codigo.get()
        cantidad = self.cantidad.get()
        remitente = self.remitente.get()
        condicionlamina = self.condicion_lamina.get()
        niveleducativo = self.nivel_educativo.get()
        añorecepcion = self.año_recepcion.get()

        if categoria and codigo and niveleducativo and titulo and condicionlamina and cantidad != '':
            tabla_laminas = self.bd.show_laminas()
            lista_codigos = []
            for fila in tabla_laminas:
                lista_codigos.append(fila[2])
            
            if codigo not in lista_codigos:
                c_filas = len(self.tabla.get_children())
                datos = (remitente, añorecepcion, niveleducativo, titulo, condicionlamina, codigo, cantidad, categoria)

                question_box = messagebox.askquestion('Información', '¿Desea agregar la fila?')
                if question_box == 'yes' and cantidad > 0:
                    categoriaid = self.cat_dic[categoria]
                    self.bd.append_lamina(codigo, remitente, añorecepcion, niveleducativo, titulo, condicionlamina, cantidad, categoriaid)
                    # self.tabla.insert('', "end", text=c_filas+1, values=datos, tags=categoria)
                    self.mostrar_laminas()
                    messagebox.showinfo('Información', 'Fila agregada')
                    self.limpiar_campos()
                elif question_box == 'yes' and cantidad == 0:
                    messagebox.showerror('ERROR', 'La Cantidad es 0')
            elif codigo in lista_codigos:
                messagebox.showerror('ERROR', 'Codigo Existente')
        else:
            messagebox.showerror('ERROR', 'Falta Rellenar datos')
            
                    
        
    def eliminar_lamina(self, event):
        self.limpiar_campos()
        l_item = self.tabla.selection()[0]
        diccionario_fila = self.tabla.item(l_item)
        question_box = messagebox.askquestion('Información', '¿Desea eliminar la fila?')

        if question_box == 'yes':
            self.tabla.delete(l_item)
            self.bd.delete_lamina(diccionario_fila['values'][8])
            messagebox.showinfo('Información', 'Fila Eliminada')

    
    def buscar_laminas(self):
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
                if fila[1] != 'Baja':
                    if fila[1] == 'Historia y Geografia':
                        self.tabla.insert('', i,text=i+1, values=fila[0:9], tags='HyG')
                    elif fila[1] == 'Lenguaje y Comunicacion':
                        self.tabla.insert('', i,text=i+1, values=fila[0:9], tags='LyC')
                    elif fila[1] == 'Comprension Lectora':
                        self.tabla.insert('', i,text=i+1, values=fila[0:9], tags='ComLectora')
                    elif fila[1] == 'Arte y Musica':
                        self.tabla.insert('', i,text=i+1, values=fila[0:9], tags='AyM')
                    elif fila[1] == 'Educacion Fisica':
                        self.tabla.insert('', i,text=i+1, values=fila[0:9], tags='EduFis')
                    elif fila[1] == None:
                        self.tabla.insert('', i,text=i+1, values=fila[0:9], tags='Agregar')
                    else:
                        self.tabla.insert('', i,text=i+1, values=fila[0:9], tags=fila[1])

        else:
            messagebox.showerror('ERROR', 'No se agrego una busqueda')

    
    def dar_baja(self):
        l_item = self.tabla.focus()
        diccionario_lamina = self.tabla.item(l_item)
        cantidad_baja = self.cantidad.get()
        condicion = self.condicion_lamina.get()
        if 'values' in diccionario_lamina and len(diccionario_lamina['values']) != 0:
            question_box = messagebox.askquestion('Información', '¿Desea dar de baja la lamina seleccionada?')
            if question_box == 'yes' and cantidad_baja != 0 and condicion != '':
                titulo = diccionario_lamina['values'][0]
                categoria = 24
                codigo = diccionario_lamina['values'][2]
                cantidad_t = diccionario_lamina['values'][3]
                remitente = diccionario_lamina['values'][4]
                nivel_edu = diccionario_lamina['values'][6]
                a_recepcion = diccionario_lamina['values'][7]
                laminaid = diccionario_lamina['values'][8]
                if cantidad_t > cantidad_baja and cantidad_baja > 0:
                    self.bd.append_lamina(codigo,remitente,a_recepcion,nivel_edu,titulo,condicion,cantidad_baja,categoria)
                    cantidad_nueva = cantidad_t - cantidad_baja
                    self.bd.update_lamina_cantidad(laminaid,cantidad_nueva)
                    messagebox.showinfo('Información', 'Lamina dada de baja')
                    self.mostrar_laminas()
                elif cantidad_t == cantidad_baja and cantidad_baja > 0:
                    self.bd.update_lamina(laminaid,codigo,remitente,a_recepcion,nivel_edu,titulo,condicion,cantidad_baja,categoria)
                    messagebox.showinfo('Información', 'Lamina dada de baja')
                    self.mostrar_laminas()
                elif cantidad_t < cantidad_baja and cantidad_baja > 0:
                    messagebox.showerror('ERROR', 'Cantidad erronea')
                else:
                    messagebox.showerror('ERROR', 'Proceso erroneo')
            else:
                messagebox.showerror('ERROR', 'Cantidad erronea')
        else:
            messagebox.showerror('ERROR', 'Selecciona una lamina')

    def guardar_laminas(self):
        self.limpiar_campos()
        self.informe.save_laminas()
        messagebox.showinfo('Informacion', 'Datos guardados')
        