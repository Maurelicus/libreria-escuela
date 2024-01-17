import sqlite3

class Comunicacion():
    
    def __init__(self):
        self.bd = sqlite3.connect("BDprueba2.db")
    #! LIBROS
    def actualizar_fila(self, id, remitente, año_recepcion, nivel_educativo, titulo, autor, editorial, año_edicion, condicion_libro, cantidad):
        cursor = self.bd.cursor()
        query = '''
        UPDATE libros
        SET Remitente = '{}', AñoRecepcion = '{}', NivelEducativo = '{}', Titulo = '{}', Autor = '{}', Editorial = '{}', AñoEdicion = '{}', CondicionLibro = '{}', Cantidad = '{}'
        WHERE LibroId = '{}'
        '''.format(remitente, año_recepcion, nivel_educativo, titulo, autor, editorial, año_edicion, condicion_libro, cantidad, id)
        cursor.execute(query)
        self.bd.commit()
        cursor.close()
    
    def mostrar_datos(self):
        cursor = self.bd.cursor()
        query = "SELECT * FROM libros"
        cursor.execute(query)
        l_filas = cursor.fetchall()
        return l_filas
    
    def insertar_fila(self, remitente, año_recepcion, nivel_educativo, titulo, autor, editorial, año_edicion, condicion_libro, cantidad):
        cursor = self.bd.cursor()
        query = '''
        INSERT INTO libros (Remitente, AñoRecepcion, NivelEducativo, Titulo, Autor, Editorial, AñoEdicion, CondicionLibro, Cantidad)
        VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}')
        '''.format(remitente, año_recepcion, nivel_educativo, titulo, autor, editorial, año_edicion, condicion_libro, cantidad)
        cursor.execute(query)
        self.bd.commit()
        cursor.close()

    def eliminar_fila(self, id):
        cursor = self.bd.cursor()
        query = '''
        DELETE FROM libros
        WHERE LibroId = '{}'        
        '''.format(id)
        cursor.execute(query)
        self.bd.commit()
        cursor.close()
    
    def buscador(self, columna, palabra):
        cursor = self.bd.cursor()
        # print(columna)
        query = '''
        SELECT 
            *
        FROM 
            libros
        WHERE 
            {} LIKE '%{}%'
        '''.format(columna,palabra)
        cursor.execute(query)
        l_filas = cursor.fetchall()
        return l_filas
    #! LAMINAS
    def mostrar_datos2(self):
        cursor = self.bd.cursor()
        query = "SELECT * FROM laminas"
        cursor.execute(query)
        l_filas = cursor.fetchall()
        return l_filas
    
    def eliminar_fila2(self, id):
        cursor = self.bd.cursor()
        query = '''
        DELETE FROM laminas
        WHERE LaminasId = '{}'        
        '''.format(id)
        cursor.execute(query)
        self.bd.commit()
        cursor.close()
    
    def actualizar_fila2(self, id, codigo, remitente, año_recepcion, nivel_educativo, titulo, condicion_lamina, cantidad):
        cursor = self.bd.cursor()
        query = '''
        UPDATE laminas
        SET Codigo = '{}', Remitente = '{}', AñoRecepcion = '{}', NivelEducativo = '{}', Titulo = '{}', CondicionLamina = '{}', Cantidad = '{}'
        WHERE LaminasId = '{}'
        '''.format(codigo, remitente, año_recepcion, nivel_educativo, titulo, condicion_lamina, cantidad, id)
        cursor.execute(query)
        self.bd.commit()
        cursor.close()
        
    def insertar_fila2(self, codigo, remitente, año_recepcion, nivel_educativo, titulo, condicion_lamina, cantidad):
        cursor = self.bd.cursor()
        query = '''
        INSERT INTO laminas (Codigo, Remitente, AñoRecepcion, NivelEducativo, Titulo, CondicionLamina, Cantidad)
        VALUES('{}','{}','{}','{}','{}','{}','{}')
        '''.format(codigo, remitente, año_recepcion, nivel_educativo, titulo, condicion_lamina, cantidad)
        cursor.execute(query)
        self.bd.commit()
        cursor.close()
    """ 
    quizas una mejora
    def actualizar_fila(self, id, remitente, año_recepcion, nivel_educativo, titulo, autor, editorial, año_edicion, condicion_libro, cantidad):
        query = '''
        UPDATE bienes_culturales
        SET REMITENTE = ?, AÑO_RECEPCION = ?, NIVEL_EDUCATIVO = ?, TITULO = ?, AUTOR = ?, EDITORIAL = ?, AÑO_EDICION = ?, ESTADO = ?, CANTIDAD = ?
        WHERE ID = ?
        '''
        try:
            with self.bd:
                self.bd.execute(query, (remitente, año_recepcion, nivel_educativo, titulo, autor, editorial, año_edicion, condicion_libro, cantidad, id))
        except sqlite3.Error as e:
            print(f"Error al actualizar fila: {e}")
    
    def mostrar_datos(self):
        query = "SELECT * FROM bienes_culturales"
        try:
            with self.bd:
                cursor = self.bd.execute(query)
                l_filas = cursor.fetchall()
                return l_filas
        except sqlite3.Error as e:
            print(f"Error al recuperar datos: {e}")
            return []
    """