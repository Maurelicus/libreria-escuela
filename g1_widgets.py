import tkinter  as tk
from tkinter import ttk

def seccion_uno(frame_uno, lista_metodos, lista_atributos):
    # print(funciones[0])
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
    reminente_entry = ttk.Entry(frame_uno, textvariable=lista_atributos[0])
    reminente_entry.grid(column=1, row=1, padx=5 ,pady=[10,5])
    añorecepcion_entry = ttk.Entry(frame_uno, textvariable=lista_atributos[1])
    añorecepcion_entry.grid(column=1, row=2, padx=5 ,pady=5)
    nied_list = ["Primaria", "Secundaria"]
    niveleducativo_combobox = ttk.Combobox(frame_uno, textvariable=lista_atributos[2] ,value=nied_list)
    niveleducativo_combobox.grid(column=1, row=3, padx=5 ,pady=5)
    niveleducativo_combobox.current(0)
    niveleducativo_combobox.state(["readonly"])
    titulo_entry = ttk.Entry(frame_uno, textvariable=lista_atributos[3])
    titulo_entry.grid(column=1, row=4, padx=5 ,pady=5)
    autor_entry = ttk.Entry(frame_uno, textvariable=lista_atributos[4])
    autor_entry.grid(column=1, row=5, padx=5 ,pady=5)
    editorial_entry = ttk.Entry(frame_uno, textvariable=lista_atributos[5])
    editorial_entry.grid(column=1, row=6, padx=5 ,pady=5)
    añoedicion_entry = ttk.Entry(frame_uno, textvariable=lista_atributos[6])
    añoedicion_entry.grid(column=1, row=7, padx=5 ,pady=5)
    coli_list = ["B", "R"]
    condicionlibro_combobox = ttk.Combobox(frame_uno, textvariable=lista_atributos[7] ,value=coli_list)
    condicionlibro_combobox.grid(column=1, row=8, padx=5 ,pady=5)
    condicionlibro_combobox.current(0)
    condicionlibro_combobox.state(["readonly"])
    cantidad_entry = ttk.Entry(frame_uno, textvariable=lista_atributos[8])
    cantidad_entry.grid(column=1, row=9, padx=5 ,pady=[5,10])
    #! Botones
    clear_boton = ttk.Button(frame_uno, text='Limpiar campos', width=20, command=lista_metodos[0])
    clear_boton.grid(column=1, row=10, padx=5, pady=[5,10])
    update_boton = ttk.Button(frame_uno, text='Actualizar fila', width=20, command=lista_metodos[1])
    update_boton.grid(column=0, row=10, padx=5, pady=[5,10])
    add_boton = ttk.Button(frame_uno, text='Añadir fila', width=20, command=lista_metodos[2])
    add_boton.grid(column=0, row=11, padx=5, pady=[5,10])

def seccion_dos(frame_dos, lista_metodos, lista_atributos, photo1, photo2):
    l_columna = ("Autor", "Titulo", "Editorial", "AñoRecepcion", "AñoEdicion", "Remitente", "NivelEducativo", "AñoEdicion", "CondicionLibro", "Cantidad")
    buscar_palabra = ttk.Combobox(frame_dos, width=20, value=l_columna, textvariable=lista_atributos[1])
    buscar_palabra.current(0)
    buscar_palabra.grid(column=0, row=0, padx=5, pady=5)
    buscar_palabra.state(["readonly"])
    # print(buscar_palabra.get())
    
    
    filtro_libroid = ttk.Entry(frame_dos, textvariable=lista_atributos[0])
    filtro_libroid.grid(column=1, row=0, padx=5 ,pady=1 )

    busc_boton = ttk.Button(frame_dos, text='buscar', width=20, 
                            command=lista_metodos[1])
    busc_boton.grid(column=2, row=0, padx=5, pady=5)

    
    show_boton = ttk.Button(frame_dos, width=20, image=photo1,
                            command=lista_metodos[0])
    show_boton.grid(column=5, row=0, padx=5, pady=5, sticky='w')
    save_boton = ttk.Button(frame_dos, width=20, image=photo2,
                                command=lista_metodos[0])
    save_boton.grid(column=3, row=0, padx=5, pady=5)
        
    