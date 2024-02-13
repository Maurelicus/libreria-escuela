import sqlite3

class Comunicacion():
    
    def __init__(self):
        self.bd = sqlite3.connect("data/BDprueba3.db")
    #! VENTANA 1
    def update_libros(self, id, remitente, año_recepcion, nivel_educativo, titulo, autor, editorial, año_edicion, condicion_libro, cantidad):
        cursor = self.bd.cursor()
        query = '''
        UPDATE libros
        SET Remitente = '{}', AñoRecepcion = '{}', NivelEducativo = '{}', Titulo = '{}', Autor = '{}', Editorial = '{}', AñoEdicion = '{}', CondicionLibro = '{}', Cantidad = '{}'
        WHERE LibroId = '{}'
        '''.format(remitente, año_recepcion, nivel_educativo, titulo, autor, editorial, año_edicion, condicion_libro, cantidad, id)
        cursor.execute(query)
        self.bd.commit()
        cursor.close()
    
    def show_libros(self):
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
    
    def agregar_libro(self, remitente, año_recepcion, nivel_educativo, titulo, autor, editorial, año_edicion, condicion_libro, cantidad):
        cursor = self.bd.cursor()
        query = '''
        INSERT INTO libros (Remitente, AñoRecepcion, NivelEducativo, Titulo, Autor, Editorial, AñoEdicion, CondicionLibro, Cantidad)
        VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}')
        '''.format(remitente, año_recepcion, nivel_educativo, titulo, autor, editorial, año_edicion, condicion_libro, cantidad)
        cursor.execute(query)
        self.bd.commit()
        cursor.close()

    def delete_libro(self, id):
        cursor = self.bd.cursor()
        query = '''
        DELETE FROM libros
        WHERE LibroId = '{}'        
        '''.format(id)
        cursor.execute(query)
        self.bd.commit()
        cursor.close()
    
    def buscar_libros(self, columna, palabra):
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
        WHERE 
            {} LIKE '%{}%'
        '''.format(columna,palabra)
        cursor.execute(query)
        l_filas = cursor.fetchall()
        return l_filas
    #! VENTANA 2
    def show_laminas(self):
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
    
    def delete_lamina(self, id):
        cursor = self.bd.cursor()
        query = '''
        DELETE FROM laminas
        WHERE LaminasId = '{}'        
        '''.format(id)
        cursor.execute(query)
        self.bd.commit()
        cursor.close()
    
    def update_lamina(self, id, codigo, remitente, año_recepcion, nivel_educativo, titulo, condicion_lamina, cantidad):
        cursor = self.bd.cursor()
        query = '''
        UPDATE laminas
        SET Codigo = '{}', Remitente = '{}', AñoRecepcion = '{}', NivelEducativo = '{}', Titulo = '{}', CondicionLamina = '{}', Cantidad = '{}'
        WHERE LaminasId = '{}'
        '''.format(codigo, remitente, año_recepcion, nivel_educativo, titulo, condicion_lamina, cantidad, id)
        cursor.execute(query)
        self.bd.commit()
        cursor.close()
        
    def agregar_lamina(self, codigo, remitente, año_recepcion, nivel_educativo, titulo, condicion_lamina, cantidad):
        cursor = self.bd.cursor()
        query = '''
        INSERT INTO laminas (Codigo, Remitente, AñoRecepcion, NivelEducativo, Titulo, CondicionLamina, Cantidad)
        VALUES('{}','{}','{}','{}','{}','{}','{}')
        '''.format(codigo, remitente, año_recepcion, nivel_educativo, titulo, condicion_lamina, cantidad)
        cursor.execute(query)
        self.bd.commit()
        cursor.close()
        
    def buscar_laminas(self, columna, palabra):
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
        WHERE 
            {} LIKE '%{}%'
        '''.format(columna,palabra)
        cursor.execute(query)
        l_filas = cursor.fetchall()
        return l_filas
    #! PEDIDO
    
    def buscar_usuarios(self, columna, palabra):
        cursor = self.bd.cursor()
        query = '''
        SELECT 
            UsuarioId AS [Codigo],
            Nivel,
            Usuario,
            Grado,
            Seccion,
            Sexo
        FROM 
            usuarios
        WHERE 
            {} LIKE '%{}%'
        '''.format(columna,palabra)
        try:
            cursor.execute(query)
            l_filas = cursor.fetchall()
            return l_filas
        except sqlite3.OperationalError:
            print("incorrecto")
    
    def agregar_libro(self, codigo, libroid, usuarioid, fecha, situacion, observacion, cantidad):
        cursor = self.bd.cursor()
        query = '''
        INSERT INTO pedido_libro (Codigo, LibroId, UsuarioId, FechaSalida, Situacion, Observacion, Cantidad)
        VALUES('{}','{}','{}','{}','{}','{}','{}')
        '''.format(codigo, libroid, usuarioid, fecha, situacion, observacion, cantidad)
        cursor.execute(query)
        self.bd.commit()
        cursor.close()
    
    def update_libro_cantidad(self, libroid, cantidad):
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
    def show_pedidos(self):
        cursor = self.bd.cursor()
        query = '''
        SELECT
            alu.Usuario,
            lib.Titulo,
            pl.Observacion,
            pl.FechaSalida,
            pl.FechaEntrada,
            pl.Situacion,
            pl.Cantidad,
            pl.PedidoId,
            pl.Codigo,
            pl.LibroId,
            pl.UsuarioId
        FROM
            pedido_libro AS pl
        INNER JOIN
            libros AS lib
        ON
            pl.LibroId = lib.LibroId
        INNER JOIN
            usuarios AS alu
        ON
            alu.UsuarioId = pl.UsuarioId
        ORDER BY
            pl.Situacion
        '''
        cursor.execute(query)
        l_filas = cursor.fetchall()
        return l_filas
    
    def buscar_pedidos(self, columna, palabra):
        cursor = self.bd.cursor()
        query = '''
        SELECT
            alu.Usuario AS [Usuario],
            lib.Titulo AS [Libro],
            pl.Observacion,
            pl.FechaSalida AS [Fecha],
            pl.FechaEntrada,
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
            usuarios AS alu
        ON
            alu.UsuarioId = pl.UsuarioId
        WHERE 
            {} LIKE '%{}%'
        '''.format(columna,palabra)
        cursor.execute(query)
        l_filas = cursor.fetchall()
        return l_filas
    
    def info_pedidolibro(self, pedidoid):
        cursor = self.bd.cursor()
        query = '''
        SELECT
            pl.LibroId,
            lib.Cantidad,
            pl.UsuarioId,
            pl.FechaSalida
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
        
    def agregar_pedido(self, codigo, libroid, usuarioid, fecha_s, fecha_e, situacion, observacion, cantidad):
        cursor = self.bd.cursor()
        query = '''
        INSERT INTO pedido_libro (Codigo, LibroId, UsuarioId, FechaSalida, FechaEntrada, Situacion, Observacion, Cantidad)
        VALUES('{}','{}','{}','{}','{}','{}','{}','{}')
        '''.format(codigo, libroid, usuarioid, fecha_s, fecha_e, situacion, observacion, cantidad)
        cursor.execute(query)
        self.bd.commit()
        cursor.close()
        
    def update_pedido(self, pedidoid, fecha_devolucion, situacion, observacion, cantidad):
        cursor = self.bd.cursor()
        query = '''
        UPDATE pedido_libro
        SET FechaEntrada = '{}', Situacion = '{}', Observacion = '{}', Cantidad = '{}'
        WHERE PedidoId = '{}'
        '''.format(fecha_devolucion, situacion, observacion, cantidad, pedidoid)
        cursor.execute(query)
        self.bd.commit()
        cursor.close()

    def agregar_usuario(self, usuarioid, usuario, sexo, nivel, grado, seccion):
        cursor = self.bd.cursor()
        query = '''
        INSERT INTO "usuarios" VALUES ("{}", "{}", "{}", "{}", "{}", "{}")
        '''.format(usuarioid, usuario, sexo, nivel, grado, seccion)
        cursor.execute(query)
        self.bd.commit()
        cursor.close()
        
    def show_usuarios(self):
        cursor = self.bd.cursor()
        query = '''
        SELECT
            UsuarioId,
            Usuario,
            Sexo,
            Nivel,
            Grado,
            Seccion
        FROM 
            Usuarios
        '''
        cursor.execute(query)
        l_filas = cursor.fetchall()
        return l_filas
        