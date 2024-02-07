from tkinter import messagebox
import tkinter as tk
import ttkbootstrap as ttk
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

root = ttk.Window(themename= 'superhero')
root.title('Biblioteca Colegio')
root.minsize(width=1200, height=650)
root.geometry('1080x747')
root.protocol("WM_DELETE_WINDOW", cerrar_aplicacion)
imagen1 = Image.open('images/library.jpg').resize((1080,647))
image_tk = ImageTk.PhotoImage(imagen1)

label = ttk.Label(root, text = 'libreria', image= image_tk)
label.pack()
button1 = ttk.Button(root, text='ingresar', command = ingresar)
button1.pack()

root.mainloop()