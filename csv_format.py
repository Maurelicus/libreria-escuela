from conexion_sqlite import Comunicacion
import sqlite3
import csv

class Nomina():
    def __init__(self):
        self.bd = Comunicacion()
        self.secundaria = "data/secundaria.csv"
        self.primaria = "data/primaria.csv"
        self.tlibros = "data/libros.csv"
        self.files = []
        self.files.append(self.secundaria)
        self.files.append(self.primaria)
        self.basedatos = sqlite3.connect("data/BDprueba.db")

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
                alumno = fila[10] + ", " + fila[8] + " " + fila[9]
                final_alumno = alumno.replace("'", "-")
                usuarios.append(final_alumno)
                codigo = 'u'+fila[7]
                sexo = fila[11]
                grado = fila[2].strip()
                tipo = "Alumno"
                seccion = fila[3].strip()
                fila_bd.append(codigo)
                fila_bd.append(final_alumno)
                fila_bd.append(sexo)
                fila_bd.append(nivel)
                fila_bd.append(grado)
                fila_bd.append(seccion)
                filas_bd.append(fila_bd)
                self.bd.append_alumno(codigo, final_alumno, sexo, nivel, grado, seccion, tipo)
            # print(filas_bd)
    def agregar_tlibros(self):
        """ 
        cursor = self.basedatos.cursor()
        query = '''
        CREATE TABLE "libros" (
            "LibroId"	INTEGER NOT NULL,
            "Titulo"	NVARCHAR(160) NOT NULL,
            "Autor"	NVARCHAR(160),
            "Editorial"	NVARCHAR(100),
            "AñoEdicion"	INTEGER,
            "Tipo"	INTEGER NOT NULL,
            "Remitente"	NVARCHAR(20),
            "NivelEducativo"	NVARCHAR(20) NOT NULL,
            "CondicionLibro"	NVARCHAR(2) NOT NULL,
            "AñoRecepcion"	INTEGER,
            "Cantidad"	INTEGER NOT NULL,
            PRIMARY KEY("LibroId" AUTOINCREMENT),
            FOREIGN KEY("Tipo") REFERENCES "categorias"("TipoId") ON DELETE NO ACTION ON UPDATE NO ACTION
        )
        '''
        cursor.execute(query)
        """

        with open(self.tlibros, encoding="utf-8") as f:
            reader = csv.reader(f)
            datos_t = list(reader)
            datos = datos_t[1:]
            filas_procesadas = []
            for fila_obtenida in datos:
                if len(fila_obtenida)>10 :
                    filas_procesadas.append(fila_obtenida)
        for fila in filas_procesadas:
            # print(fila)
            titulo = fila[1]
            final_titulo = titulo.replace("'", "-")
            autor = fila[2]
            final_autor = autor.replace("'", "-")
            editorial = fila[3]
            final_editorial = editorial.replace("'", "-")
            aedicion = fila[4]
            tipoid = fila[5]
            remitente = fila[6]
            niveleducativo = fila[7]
            condicion = fila[8]
            arecepcion = fila[9]
            cantidad = fila[10]
            self.bd.append_libro(remitente, arecepcion, niveleducativo, final_titulo, final_autor, final_editorial ,aedicion, condicion, cantidad, tipoid)

nomina1 = Nomina()
# nomina1.agregar_nomina()
nomina1.agregar_tlibros()