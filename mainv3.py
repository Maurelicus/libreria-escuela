from tkinter import messagebox, PhotoImage, Canvas, font
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk

from ventanav4principal import Ventana


def ingresar():

    def cerrar_nueva_ventana():
        root.deiconify()  # Muestra la ventana principal
        ven_pri.destroy()
        
    if __name__ == "__main__":
        root.withdraw()
        ven_pri = ttk.Toplevel()
        ven_pri.title('Biblioteca Colegio')
        ven_pri.minsize(width=1200, height=650)
        # 1440x900
        ven_pri.geometry('1000x600')
        ven_pri.columnconfigure(0, weight=1)
        ven_pri.rowconfigure(0, weight=1)
        ven_pri.protocol("WM_DELETE_WINDOW", cerrar_nueva_ventana)
        Ventana(ven_pri)
        # app.mainloop()        
    
def cerrar_aplicacion():
    if messagebox.askokcancel("Cerrar Aplicación", "¿Seguro que quieres salir?"):
        root.destroy()

root = ttk.Window(themename= 'morph')
root.title('Biblioteca Colegio Administrador')
root.maxsize(width=640, height=426)
root.minsize(width=640, height=426)
root.geometry('640x426')
root.protocol("WM_DELETE_WINDOW", cerrar_aplicacion)

imagen1 = Image.open('images/logo_colegio.png').resize((180,223))
image_tk = ImageTk.PhotoImage(imagen1)
bg = PhotoImage(file='images/fondo.png')

my_canvas = Canvas(root, width=640, height=426)
my_canvas.pack(fill='both', expand=True)

my_canvas.create_image(0,0, image = bg, anchor='nw')
my_canvas.create_text(320, 30, text='Biblioteca Ricardo Florez Gutierrez', 
                      fill='#fdfefe', font=("Chandas", 22))
my_canvas.create_image(240,90,image=image_tk, anchor='nw')

button1 = ttk.Button(root, text='ingresar', command = ingresar, bootstyle='info-outline')
button1_window = my_canvas.create_window(290,360,anchor='nw', window=button1)


root.mainloop()