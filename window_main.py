from tkinter import messagebox, PhotoImage, Canvas
from ttkbootstrap.constants import *
import ttkbootstrap as ttk

from inventario.vinventario import NotebookInventario
from alumno.valumno import NotebookAlumno
from profesor.vprofesor import NotebookProfesor

class VentanaMain():
    def __init__(self):

        # journal-minty-united-morph
        self.root = ttk.Window(themename= 'minty')
        self.nombre = 'Biblioteca Ricardo Florez Guterres'
        self.root.title(f'{self.nombre}')
        self.root.maxsize(width=640, height=427)
        self.root.minsize(width=640, height=427)
        # self.root.protocol("WM_DELETE_WINDOW", self.cerrar_aplicacion)
        self.bg = PhotoImage(file='images/fondo.png')
        self.logo_tk = PhotoImage(file='images/logo_colegio.png')
        self.libro_tk = PhotoImage(file='images/libros.png')
        self.alumno_tk = PhotoImage(file='images/estudiante.png')
        self.profesor_tk = PhotoImage(file='images/profesor.png')
        self.vmain()
        
    def vmain(self):
        
        my_canvas = Canvas(self.root, width=640, height=426)
        my_canvas.create_image(0,0, image = self.bg, anchor='nw')
        my_canvas.create_image(250,90,image=self.logo_tk, anchor='nw')
        my_canvas.create_image(305,298,image=self.libro_tk, anchor='nw')
        my_canvas.create_image(95,298,image=self.alumno_tk, anchor='nw')
        my_canvas.create_image(497,295,image=self.profesor_tk, anchor='nw')
        my_canvas.create_text(
            320, 30, fill='#fdfefe', font=("Chandas", 22),
            text='Biblioteca Ricardo Florez Gutierrez')
        my_canvas.pack(fill='both', expand=True)

        ingresar_button = ttk.Button(
            self.root, text='Inventario', 
            command = self.ingresar_inventario, 
            bootstyle='dark-outline')
        # ingresar_button.bind("<Return>", str(lambda: ingresar_inventario()))
        alumno_button = ttk.Button(
            self.root, text='Alumno', 
            command = self.ingresar_alumno, 
            bootstyle='dark-outline')
        # alumno_button.bind("<Return>", str(lambda: ingresar_alumno()))
        profesor_button = ttk.Button(
            self.root, text='Profesor', 
            command = self.ingresar_profesor, 
            bootstyle='dark-outline')
        # profesor_button.bind("<Return>", str(lambda: ingresar_profesor()))
        
        my_canvas.create_window(290,360,anchor='nw', window=ingresar_button)
        my_canvas.create_window(90,360,anchor='nw', window=alumno_button)
        my_canvas.create_window(490,360,anchor='nw', window=profesor_button)

    def ingresar_inventario(self):

        def cerrar_inventario():
            self.root.deiconify()  # Muestra la ventana principal
            ven_inventario.destroy()
            
        self.root.withdraw()
        ven_inventario = ttk.Toplevel()
        ven_inventario.title(f'Inventario de la {self.nombre}')
        ven_inventario.minsize(width=1300, height=700)
        # 1440x900
        ven_inventario.geometry('1000x600')
        ven_inventario.columnconfigure(0, weight=1)
        ven_inventario.rowconfigure(0, weight=1)
        ven_inventario.protocol("WM_DELETE_WINDOW", cerrar_inventario)
        NotebookInventario(ven_inventario)
            
    def ingresar_alumno(self):

        def cerrar_alumno():
            self.root.deiconify()  # Muestra la ventana principal
            ven_alumno.destroy()
            
        self.root.withdraw()
        ven_alumno = ttk.Toplevel()
        ven_alumno.title(f'{self.nombre} - Parte Alumno')
        ven_alumno.minsize(width=1300, height=700)
        # 1440x900
        ven_alumno.geometry('1000x600')
        ven_alumno.columnconfigure(0, weight=1)
        ven_alumno.rowconfigure(0, weight=1)
        ven_alumno.protocol("WM_DELETE_WINDOW", cerrar_alumno)
        NotebookAlumno(ven_alumno)

    def ingresar_profesor(self):

        def cerrar_profesor():
            self.root.deiconify()  # Muestra la ventana principal
            ven_profesor.destroy()
            
        self.root.withdraw()
        ven_profesor = ttk.Toplevel()
        ven_profesor.title(f'{self.nombre} - Parte Profesor')
        ven_profesor.minsize(width=1300, height=700)
            # 1440x900
        ven_profesor.geometry('1000x600')
        ven_profesor.columnconfigure(0, weight=1)
        ven_profesor.rowconfigure(0, weight=1)
        ven_profesor.protocol("WM_DELETE_WINDOW", cerrar_profesor)
        NotebookProfesor(ven_profesor)
        
""" 
    def cerrar_aplicacion(self):
        if messagebox.askokcancel("Cerrar Aplicación", "¿Desea salir?"):
            self.root.destroy()
"""

