import sqlite3

class Comunicacion():
    
    def __init__(self):
        self.bd = sqlite3.connect("BDprueba3.db")
    #! VENTANA 1
    def actualizar_filav1(self, id, remitente, año_recepcion, nivel_educativo, titulo, autor, editorial, año_edicion, condicion_libro, cantidad):
        cursor = self.bd.cursor()
        query = '''
        UPDATE libros
        SET Remitente = '{}', AñoRecepcion = '{}', NivelEducativo = '{}', Titulo = '{}', Autor = '{}', Editorial = '{}', AñoEdicion = '{}', CondicionLibro = '{}', Cantidad = '{}'
        WHERE LibroId = '{}'
        '''.format(remitente, año_recepcion, nivel_educativo, titulo, autor, editorial, año_edicion, condicion_libro, cantidad, id)
        cursor.execute(query)
        self.bd.commit()
        cursor.close()
    
    def mostrar_datosv1(self):
        cursor = self.bd.cursor()
        query = '''
        SELECT 
            Remitente,
            AñoRecepcion,
            NivelEducativo,
            Titulo,
            Autor,
            Editorial,
            AñoEdicion,
            CondicionLibro,
            Cantidad,
            LibroId
        FROM 
            libros
        '''
        cursor.execute(query)
        l_filas = cursor.fetchall()
        return l_filas
    
    def insertar_filav1(self, remitente, año_recepcion, nivel_educativo, titulo, autor, editorial, año_edicion, condicion_libro, cantidad):
        cursor = self.bd.cursor()
        query = '''
        INSERT INTO libros (Remitente, AñoRecepcion, NivelEducativo, Titulo, Autor, Editorial, AñoEdicion, CondicionLibro, Cantidad)
        VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}')
        '''.format(remitente, año_recepcion, nivel_educativo, titulo, autor, editorial, año_edicion, condicion_libro, cantidad)
        cursor.execute(query)
        self.bd.commit()
        cursor.close()

    def eliminar_filav1(self, id):
        cursor = self.bd.cursor()
        query = '''
        DELETE FROM libros
        WHERE LibroId = '{}'        
        '''.format(id)
        cursor.execute(query)
        self.bd.commit()
        cursor.close()
    
    def buscadorv1(self, columna, palabra):
        cursor = self.bd.cursor()
        # print(columna)
        query = '''
        SELECT 
            Remitente,
            AñoRecepcion,
            NivelEducativo,
            Titulo,
            Autor,
            Editorial,
            AñoEdicion,
            CondicionLibro,
            Cantidad,
            LibroId
        FROM 
            libros
        WHERE 
            {} LIKE '%{}%'
        '''.format(columna,palabra)
        cursor.execute(query)
        l_filas = cursor.fetchall()
        return l_filas
    #! VENTANA 2
    def mostrar_datosv2(self):
        cursor = self.bd.cursor()
        query = '''
        SELECT
            Codigo,
            Remitente,
            AñoRecepcion,
            NivelEducativo,
            Titulo,
            CondicionLamina,
            Cantidad,
            LaminasId
        FROM 
            laminas
        '''
        cursor.execute(query)
        l_filas = cursor.fetchall()
        return l_filas
    
    def eliminar_filav2(self, id):
        cursor = self.bd.cursor()
        query = '''
        DELETE FROM laminas
        WHERE LaminasId = '{}'        
        '''.format(id)
        cursor.execute(query)
        self.bd.commit()
        cursor.close()
    
    def actualizar_filav2(self, id, codigo, remitente, año_recepcion, nivel_educativo, titulo, condicion_lamina, cantidad):
        cursor = self.bd.cursor()
        query = '''
        UPDATE laminas
        SET Codigo = '{}', Remitente = '{}', AñoRecepcion = '{}', NivelEducativo = '{}', Titulo = '{}', CondicionLamina = '{}', Cantidad = '{}'
        WHERE LaminasId = '{}'
        '''.format(codigo, remitente, año_recepcion, nivel_educativo, titulo, condicion_lamina, cantidad, id)
        cursor.execute(query)
        self.bd.commit()
        cursor.close()
        
    def insertar_filav2(self, codigo, remitente, año_recepcion, nivel_educativo, titulo, condicion_lamina, cantidad):
        cursor = self.bd.cursor()
        query = '''
        INSERT INTO laminas (Codigo, Remitente, AñoRecepcion, NivelEducativo, Titulo, CondicionLamina, Cantidad)
        VALUES('{}','{}','{}','{}','{}','{}','{}')
        '''.format(codigo, remitente, año_recepcion, nivel_educativo, titulo, condicion_lamina, cantidad)
        cursor.execute(query)
        self.bd.commit()
        cursor.close()
        
    def buscadorv2(self, columna, palabra):
        cursor = self.bd.cursor()
        # print(columna)
        query = '''
        SELECT 
            Codigo,
            Remitente,
            AñoRecepcion,
            NivelEducativo,
            Titulo,
            CondicionLamina,
            Cantidad,
            LaminasId
        FROM 
            laminas
        WHERE 
            {} LIKE '%{}%'
        '''.format(columna,palabra)
        cursor.execute(query)
        l_filas = cursor.fetchall()
        return l_filas
    #! PEDIDO
    def buscador_librov3(self, columna, palabra):
        cursor = self.bd.cursor()
        # print(columna)
        query = '''
        SELECT 
            NivelEducativo,
            Titulo,
            Autor,
            Editorial,
            AñoEdicion,
            Cantidad,
            LibroId
        FROM 
            libros
        WHERE 
            {} LIKE '%{}%'
        '''.format(columna,palabra)
        cursor.execute(query)
        l_filas = cursor.fetchall()
        return l_filas
    
    def buscador_alumnov3(self, columna, palabra):
        cursor = self.bd.cursor()
        # print(columna)
        query = '''
        SELECT 
            EstudianteId,
            Nivel,
            Usuario,
            Grado,
            Seccion,
            Sexo
        FROM 
            alumnos
        WHERE 
            {} LIKE '%{}%'
        '''.format(columna,palabra)
        cursor.execute(query)
        l_filas = cursor.fetchall()
        return l_filas
    
    def insertar_filav3(self, codigo, libroid, usuarioid, fecha, situacion, observacion, cantidad):
        cursor = self.bd.cursor()
        query = '''
        INSERT INTO pedido_libro (Codigo, LibroId, UsuarioId, Fecha, Situacion, Observacion, Cantidad)
        VALUES('{}','{}','{}','{}','{}','{}','{}')
        '''.format(codigo, libroid, usuarioid, fecha, situacion, observacion, cantidad)
        cursor.execute(query)
        self.bd.commit()
        cursor.close()
        
    def cantidadv3(self, libroid):
        cursor = self.bd.cursor()
        query = '''
        SELECT
            Cantidad
        FROM
            libros
        WHERE
            LibroId = {}'''.format(libroid)
        cursor.execute(query)
        cantidad_total = cursor.fetchall()
        return cantidad_total
    
    def actualizar_filav3(self, libroid, cantidad):
        cursor = self.bd.cursor()
        query = '''
        UPDATE libros
        SET Cantidad = '{}'
        WHERE LibroId = '{}'
        '''.format(cantidad, libroid)
        cursor.execute(query)
        self.bd.commit()
        cursor.close()
        
    #! DEVOLUCIONES
    def mostrar_datosv4(self):
        cursor = self.bd.cursor()
        query = '''
        SELECT
            alu.Usuario,
            lib.Titulo,
            pl.Observacion,
            pl.Fecha,
            pl.Situacion,
            pl.Cantidad,
            pl.PedidoId
        FROM
            pedido_libro AS pl
        INNER JOIN
            libros AS lib
        ON
            pl.LibroId = lib.LibroId
        INNER JOIN
            alumnos AS alu
        ON
            alu.EstudianteId = pl.UsuarioId
        '''
        cursor.execute(query)
        l_filas = cursor.fetchall()
        return l_filas
    
    def buscadorv4(self, columna, palabra):
        cursor = self.bd.cursor()
        # print(columna)
        query = '''
        SELECT
            alu.Usuario AS [Alumno],
            lib.Titulo AS [Libro],
            pl.Observacion,
            pl.Fecha AS [Fecha],
            pl.Situacion AS [Situacion],
            pl.Cantidad,
            pl.PedidoId
        FROM
            pedido_libro AS pl
        INNER JOIN
            libros AS lib
        ON
            pl.LibroId = lib.LibroId
        INNER JOIN
            alumnos AS alu
        ON
            alu.EstudianteId = pl.UsuarioId
        WHERE 
            {} LIKE '%{}%'
        '''.format(columna,palabra)
        cursor.execute(query)
        l_filas = cursor.fetchall()
        return l_filas
    
    def obtener_librov4(self, pedidoid):
        cursor = self.bd.cursor()
        query = '''
        
        SELECT
            pl.LibroId,
            lib.cantidad
        FROM
            pedido_libro AS pl
        INNER JOIN
            libros AS lib
        ON
            pl.LibroId = lib.LibroId
        WHERE 
            PedidoId = {}
        '''.format(pedidoid)
        cursor.execute(query)
        idlibro = cursor.fetchall()
        return idlibro
    
    def actualizar_filav4(self, pedidoid, fecha, situacion, observacion):
        cursor = self.bd.cursor()
        query = '''
        UPDATE pedido_libro
        SET Fecha = '{}', Situacion = '{}', Observacion = '{}'
        WHERE PedidoId = '{}'
        '''.format(fecha, situacion, observacion, pedidoid)
        cursor.execute(query)
        self.bd.commit()
        cursor.close()
