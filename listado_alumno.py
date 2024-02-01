from conexion_sqlite import Comunicacion
import csv

bd = Comunicacion()

filename1 = "data/rptListadoEstudiantes.csv"
filename2 = "data/rptListadoEstudiantes2.csv"
with open(filename2) as f:
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
# print(filas_bd)