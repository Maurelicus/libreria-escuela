from conexion_sqlite import Comunicacion
from datetime import date, datetime
from tkinter import messagebox
import csv
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
    
# pregunta_box1 = messagebox.askokcancel('Información', 'Se agregara una nueva fila')
pregunta_box1 = messagebox.askquestion('Información', '¿Estas seguro?')
# pregunta_box1 = messagebox.showerror('Información', '¿Estas seguro?')
# pregunta_box2 = messagebox.showwarning('Información', '¿Estas seguro?')
# pregunta_box1 = messagebox.showinfo('Información', 'Fila modificada')
# pregunta_box4 = messagebox.askyesnocancel('Información', '¿Estas seguro?')

# pregunta_box1 = messagebox.askyesno('Información', '¿Estas seguro?')
# pregunta_box3 = messagebox.askretrycancel('Información', '¿Estas seguro?')
print(pregunta_box1)
"""
""" 
filename = "rptListadoEstudiantes.csv"
with open(filename) as f:
    reader = csv.reader(f)
    datos_t = list(reader)
    datos = datos_t[10:]
    nivel = datos_t[7][4].strip()
    filas_procesadas = []
    for fila_obtenida in datos:
        if len(fila_obtenida)>10 :
            filas_procesadas.append(fila_obtenida)
filas_bd = []
usuarios = []
for fila in filas_procesadas:
    fila_bd = []
    usuario = fila[10] + ", " + fila[8] + " " + fila[9]
    final_usuario = usuario.replace("'", "-")
    usuarios.append(final_usuario)
    estudianteid = fila[7]
    sexo = fila[11]
    grado = fila[2].strip()
    seccion = fila[3].strip()
    fila_bd.append(estudianteid)
    fila_bd.append(final_usuario)
    fila_bd.append(sexo)
    fila_bd.append(nivel)
    fila_bd.append(grado)
    fila_bd.append(seccion)
    filas_bd.append(fila_bd)
    bd.insertar_alumnos(estudianteid, final_usuario, sexo, nivel, grado, seccion)
# print(usuarios)
"""
# print(5/0)