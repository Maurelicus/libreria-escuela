import sqlite3

class Comunicacion():
    
    def __init__(self):
        self.bd = sqlite3.connect("base_de_dato1.db")
        
    def actualizar_fila(self, id, remitente, año_recepcion, nivel_educativo, titulo, autor, editorial, año_edicion, condicion_libro, cantidad):
        cursor = self.bd.cursor()
        query = '''
        UPDATE bienes_culturales
        SET REMITENTE = '{}', AÑO_RECEPCION = '{}', NIVEL_EDUCATIVO = '{}', TITULO = '{}', AUTOR = '{}', EDITORIAL = '{}', AÑO_EDICION = '{}', ESTADO = '{}', CANTIDAD = '{}'
        WHERE ID = '{}'
        '''.format(remitente, año_recepcion, nivel_educativo, titulo, autor, editorial, año_edicion, condicion_libro, cantidad, id)
        cursor.execute(query)
        self.bd.commit()
        cursor.close()
    
    def mostrar_datos(self):
        cursor = self.bd.cursor()
        query = "SELECT * FROM bienes_culturales"
        cursor.execute(query)
        l_filas = cursor.fetchall()
        return l_filas
    
    def insertar_fila(self, remitente, año_recepcion, nivel_educativo, titulo, autor, editorial, año_edicion, condicion_libro, cantidad):
        cursor = self.bd.cursor()
        query = '''
        INSERT INTO bienes_culturales (REMITENTE, ANO_RECEPCION, NIVEL_EDUCATIVO, TITULO, AUTOR, EDITORIAL, ANO_EDICION, ESTADO, CANTIDAD)
        VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}')
        '''.format(remitente, año_recepcion, nivel_educativo, titulo, autor, editorial, año_edicion, condicion_libro, cantidad)
        cursor.execute(query)
        self.bd.commit()
        cursor.close()

    def eliminar_fila(self, id):
        cursor = self.bd.cursor()
        query = '''
        DELETE FROM bienes_culturales
        WHERE ID = '{}'        
        '''.format(id)
        cursor.execute(query)
        self.bd.commit()
        cursor.close()
    """ 
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