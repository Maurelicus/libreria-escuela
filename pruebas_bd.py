from tkinter import *
from tkinter import font

def dar_baja(self):
        self.limpiar_campos()
        item_l = self.tabla.focus()
        diccionario_fila = self.tabla.item(item_l)
        messagebox.showinfo('Informacion', 'Datos eliminados')
        question_box = messagebox.askquestion('Información', '¿Desea eliminar la fila?')
