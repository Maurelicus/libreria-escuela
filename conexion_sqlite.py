import sqlite3

class Comunicacion():
    
    def __init__(self):
        self.bd = sqlite3.connect("BDprueba.db")
        
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
        print(columna)
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