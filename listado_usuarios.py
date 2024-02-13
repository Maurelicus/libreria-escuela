from conexion_sqlite import Comunicacion
import csv

class Nomina():
    def __init__(self):
        self.bd = Comunicacion()
        self.secundaria = "data/secundaria.csv"
        self.primaria = "data/primaria.csv"
        self.files = []
        self.files.append(self.secundaria)
        self.files.append(self.primaria)
        
    def agregar_nomina(self):
        for path in self.files:
            with open(path, encoding="utf-8") as f:
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
                usuarioid = 'u'+fila[7]
                sexo = fila[11]
                grado = fila[2].strip()
                tipo = "alumno"
                seccion = fila[3].strip()
                fila_bd.append(usuarioid)
                fila_bd.append(final_usuario)
                fila_bd.append(sexo)
                fila_bd.append(nivel)
                fila_bd.append(grado)
                fila_bd.append(seccion)
                filas_bd.append(fila_bd)
                self.bd.agregar_usuario(usuarioid, final_usuario, sexo, nivel, grado, seccion, tipo)
            # print(filas_bd)
nomina1 = Nomina()
nomina1.agregar_nomina()