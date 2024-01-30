from conexion_sqlite import Comunicacion
from datetime import date, datetime
from tkinter import messagebox
bd = Comunicacion()

"""
today = date.today()
now = datetime.now()
print(today)
# print(now)

total=4
c_pedida=5
c_restante=total-c_pedida
if total==0:
    print('no hay existentes')
elif c_restante < 0:
    print('cantidad exedida')
else:
    print('correcto')
""" 
# pregunta_box1 = messagebox.askokcancel('Información', 'Se agregara una nueva fila')
pregunta_box1 = messagebox.askquestion('Información', '¿Estas seguro?')
# pregunta_box1 = messagebox.showerror('Información', '¿Estas seguro?')
# pregunta_box2 = messagebox.showwarning('Información', '¿Estas seguro?')
# pregunta_box1 = messagebox.showinfo('Información', 'Fila modificada')
# pregunta_box4 = messagebox.askyesnocancel('Información', '¿Estas seguro?')

# pregunta_box1 = messagebox.askyesno('Información', '¿Estas seguro?')
# pregunta_box3 = messagebox.askretrycancel('Información', '¿Estas seguro?')
print(pregunta_box1)
