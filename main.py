from tkinter import messagebox, PhotoImage, Canvas, font
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk

from inventario import NotebookInventario
from alumno import NotebookAlumno


def ingresar_inventario():

    def cerrar_inventario():
        root.deiconify()  # Muestra la ventana principal
        ven_inventario.destroy()
        
    if __name__ == "__main__":
        root.withdraw()
        ven_inventario = ttk.Toplevel()
        ven_inventario.title('Biblioteca Colegio')
        ven_inventario.minsize(width=1300, height=700)
        # 1440x900
        ven_inventario.geometry('1000x600')
        ven_inventario.columnconfigure(0, weight=1)
        ven_inventario.rowconfigure(0, weight=1)
        ven_inventario.protocol("WM_DELETE_WINDOW", cerrar_inventario)
        NotebookInventario(ven_inventario)
        # app.mainloop()        
def ingresar_alumno():

    def cerrar_alumno():
        root.deiconify()  # Muestra la ventana principal
        ven_alumno.destroy()
        
    if __name__ == "__main__":
        root.withdraw()
        ven_alumno = ttk.Toplevel()
        ven_alumno.title('Biblioteca Colegio')
        ven_alumno.minsize(width=1300, height=700)
        # 1440x900
        ven_alumno.geometry('1000x600')
        ven_alumno.columnconfigure(0, weight=1)
        ven_alumno.rowconfigure(0, weight=1)
        ven_alumno.protocol("WM_DELETE_WINDOW", cerrar_alumno)
        NotebookAlumno(ven_alumno)
        # app.mainloop()        
    

def cerrar_aplicacion():
    if messagebox.askokcancel("Cerrar Aplicación", "¿Seguro que quieres salir?"):
        root.destroy()
# journal-minty-united-morph
root = ttk.Window(themename= 'minty')
root.title('Biblioteca Colegio Administrador')
root.maxsize(width=640, height=427)
root.minsize(width=640, height=427)
root.geometry('640x426')
root.protocol("WM_DELETE_WINDOW", cerrar_aplicacion)

bg = PhotoImage(file='images/fondo.png')

logo_imagen = Image.open('images/logo_colegio.png').resize((140,183))
logo_tk = ImageTk.PhotoImage(logo_imagen)

libro_imagen = Image.open('images/libros.png').resize((64,64))
libro_tk = ImageTk.PhotoImage(libro_imagen)

estudiante_imagen = Image.open('images/estudiante.png').resize((64,64))
alumno_tk = ImageTk.PhotoImage(estudiante_imagen)

profesor_imagen = Image.open('images/profesor.png').resize((64,64))
profesor_tk = ImageTk.PhotoImage(profesor_imagen)

my_canvas = Canvas(root, width=640, height=426)
my_canvas.create_image(0,0, image = bg, anchor='nw')
my_canvas.create_image(269,90,image=logo_tk, anchor='nw')
my_canvas.create_image(305,298,image=libro_tk, anchor='nw')
my_canvas.create_image(95,298,image=alumno_tk, anchor='nw')
my_canvas.create_image(497,295,image=profesor_tk, anchor='nw')
my_canvas.create_text(320, 30, text='Biblioteca Ricardo Florez Gutierrez', 
                      fill='#fdfefe', font=("Chandas", 22))
my_canvas.pack(fill='both', expand=True)


ingresar_button = ttk.Button(root, text='Inventario', command = ingresar_inventario, 
                             bootstyle='info-outline')
ingresar_button.bind("<Return>", ingresar_inventario)
inbutton_window = my_canvas.create_window(290,360,anchor='nw', window=ingresar_button)

alumno_button = ttk.Button(root, text='Alumno', command = ingresar_alumno, 
                             bootstyle='info-outline')
alumno_button.bind("<Return>", ingresar_alumno)
inbutton_window = my_canvas.create_window(90,360,anchor='nw', window=alumno_button)

alumno_button = ttk.Button(root, text='Profesor', command = ingresar_alumno, 
                             bootstyle='info-outline')
alumno_button.bind("<Return>", ingresar_alumno)
inbutton_window = my_canvas.create_window(490,360,anchor='nw', window=alumno_button)



root.mainloop()